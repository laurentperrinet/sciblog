.. title: setting graphics' path
.. slug: 2009-08-21-setting-graphics-path
.. date: 2009-08-21 13:36:57
.. type: text
.. tags: latex


-  instead of using

   ::

       \includegraphics[width=\textwidth]{folder2_relative/picture.png}%

.. TEASER_END


-  by including in the front matter (i.e. before ``\begin{document``}):

   ::

       \DeclareGraphicsExtensions{.png,.pdf}%
       \graphicspath{{../folder1_relative/},{folder2_relative/},{/home/myname/folder_absolute/figures/}}%

-  you may simply use

   ::

       \includegraphics[width=.49\textwidth]{picture}%


.. TEASER_END

-  one advantage is that you could use context dependent rules, for
   instance:

   ::

       \newif\ifpdf
          \ifx\pdfoutput\undefined \pdffalse
       \else \pdfoutput=1 \pdftrue \fi
       % portability between LaTeX and pdfLaTeX
       \ifpdf
       \usepackage[pdftex]{graphicx}
       \usepackage[pdftex, pdfusetitle ,colorlinks=false, pdfborder={0 0 0}]{hyperref}%
       \DeclareGraphicsExtensions{.png,.pdf}%
       \graphicspath{{figures_pdf/}}%
       \pdfoutput=1 % we are running pdflatex
       \pdfcompresslevel=9     % compression level for text and image;
       \pdftrue
       % we are using the traditional latex
       \else
       \usepackage{graphicx}%
       \usepackage[colorlinks=false]{hyperref}%
       \DeclareGraphicsExtensions{.eps}%
       \graphicspath{{figures_eps/}}%
       \fi
