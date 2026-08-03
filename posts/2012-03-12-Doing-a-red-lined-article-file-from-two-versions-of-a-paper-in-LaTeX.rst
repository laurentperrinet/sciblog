.. title: Doing a red-lined article file from two versions of a paper in LaTeX
.. slug: 2012-03-12-Doing-a-red-lined-article-file-from-two-versions-of-a-paper-in-LaTeX
.. date: 2012-03-12 13:36:57
.. type: text
.. tags: latex, sciblog


-  The editor of our submitted paper asked for a red-lined article file.
   Using ``latexdiff`` makes this task very easy: Simply grab the 2
   versions of your manuscript and issue


   .. TEASER_END


   ::

       latexdiff manuscript_v1.tex manuscript_v2.tex   > diff.tex
       latexmk -pdf diff.tex

   . The ``latexmk`` program allows to get all necessary passes to get a
   clean output file.

-  One issue is that one version imported a few other source files using
   the ``\input`` command, so we used the following parameter:

   ::

       latexdiff --flatten manuscript_v1.tex manuscript_v2.tex   > diff.tex
       latexmk -pdf diff.tex

-  it is recommended that instead of using bibtex, you copy and paste
   the content of the ``.bbl`` file.
-  Moral: one advantage of LaTeX is that your data, your dear prose, is
   in text (not binary) format and has an open syntax. This process
   allows the creation of the red-lined article file in one shot with no
   fiddling and lost time of copy and pasting. So whatever soft you use
   to put your ideas in readable digital format, just use something
   simple, structured and open.
