.. title: Installation TeX
.. slug: 2009-08-19-Installation-TeX
.. date: 2009-08-19 13:36:57
.. type: text
.. tags: latex

Some useful bits of ``\LaTeX`` code accumulated over the years...

.. TEASER_END

count number of words / compter le nombre de mots
-------------------------------------------------

-  Pour compter le nombre de mots et de caractères d'un document latex,
   il suffit d'installer deTeX et de lancer la simple ligne de commande

   ::

       detex MonFichier.tex | wc -w

-  alternatively, you may use

   ::

       pdftotext MonFichier.pdf - | wc -w

-  in TexShop there's a "Statistics..."
   interface to the same technique.
-  on MacOsX, to install appropriate tools, use MacPorts and

   ::

       sudo port install detex
       sudo port install xpdf +a4 +with_poppler

including source code in a document with pretty printing
--------------------------------------------------------

-  use

   ::

       \usepackage{attachfile}

   or

   ::

       \usepackage{filecontents}

-  see documentation:

   ::

       texdoc attachfile

referring to table or image
---------------------------

-  referring to table or image (and not to the bottom of it)

   ::

         \usepackage{hypcap}

framed box
----------

-  make a framed box around text (and configure space) :

   ::

       \setlength\fboxsep{1pt}
       \setlength\fboxrule{0.5pt}
       \fbox{text}

convert a collection of JPGs to a pdf
-------------------------------------

::

    \listfiles
    \documentclass{minimal}
    \usepackage{graphicx}
    \usepackage[active,graphics,tightpage]{preview}
    \begin{document}
    \includegraphics{pic1}
    \includegraphics{pic2}
    \includegraphics{pic3}
    \end{document}

-  or

::

    for f in *.jpg ; do convert $f `basename $f .jpg`.pdf ; done

-  or `` slideshow.tex`` TeX file

::

    ___________________________________________________________
    \pdfcatalog{/PageMode/FullScreen}\pdfcompresslevel=0
    \pdfhorigin0pt\pdfvorigin0pt
    \def\process#1 {\setbox0\hbox{\pdfximage width 20cm {#1}%
      \pdfrefximage\pdflastximage}%
      \pdfpagewidth=\wd0 \pdfpageheight=\ht0 \shipout\box0\par}
    \everypar{\setbox0\lastbox\process} \input dir \end
    ___________________________________________________________
    Usage:
    ls *.jpg > dir
    pdftex slideshow


more fonts
==========

-  on the mac, out of the box with i-installer

   ::

       The gwTeX part of this distribution contains all the setup files you need to use a couple of fonts from your Mac. The setup has been created by Thomas A. Schmitz (he did the main work) and Adam Lindsay, hence the naming: gtamacfonts.
       To use these fonts with LaTeX, put e.g. the following in your file:
               \usepackage[T1]{fontenc}
               \usepackage{gtamachoefler}
       Such a style file will make Hoefler Text the serif (roman) text font and Gill Sans the sans serif font. The following basic styles are available:
               gtamacbaskerville.sty
               gtamacdidot.sty
               gtamacgeorgia.sty
               gtamachoefler.sty
       There are  more. See the manual for details. For the same effect using ConTeXt, enter e.g.:
               \usetypescriptfile[type-gtamacfonts]
               \usetypescript[Hoefler][ec]
               \setupbodyfont[Hoefler,12pt]
       Example documents and a manual can be found in the texmf.gwtex/doc/fonts/gtamacfonts subdirectory. To get the manual you can type "texdoc gtamacfonts" in a Terminal window.

-  Latin Modern

   ::

       \usepackage[T1]{fontenc}
       \usepackage{lmodern}

Installation TeX
================

-  Sous Un\*x\_like, utilisation de TeTeX :
   `http://www.tug.org/teTeX/ <http://www.tug.org/teTeX/>`__
-  Pour ajouter un package, copiez le à un endroit adéquat (voir
   `http://www.ctan.org/installationadvice/ <http://www.ctan.org/installationadvice/>`__
   ), puis faire

   ::

       texhash

   -  pour rafraichir l'arborisation des packetages connus par le moteur
      tex

Tex on MacOsX
-------------

-  !\ `TexLive <http://www.tug.org/mactex>`__ is the most recent /easy
   distribution. You may add new packages easilly in
   ``$HOME/Library/texmf`` (see a
   `reference <http://www.tug.org/mactex/whatgetsinstalledwhere.html>`__)
   or using the `TexLive tool <http://tug.org/texlive/tlmgr.html>`__:
   ``tlmgr``
-  to install :

   ::

       wget http://ftp.klid.dk/ftp/texlive/tlnet/mactex-2009-sept-20.mpkg.zip
       unzip mactex-2009-sept-20.mpkg.zip
       sudo installer -pkg MacTeX-2009.mpkg -target /

   (check before on
   `http://ftp.klid.dk/ftp/texlive/tlnet/ <http://ftp.klid.dk/ftp/texlive/tlnet/>`__
   the correct name)

-  I had to set up a new source repository :

   ::

       sudo tlmgr option location http://ftp.klid.dk/ftp/texlive/tlnet

-  to upgrade

   ::

       sudo tlmgr update --self
       sudo tlmgr update --all
