.. title: Creating Proceedings (almost) automatically using python and latex
.. slug: 2009-08-26-Creating-Proceedings-(almost)-automatically-using-python-and-latex
.. date: 2009-08-26 13:36:57
.. type: text
.. tags: latex


In order to produce proceedings for the
`NeuroComp08 <http://2008.neurocomp.fr>`__ that we organized, I used a
combination of LaTeX  and Python to generate a
`PDF <http://2008.neurocomp.fr/neurocomp08proceedings.pdf>`__ from our
preprint server based on `ConfMaster <http://www.confmaster.net/>`__.
This was due to the lack of an appropriate tool for this system and the
need to be flexible to any change made in last minute by the authors. I
used the following steps (these are summarized in the included
`Makefile`
file at the bottom that allowed to rebuild everything when any small
change in these steps were done).

 .. TEASER_END


#. First, in `ConfMaster <http://www.confmaster.net/>`__, download the
   papers from the system (Admistrator/Export DB/Download Files/Submit)
   but also all metadata in CSV format (Admistrator/Export DB/CSV Data
   to export/Papers). The CSV file had to be manually cleaned-up (using
   ``vim`` and ``OpenOffice``) to correct character encoding and some
   errors from users. In fact, people had sometimes accents in their
   names and I found out ultimately that the most flexible way to get
   all accents was to translate everything to a good old latex-type of
   encoding.
