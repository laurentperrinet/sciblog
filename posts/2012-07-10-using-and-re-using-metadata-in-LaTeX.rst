.. title: using and re-using metadata in LaTeX
.. slug: 2012-07-10-using-and-re-using-metadata-in-LaTeX
.. date: 2012-07-10 13:36:57
.. type: text
.. tags: latex, sciblog


Introduire des metas / Include meta keywords
--------------------------------------------


.. TEASER_END


-  pour mieux référencer votre papier, introduisez des metas en ajoutant
   avant le ``\begin{document} `` la commande

   ::

       \hypersetup{%
         pdftitle={my title},%
         pdfsubject={short description},%
         pdfauthor={Laurent Perrinet <Laurent.Perrinet@univ-amu.fr.fr>, INT/CNRS, 31, ch. Joseph Aiguier, 13402 Marseille Cedex 20, France; https://invibe.net/LaurentPerrinet},%
         pdfkeywords={Neuronal representation, ....},%
       }

-  vous aurez besoin auparavant de charger le package ``hyperref``:

   ::

       \usepackage[pdftex, pdfusetitle ,colorlinks=false, pdfborder={0 0 0}]{hyperref}%

variables
---------

-  the basics is to use variables within LaTex
-  for instance, these may be useful to define a switch

   ::

       \let \mode=0
       \if 1\mode
        truc...truc...truc
       \else
       \fi

complete example
----------------

-  even better, we can use string variables

   ::

       \documentclass[11pt]{article}
       %-------definitions-----
       \newcommand{\Author}{Laurent Perrinet}
       \newcommand{\Address}{INT}
       \newcommand{\Website}{https://invibe.net/LaurentPerrinet}
       \newcommand{\Email}{Laurent.Perrinet@incm.cnrs-mrs.fr}
       \newcommand{\Title}{My title}
       \newcommand{\Keywords}{my first keyword, my first keyword, more keywords.}
       %--------------------------
       \usepackage{url}
       \usepackage[pdftex, pdfusetitle,colorlinks=false,pdfborder={0 0 0}]{hyperref}%
       \hypersetup{%
       pdftitle={\Title},%
       pdfauthor={\Author < \Email > \Address - \Website},%
       pdfkeywords={\Keywords},%
       }%
       \begin{document}
       \title{\Title}
       \author{\Author\thanks{\Address , e-mail: \Email , WWW: \Website }}
       \date{}
       \maketitle
       {\bf Keywords:} \Keywords %

       My text is here...

       \end{document}
