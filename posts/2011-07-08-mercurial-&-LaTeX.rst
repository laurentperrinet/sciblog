.. title: mercurial & LaTeX
.. slug: 2011-07-08-mercurial-&-LaTeX
.. date: 2011-07-08 13:36:57
.. type: text
.. tags: latex, sciblog



.. TEASER_END
.. warning::

  This post is certainly obsolete...



#. Just a add the following lines to your Makefile

   ::

       HGID:=$(shell hg parents -R .. --template "Mercurial revision {rev} - date: {date|isodate}")
       hgid.tex:dummy
               [ -f $@ ] || touch $@
               echo '\\renewcommand{\hgid}{$(HGID)}' > $@
       dummy: ;

#. and this lines to your main tex file

   ::

       \newcommand{\hgid}{null}
       \input{hgid}

   now one can use the command ``\hgid`` to get the version everywhere.

#. for instance

   ::

       \newcommand{\HRule}{\rule{\linewidth}{0.5mm}}
       \usepackage{fancyhdr}
       \pagestyle{fancyplain}
       \fancyhead{}
       \chead{{\sc This a DRAFT, please do not distribute.}}
       \cfoot{\HRule \\ \hgid}
