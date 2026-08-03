.. title: inkscape native
.. slug: 2009-11-26-inkscape-native
.. date: 2009-11-26 13:36:57
.. type: text
.. tags: macos, sciblog


-  trying out
   `http://wiki.inkscape.org/wiki/index.php/CompilingMacOsX#Building\_Aqua\_November\_2009 <http://wiki.inkscape.org/wiki/index.php/CompilingMacOsX#Building_Aqua_November_2009>`__

.. TEASER_END
.. warning::

  This post is certainly obsolete...

-  build dependencies

   ::

       sudo port install autoconf automake

       sudo port install librsvg libwpd libwpg libcroco

       sudo port install libxslt boost boehmgc gtkmm lcms intltool popt

       sudo port install cairo +quartz+no_x11 cairomm pango +quartz+no_x11 poppler +quartz gtk2 +quartz

       sudo port install gsl

       sudo port install hicolor-icon-theme

       sudo port install subversion

       sudo port install libxml2 libxslt

       # optional to speed up the compiling process:
       sudo port install ccache
       export CC="ccache gcc"
       export CXX="ccache g++"

-  getting the sources

   ::

       cd tmp
       svn co https://inkscape.svn.sourceforge.net/svnroot/inkscape/inkscape/trunk inkscape
       cd inkscape/packaging/macosx/

-  compile

   ::

       # Edit the file osx-build.sh to remove the configure option --enable-osxapp
       # (line 24)

       # I used TextWrangler for this, pico or another command line editor will do the same.

       # Back to the terminal:

       # configure it:
       sudo ./osx-build.sh c

       # build it:
       sudo ./osx-build.sh b

       # install it:
       sudo ./osx-build.sh i

       # test it:
       ../../Build/bin/inkscape

   compiles ok :-), but crashes rather rapidly :-(
