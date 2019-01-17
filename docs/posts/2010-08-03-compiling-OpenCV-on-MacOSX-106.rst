.. title: compiling OpenCV on MacOSX 10.6
.. slug: 2010-08-03-compiling-OpenCV-on-MacOSX-106
.. date: 2010-08-03 13:36:57
.. type: text
.. tags: macos, sciblog


using macports
--------------

-  it works now with macports:

   ::

       sudo port install -u opencv +python26 +tbb

.. TEASER_END
.. warning::

 This post is certainly obsolete...

latest SVN
----------

-  compiling here along with MacTex...
-  from
   `http://opencv.willowgarage.com/wiki/Mac\_OS\_X\_OpenCV\_Port <http://opencv.willowgarage.com/wiki/Mac_OS_X_OpenCV_Port>`__

   ::

       svn co https://code.ros.org/svn/opencv/trunk/opencv
       cd opencv # the directory containing INSTALL, CMakeLists.txt etc.
       mkdir build
       cd build
       cmake -D CMAKE_OSX_ARCHITECTURES=x86_64 -D WITH_FFMPEG=ON -D BUILD_EXAMPLES=ON -D BUILD_LATEX_DOCS=ON -D PDFLATEX_COMPILER=/usr/texbin/pdflatex -D BUILD_NEW_PYTHON_SUPPORT=ON  -D PYTHON_LIBRARY=/opt/local/lib/libpython2.6.dylib -D PYTHON_INCLUDE_DIR=/opt/local/Library/Frameworks/Python.framework/Headers ..
       make -j4
       sudo make install

-  I had to rebuild some ports

   ::

       sudo port install ilmbase
       port provides /opt/local/lib/libIlmImf.dylib
       sudo port install openexr
       sudo port install libdc1394

   and recompile

-  then could run

   ::

       cd ../samples/python/
       python camera.py

using homebrew
--------------

-  another route is homebrew:
   `http://gist.github.com/519418 <http://gist.github.com/519418>`__ / :

   ::

       $ brew info opencv
       opencv 2.1.1-pre
       http://opencv.willowgarage.com/wiki/
       Depends on: cmake, pkg-config, libtiff, jasper, tbb
       /usr/local/Cellar/opencv/2.1.1-pre (96 files, 37M)

       The OpenCV Python module will not work until you edit your PYTHONPATH like so:
         export PYTHONPATH="/usr/local/lib/python2.6/site-packages/:$PYTHONPATH"

       To make this permanent, put it in your shell's profile (e.g. ~/.profile).

       http://github.com/mxcl/homebrew/commits/master/Library/Formula/opencv.rb
