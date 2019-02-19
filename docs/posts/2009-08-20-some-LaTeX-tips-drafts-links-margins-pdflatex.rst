.. title: some LaTeX tips: drafts, links, margins, pdflatex
.. slug: 2009-08-20-some-LaTeX-tips-drafts-links-margins-pdflatex
.. date: 2009-08-20 13:36:57
.. type: text
.. tags: latex

More ``\LaTeX`` tips...

.. TEASER_END

checking typographic style
--------------------------

-  Lint for LaTeX :
   `http://baruch.ev-en.org/proj/chktex/ <http://baruch.ev-en.org/proj/chktex/>`__

make links
----------

-  hyperref quick reference list :

   ::

       \href{URL}{text }
       \url{URL}
       \nolinkurl{URL}

managing margins
----------------

-  to adjust margins, use

   ::

       \usepackage[margin=2.5cm]{geometry}

   then play around with the ``2.5cm`` value until it fits.

-  tips for fitting your text in the required size : `LaTeX Tips n
   Tricks for Conference
   Paper <http://www-db.stanford.edu/~manku/latex.html>`__

citations
---------

-  If you give LaTeX \\cite{fred,joe,harry,min}, its default commands
   could give something like "[2,6,4,3]"; this looks awful. One can of
   course get the things in order by rearranging the keys in the \\cite
   command, but who wants to do that sort of thing for no more
   improvement than "[2,3,4,6]"

   -  The cite package sorts the numbers and detects consecutive
      sequences, so creating "[2-4,6]". The natbib package, with the
      numbers and sort&compress options, will do the same when working
      with its own numeric bibliography styles (plainnat.bst and
      unsrtnat.bst).
   -  If you might need to make hyperreferences to your citations, cite
      isn't adequate. If you add the hypernat package:

      ::

            \usepackage[...]{hyperref}
            \usepackage[numbers,sort&compress]{natbib}
            \usepackage{hypernat}
            ...
            \bibliographystyle{plainnat}

      See for example
      `http://www.tex.ac.uk/cgi-bin/texfaq2html?label=citesort <http://www.tex.ac.uk/cgi-bin/texfaq2html?label=citesort>`__

Useful draft tips
-----------------

-  “LaTeX and Subversion”

   -  set a keyword with ``svn propset svn:keywords "Id" index.tex `` so
      that every occurrence of
   -  use latex-svninfo
      `http://www.ctan.org/tex-archive/macros/latex/contrib/svninfo/ <http://www.ctan.org/tex-archive/macros/latex/contrib/svninfo/>`__
      for instance with

      ::

          \usepackage[fancyhdr,today,draft]{svninfo}%
          %\usepackage[fancyhdr]{svninfo}%
          \pagestyle{fancyplain}
          \fancyhead{}

   -  now at every commit $Id$ will be replaced by useful data that will
      show up in the foot of the page
   -  for a reference on using keywords see
      `http://wiki.loria.fr/wiki/Variables\_automatiques <http://wiki.loria.fr/wiki/Variables_automatiques>`__

using pdfLaTeX
--------------

-  |X-(| sites like arXiV use only plain LaTeX so that you should keep
   the 2 versions of your directives for better portability (see \\ifpdf
   ...)

   -  in particular arXiV rejects the ``microtype`` package

-  le package hyperref permet même de faire des références vers les
   différents chapitres.
-  PDfLaTeX ne permet pas d'inclure des eps pour cela il faut les
   convertir en pdf avec
   `epstopdf <http://www.ctan.org/tex-archive/support/epstopdf/>`__ ou
   le script suivant qui permet de convertir tous les .eps d'un dossier
   (à sauver et rendre executable):

   ::

       for f in $* ;do
           if echo "$f" | grep -i eps*   ; then
                epstopdf --nocompress $f
                echo "converting  $f to pdf ..."
           else
           echo "$f is not a eps file, ignored"
           fi
       done

   il suffit alors d'executer en console
   `` ./mon_script la-ou-ya-tout-mes-eps/*.eps ``



.. |X-(| image:: https://invibe.net/moin_static196/moniker/img/angry.png
