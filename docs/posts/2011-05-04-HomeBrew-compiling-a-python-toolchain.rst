.. title: HomeBrew: compiling a python toolchain
.. slug: 2011-05-04-HomeBrew-compiling-a-python-toolchain
.. date: 2011-05-04 13:36:57
.. type: text
.. tags: sciblog

.. TEASER_END
.. warning::

  This post is certainly obsolete...


::

    # install python through HomeBrew as a framework
    brew install python --framework
    mkdir ~/Frameworks
    ln -s "/usr/local/Cellar/python/2.7.2/Frameworks/Python.framework" ~/Frameworks





    # bootstrap pip
    /usr/local/share/python/easy_install pip
    /usr/local/share/python/pip install --upgrade distribute

    # libraries
    brew install gfortran
    pip install -U ipython

    # useful packages
    pip install -U nose
    pip install -U progressbar
    easy_install pyreport
    easy_install -f http://dist.plone.org/thirdparty/ -U PIL==1.1.7
    pip install -U mercurial

    # numpy et al
    pip install -U numpy
    pip install -U scipy
    pip install -U -e git+git@github.com:matplotlib/matplotlib.git#egg=matplotlib
    # pip install -f http://downloads.sourceforge.net/project/matplotlib/matplotlib/matplotlib-1.0/matplotlib-1.0.0.tar.gz matplotlib

    # IDE
    pip install -U sphinx pyflakes rope
    brew install sip
    brew install pyqt
    pip install -U spyder

    # mayavi
    brew install vtk --python
    pip install -U traitsbackendqt
    pip install -U configobj
    pip install  -U "Mayavi[app]"