#. the following script
   `body.py`
   generated a link between the CSV and the folder of PDFs, but also
   generated index terms in the resulting
   `body.tex`
   file for the creation of the authors and keywords tables:

   #. extracting the information

      #. first, reading the CSV:

         ::

                1 # the csv module allows high-level reading of cells.
                2 import csv, os
                3 root = '.' # where you stored the CSV and the PDF folder
                4
                5 ## gather information from the CSV
                6 papers = list(csv.reader(open(os.path.join(root,'paper_Neurocomp2008.csv'), "rb"), delimiter=',', quotechar = '"'))

      #. getting the index of particular columns of interest identified
         in the first line ``papers[0]`` of the CSV file:

         ::

                1 def index(vector, match):
                2     for index, value in enumerate(vector):
                3         #print value
                4         if value == match:
                5             index_ = index
                6     return index_
                7
                8 index_title = index(papers[0],'Title')
                9 index_contact_author = index(papers[0],'ContactAuthor_LastName')
               10 index_author1 = index(papers[0],'CoAuthor_1_LastName')
               11 index_kw1 = index(papers[0],'Keyword1')

      #. getting the relevant data from the CSV by looping over all
         lines:

         ::

                1 first_author, id = [], []
                2 db = {}
                3 for paper in papers[1:]:
                4     id = int(paper[0])
                5     db.update( {id : {'contact_author':paper[index_contact_author+1] + ', ' + paper[index_contact_author] } })
                6
                7     index = index_author1 #index of the name of Contact author 1
                8     author_list = []
                9     while True:
               10         if len(paper[index])>1:
               11             author_list.append(paper[index+1] + ' ' + '{\\sc ' + paper[index] + '}')
               12         else:
               13             #print paper[index]
               14             break
               15         index += 5
               16     #print author_list
               17     db[id].update({'author_list':author_list})
               18     db[id].update({'title':paper[index_title]})
               19
               20     keywords, index_kw = [] , index_kw1
               21     while (index_kw < index_kw +5):
               22         kw = paper[index_kw]
               23         #print kw
               24         if (kw == ''):
               25             break
               26         else:
               27             keywords.append(kw)
               28         index_kw += 1
               29     db[id].update({'keywords':keywords})

      #. identify relevant papers using the name of the PDF which
         contains its ID:

         ::

                1 ## link the db with the collection of papers retrieved by the export db feature of confmaster
                2 paper_directory = os.path.join(root,'NEUROCOMP2008Submissions_final')
                3
                4 paper_list = os.listdir(paper_directory)
                5
                6 for paper in paper_list:
                7     if paper.find('.pdf') > -1:
                8         conf, id_str, md5 = paper.split('_')
                9         id_list = int(id_str)
               10         #print id_list, paper
               11         db[id_list].update({'pdf':paper} )

      #. remove some:

         ::

                1 ## exclude some papers (rejected / not participating)
                2 list_excluded = [50,57,18,44]
                3 for id in list_excluded:
                4     print ' * Removing ', db[id]['title'], ' from ',  db[id]['author_list']
                5     del db[id]

      #. sorting data

         ::

                1 # sorting the dictionary by contact_author: (see http://code.activestate.com/recipes/52306/)
                2 items=db.items()
                3 backitems = [ [v[1]['contact_author'],v[0]] for v in items]
                4 backitems.sort()
                5 sortedlist=[ backitems[i][1] for i in range(0,len(backitems))]

      #. and manually include the program:

         ::

                1 program=[{'Cortical treatments':[56,16]},
                2             {'Neuron models':[67,39,15,27,47,64,32, 58,48,21,54]},
                3             {'Neural fields and attractor networks':[31,43,8,65]},
                4             {'Computational vision':[19,77,13,41,11,12,38,40]},
                5             {'Biophysical models':[46,9,51,52,59]},
                6             {'Action selection': [22,20,74,37]},
                7             {'Connectionnist models':[6,72]},
                8             {'BMI and signal processing':[42,70,49,60,63,66,45,7,10,14,76,33,75]},
                9             {'Population coding':[61,35,68,26,36,53]},
               10             {'Plasticity and  functional specialization':[69,62,29,5,34,24]},
               11             {'Network dynamics':[28,25,23,73]},
               12             {'Neural interfaces and softwares':[55,71,30]}]

   #. We begin to write the file:

      #. first, the script opens the file and writes a header (I'm using
         `TexShop <http://www.uoregon.edu/~koch/texshop/>`__):

         ::

                1 # write the header
                2 fic = open('body.tex','w')
                3 # write the includes for all papers
                4 fic.write("""%!TEX TS-program = pdflatex
                5 %%!TEX encoding = Latin1
                6 %!TEX root = neurocomp08proceedings.tex
                7 """)

      #. Define the templates of latex commands

         ::

                1 MODEL_include = """\includepdf[pages=-,%saddtotoc={1,subsection,2,%s,%s}]{%s}
                2 """
                3 MODEL_index_first = """\index{author}{%s|bb}
                4 """
                5 MODEL_index = """\index{author}{%s}
                6 """
                7 MODEL_index_kw = """\index{keyword}{%s}
                8 """
                9 MODEL_section = """
               10 \\refstepcounter{section}
               11 \\addcontentsline{toc}{section}{%s}
               12 """

      #. Define a function to correctly write th author list

         ::

                1 def make_author_list(author_list):
                2
                3     if len(author_list)==1:
                4         s= author_list[0]
                5     else:
                6         s= author_list[0]
                7         if len(author_list)>1:
                8             for author in author_list[1:-1]:
                9                 s +=  ', ' +  author
               10         s += ' and ' + author_list[-1]
               11     return s

      #. Main loop

         ::

                1 for themes in program:
                2     print (themes.keys()[0])
                3     fic.write(MODEL_section %(themes.keys()[0]))
                4     for id in themes.values()[0]:
                5         try:
                6             for i_author, author in enumerate(db[id]['author_list']):
                7                 if i_author == 0: fic.write(MODEL_index_first %(author))
                8                 else: fic.write(MODEL_index %(author))
                9             for kw in db[id]['keywords']:
               10                 fic.write(MODEL_index_kw %(kw))
               11
               12             # some papers were not vertically centered, correcting that manually
               13             option = '' # default option
               14             if id == 55: option =' offset = 0 -1cm, '
               15             if id == 65: option =' offset = 0 -1.9cm, '
               16             if id == 13: option =' offset = 0 -2cm, '
               17             if id == 40: option =' offset = 0 -1cm, '
               18             if id == 70: option =' offset = 0 -2cm, '
               19             if id == 62: option =' offset = 0 -1cm, '
               20             if id == 29: option =' offset = 0 -2.5cm, '
               21
               22             if id == 73: option =' offset = 0 1cm, '
               23             if id == 55: option =' offset = 0 -1cm, '
               24             if id == 70: option =' offset = 0 -2cm, '
               25
               26             #print db[id]['title'] + ', ' + db[id]['author_list']
               27             titre = '{\\bf ' + db[id]['title'] + '} by \\emph{' + make_author_list(db[id]['author_list']) + '}'
               28             fic.write(MODEL_include %(option, titre,id,os.path.join(paper_directory,db[id]['pdf']) ))
               29         except:
               30             print ' /!\\ Paper ', db[id], ' has no pdf!'

      #. Closing the file

         ::

                1 fic.close()

