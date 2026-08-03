.. title: installing python and its components
.. slug: 2010-10-27-installing-python-and-its-components
.. date: 2010-10-27 13:36:57
.. type: text
.. tags: macos, sciblog


-  Python is often pre-installed on your system or easy to download.
   More difficult is to get the essential packages (numpy, scipy,
   matplotlib, ipython) and their dependencies installed. Here, I list
   some of the possibilities.



.. TEASER_END

on MacOsX: using MacPorts
-------------------------

-  A basic installation procedure is to use the `enthought
   distribution <http://www.enthought.com/products/edudownload.php>`__,
-  Another route is to use `MacPorts <http://www.macports.org>`__. It is
   a generic package manager inspired by what you get using Debian's
   ``apt`` scheme.
-  Once `install <http://www.macports.org/install.php>`__\ ed, do on the
   command-line

   -  on Leopard:

      ::

          sudo port install py25-pil py25-numpy py25-scipy py25-ipython py25-matplotlib +cairo+latex+tkinter
          sudo python_select python25

      (Note: you may also use ``python26`` on Leopard).

   -  on Snow Leopard:

      ::

          sudo port install py26-numpy py26-scipy py26-ipython py26-matplotlib
          sudo port install py26-pyobjc2-cocoa py26-pil py26-distribute py26-pip py26-py2app python_select
          sudo port install vtk5 +carbon +qt4_mac +python26 py26-mayavi

          sudo python_select python26

      to install a bunch of useful python packages.

   -  to get a package that is not available through macports, do:

      ::

          sudo easy_install progressbar

-  for `visionEgg <http://www.visionegg.org>`__ :

   ::

       sudo port install py26-opengl py26-game
       sudo easy_install visionegg

-  `http://ipython.scipy.org/moin/Py4Science/InstallationOSX <http://ipython.scipy.org/moin/Py4Science/InstallationOSX>`__
-  on Snow Leopard, you'll have to follow `these
   instructions <http://blog.hyperjeff.net/?p=160>`__.

Windows
-------

-  `http://www.pythonxy.com <http://www.pythonxy.com>`__

Debian / Ubuntu
---------------

-  see `http://neuro.debian.net/ <http://neuro.debian.net/>`__

   ::

       sudo aptitude install ipython python-numpy python-scipy python-matplotlib

DistUtils, PIP & Easy Install
-----------------------------

-  most of the time, there's a ``setup.py`` file:

   ::

       python setup.py install --prefix=~

-  See
   `http://peak.telecommunity.com/DevCenter/EasyInstall <http://peak.telecommunity.com/DevCenter/EasyInstall>`__
-  to install ``numpy`` (same for ``pylab``, ``scipy``, or
   ``visionegg``), simply do

   ::

       easy_install numpy

-  most of the cases, on a test server or a single-user machine, you may
   find more useful to install in your home dirtectory, for instance:

   ::

       easy_install -d ~/lib/python2.5/site-packages/ numpy

-  to upgrade, use

   ::

       easy_install -U numpy

-  you can `browse <http://pypi.python.org/pypi?%3Aaction=browse>`__ the
   list of available packages.
-  for pip: `http://pip.openplans.org/ <http://pip.openplans.org/>`__
-  you may create a script tu update all packages:

   ::

       for i in `python -c "for dist in __import__('pkg_resources').working_set: print dist.project_name"`:
       do
       echo "`easy_install -U $i`"
       echo "++++++++++++++++++++++++++++++++++++++++++++++++++"
       done

-  to install PIL, use

   ::

       easy_install -d lib/python2.6/site-packages/ --find-links http://www.pythonware.com/products/pil/ Imaging

SVNs: bleeding edge versions
----------------------------

-  numpy

   ::

       svn co http://svn.scipy.org/svn/numpy/trunk numpy
       cd numpy
       python setup.py build
       sudo python setup.py install
       rm -rf build
       cd ..

-  SciPy

   ::

       svn co http://svn.scipy.org/svn/scipy/trunk scipy
       cd scipy
       python setup.py build
       sudo python setup.py install
       rm -rf build
       cd ..

   -  see `scipy <http://www.scipy.org/Installing_SciPy/Mac_OS_X>`__
      `http://www.scipy.org/Installing\_SciPy/Mac\_OS\_X <http://www.scipy.org/Installing_SciPy/Mac_OS_X>`__

-  pylab

   ::

       svn co https://svn.sourceforge.net/svnroot/matplotlib/trunk/matplotlib matplotlib
       cd matplotlib
       python setup.py build
       sudo python setup.py install
       sudo rm -rf build
       cd ..

-  `SPE <http://pythonide.blogspot.com/2007/02/how-to-download-latest-spe-from_26.html>`__

   ::

       svn checkout svn://svn.berlios.de/python/spe/trunk/_spe

-  PIL

   ::

           wget http://effbot.org/downloads/Imaging-1.1.6.tar.gz
           tar zxvf  Imaging-1.1.6.tar.gz
           cd Imaging-1.1.6
           python setup.py build_ext -i
           python selftest.py
           python setup.py install

-  gsl

   ::

           cvs -d :pserver:anoncvs@sources.redhat.com:/cvs/gsl login
           cvs -d :pserver:anoncvs@sources.redhat.com:/cvs/gsl checkout gsl
           cd gsl/
           ./autogen.sh
           ./configure --enable-maintainer-mode
           make

-  pytables

   -  dependency on HDF

      ::

          wget ftp://ftp.hdfgroup.org/HDF5/current/src/hdf5-1.6.5.tar.gz
          tar zxvf hdf5-1.6.5.tar.gz
          cd hdf5-1.6.5
          ./configure --enable-cxx
          make
          make install
          h5ls -r  Documents/Sci/projets/virtualV1/experiments/benchmark_one/results/benchmark_retina_high.h5

      -  and `Py
         Rex <http://www.cosc.canterbury.ac.nz/greg.ewing/python/Pyrex/Pyrex-0.9.5.1a.tar.gz>`__

      ::

          wget http://www.cosc.canterbury.ac.nz/greg.ewing/python/Pyrex/Pyrex-0.9.5.1a.tar.gz
          tar zxvf Pyrex-0.9.5.1a.tar.gz
          cd Pyrex-0.9.5.1a
          python setup.py build
          sudo python setup.py install
          rm -rf build

   -  install

      ::

          wget http://puzzle.dl.sourceforge.net/sourceforge/pytables/pytables-1.4.tar.gz
          #svn co http://pytables.org/svn/pytables/trunk/ pytables
          tar zxvf pytables-1.4.tar.gz
          cd pytables-1.4
          export DYLD_LIBRARY_PATH=/sw/lib # or in .bashrc
          python setup.py install --hdf5=/sw
          cd ..

-  pygtk

   ::

       wget http://ftp.gnome.org/pub/GNOME/sources/pygtk/2.8/pygtk-2.8.6.tar.bz2
       tar xvfj pygtk-2.8.6.tar.bz2
       cd pygtk-2.8.6
       .configure
       make
       sudo make install    # or without sudo as root
       cd ..