#. once this file is created, you may include it in a traditional
   proceedings latex file
   `neurocomp08proceedings.tex`:

   #. Defining the classes: In particular, we use ``pdfpages`` and
      ``multind``.

      ::

          %!TEX TS-program = pdflatex
          %!TEX encoding = ISO Latin 1
          %!TEX root = neurocomp08proceedings.tex
          \documentclass[twoside,a4paper]{article}%,draft
          \usepackage[applemac]{inputenc}%
          %
          \usepackage[final]{pdfpages}%
          \usepackage[pdftex, pdfusetitle ,colorlinks=false,pdfborder={0 0 0},pdftitle={Proceedings of the second french conference on  Computational Neuroscience: NeuroComp08}]{hyperref}%
          %
          \usepackage{makeidx}%,showidx}
          \usepackage{multind,multicol} % http://www.cs.ubc.ca/local/computing/software/latex/local-guide/node24.shtml
          \makeindex{author}%
          \makeindex{keyword}%
          %\renewcommand{\indexname}{List of authors}
          \newcommand{\bb}[1]{{\bf #1}} % to make first author bold
          %
          \usepackage{color}%
          \setlength\fboxsep{3pt}%
          %
          % Support for adding page headers and footers
          \usepackage{fancyhdr}
          %% Set the top and left margins so that the header hugs the to right corner of the paper
          %\topmargin -70pt
          %\oddsidemargin -70pt
          % Commands for adding headers and footers
          \pagestyle{fancy}
          %\fancyhead{} % clear all header fields
          %\fancyhead[RO,LE]{\sectionmark}
          \fancyfoot{} % clear all footer fields
          %\renewcommand{\sectionmark}[1]{\bfseries\markboth{\thesection.\ #1}{}}
          \renewcommand{\sectionmark}[1]{\markboth{#1}{}}
          \fancyfoot[LE,RO]{\thepage}
          \fancyfoot[LO,RE]{\colorbox{white}{Proceedings  of the second french conference on  Computational Neuroscience:  NeuroComp08}}
          \renewcommand{\headrulewidth}{0.2pt}
          \renewcommand{\footrulewidth}{0.4pt}
          %\setlength\textwidth{15cm}
          \setlength\headwidth{18.5cm}
          \setlength\textheight{25.85cm}
          %\setlength\hoffset{1cm}
          \topmargin=-1.95cm
          %\usepackage[a4paper,hmargin=1cm,vmargin=1cm]{geometry}
          %\usepackage[a4paper]{geometry}

   #. Begin the document by including the cover as a one-page PDF
      (converted from a SVG in the
      `Makefile`
      below)

      ::

          \begin{document}
          \includepdf[pages=-]{affiche_NeuroComp.pdf}
          \newpage

          \includepdfset{pages=-,pagecommand=\thispagestyle{fancy}}
          \newpage

   #. Including a page with the BibTex entry and the ISBN number (using macro file ``ean13.tex``)

      ::

          %%  FRONTMATTER:
          %
          %%\emptyheads
          \thispagestyle{empty}
          \include{titlepage}
          %\frontmatter
          %\newpage
          %\setcounter{page}{3}
          %\pagestyle{fancy}
          \pagestyle{empty}
          \subsection*{How to cite this proceedings book?}
          \begin{verbatim}
          @proceedings{NeuroComp08,
                   Title = {Proceedings of the second french conference on
                               Computational Neuroscience, Marseille},
                   Editor = {Laurent U. Perrinet and Emmanuel Dauc{\'e}},
                   Isbn = {978-2-9532965-0-1},
                   Url = {http://2008.neurocomp.fr},
                   Month ={October},
                   Year = {2008}}
          \end{verbatim}
          \vfill
          \begin{flushright}
          \input ean13
          \ISBN 978-2-9532965-0-1 %
          \vspace{2cm}
          \EAN 978-29-532965-0-1
          \end{flushright}
          \newpage
          \pagestyle{empty}
          \setlength{\parskip}{1ex plus 0.3ex minus 0.3ex}
          \setlength{\parindent}{1em}

   #. Some verbose introduction, see also
      `titlepage.tex`:

      ::

          \subsection*{Introduction}
          Ce recueil contient les actes de la seconde conférence française de neurosciences computationnelles qui s'est tenue à Marseille du 8 au 11 octobre 2008.

          Les neurosciences computationnelles portent sur l'étude des processus de traitement de l'information dans le système nerveux, du niveau de la cellule jusqu'à celui des populations de neurones et du contrôle du comportement. Le but de cette conférence est de rassembler des chercheurs issus de différentes disciplines, incluant les neurosciences, les sciences de l'information, la physique statistique ou encore la robotique, afin d'offrir un large panorama des recherches menées dans le domaine.

          Ce recueil présente les 68 contributions qui ont été présentées lors de la conférence, dans leur ordre d'apparition dans le programme. Le premier jour était consacré aux modèles de la cellule neurale, aux modèles des traitements visuels et corticaux, ainsi qu'aux modèles de réseaux de neurones bio-mimétiques. La seconde journée était consacrée aux interfaces cerveau-machine, à la dynamique des grands ensembles de neurones, à la plasticité fonctionnelle et aux interfaces neurales.

          Cette conférence a été rendue possible grâce au soutien de nombreuses institutions, et nous tenons à remercier le CNRS, la Société des neurosciences, Le conseil régional de la région Provence Alpes Côte d'Azur, le conseil général des Bouches de Rhône, la mairie de Marseille, l'université de Provence, l'IFR "Sciences du cerveau et de la cognition", et l'INRIA. Nous remercions chaleureusement la faculté de médecine de Marseille et l'université de la Méditerranée qui nous ont hébergés pendant tout le déroulement de la conférence.

          Les organisateurs de la conférence remercient les membres du comité scientifique et du comité de lecture, les auteurs des différentes contributions ainsi que tous ceux qui ont contribué au bon déroulement de ces journées.


          {\it This proceedings book contains the contributions that were presented at the second french conference on Computational Neuroscience that was held in Marseille from October 8th to 11th, 2008.

          Computational neuroscience is the study of the mechanisms governing the processing of information in the nervous system, from the cellular level to the population of neurons and behaviour control. The aim of this conference was to gather people from various fields, including neuroscience, information science, statistical physics or robotics, in order to give a large panorama of the ongoing research in the field.

          This book presents the 68 contributions which have been presented at the conference, with respect to their order of appearance in the conference program. The first day was devoted to the modelling of neural cells, to visual and cortical treatments and realistic neural networks models. The second day was devoted to brain-machine interfaces, large-scale and dynamical models, functional plasticity and neural interfaces.

          This conference has been made possible with financial support from the CNRS, the French Society of Neuroscience,  the regional council of Provence and of Bouches-du-Rhône, the city of Marseille, the university of Provence, the IFR "Sciences du Cerveau et de la Cognition" and the INRIA. It was kindly hosted by the Marseille medicine faculty and the University of the Mediterranean. We are grateful to all these supporting organizations for helping us gathering the computational neuroscience community in Marseille.

          The organizers of this conference would like to thank the scientific committee members and reviewers, the authors of the submitted papers and all those who have helped with which we could provide you the best conditions possible.
          }

          \vfill
          \noindent Laurent Perrinet and Emmanuel Daucé\hfill October, 2008
          \newpage

   #. Table of Contents

      ::

          %%%%%%%%TOC%%%%%%%%%%%%%%%%%%
          \pagestyle{empty}
          \oddsidemargin=2cm
          \evensidemargin=2cm
          \tableofcontents
          \newpage

   #. Including the above generated
      `body.tex`
      file

      ::

          %%%%%%%%%%%%%%%%%%%%%%%%%%%%%
          %   MAINMATTER --  Section by Section
          \pagenumbering{arabic}
          \setcounter{page}{1}
          \oddsidemargin=-1cm
          \evensidemargin=5cm
          \input body %_static

   #. Finally, include both index:

      ::

          %%%%%%%%%%%%%%%   Author and Subject Index
          \oddsidemargin=2cm
          \evensidemargin=2cm
          \printindex{author}{Author Index}
          \printindex{keyword}{Keyword Index}

   #. And close the book:

      ::

          \thispagestyle{empty}
          %\includepdf[pages=-,pagecommand={\thispagestyle{empty}},addtotoc={1,section,1,{\bf Presentation of the INCF} by \emph{{\sc Chatzopoulou}, Elli},8}]{INCF_Neurocomp08.pdf}%
          \includepdf[pages=-,pagecommand={\thispagestyle{empty}}]{INCF_Neurocomp08.pdf}%
          \end{document}

#. A
   `Makefile`
   eased debugging and flow control:

   ::

       latexfile = neurocomp08proceedings

       default: $(latexfile).pdf

       pdf: $(latexfile).pdf

       body.tex: paper_Neurocomp2008.csv body.py
               python body.py

       %.eps: %.png
               convert $< $@

       %.eps: %.jpg
               convert $< $@

       affiche_NeuroComp.pdf: affiche_NeuroComp.svg PACA3-coul_N_.pdf SdN.png  LogoMarseille.png LogoCnrs.png
               inkscape affiche_NeuroComp.svg -A affiche_NeuroComp.pdf


       $(latexfile).pdf: $(latexfile).tex body.tex titlepage.tex ean13.tex affiche_NeuroComp.pdf
               pdflatex  $(latexfile)
               makeindex keyword.idx
               makeindex author.idx
               pdflatex $(latexfile)
               while ( grep -q '^LaTeX Warning: Label(s) may have changed' $(latexfile).log) \
                       do pdflatex $(latexfile); done
               while ( grep -q 'Rerun to get citations correct.' $(latexfile).log) \
                       do pdflatex $(latexfile); done


       clean:
               rm -f $(latexfile).out  $(latexfile).pdf $(latexfile).log titlepage.aux \
                       $(latexfile).aux $(latexfile).toc  body.tex keyword.ilg author.ilg \
                       $(latexfile).ind author.idx keyword.idx author.ind keyword.ind

#. and voilà!
