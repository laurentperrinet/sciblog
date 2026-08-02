.. title: managing packages on MacOsX : testing HomeBrew
.. slug: 2010-08-31-managing-packages-on-MacOsX-testing-HomeBrew
.. date: 2010-08-31 13:36:57
.. type: text
.. tags: macos, sciblog


-  a newcomer after fink and MacPorts:
   `http://wiki.github.com/mxcl/homebrew/ <http://wiki.github.com/mxcl/homebrew/>`__
-  advertised
   `here <http://www.engineyard.com/blog/2010/homebrew-os-xs-missing-package-manager/>`__



.. TEASER_END

-  install

   ::

        $ ruby -e "$(curl -fsS http://gist.github.com/raw/323731/install_homebrew.rb)"
       ==> This script will install:
       /usr/local/bin/brew
       /usr/local/Library/Formula/...
       /usr/local/Library/Homebrew/...

       Press enter to continue
       ==> Downloading and Installing Homebrew...
       ==> Installation successful!

-  fix permissions

   ::

        $ sudo chown -R `whoami` /usr/local

-  to install python specific stuff, use ``pip``:

   ::

       brew install pip
       echo '[install]
       install-scripts=/usr/local/Cellar/PyPi/2.6/bin
       install-data=/usr/local/Cellar/PyPi/2.6/share' > ~/.pydistutils.cfg
       pip install ipython

-  this is with the exception of numpy + scipy, the latter needing

   ::

       cd tmp
       svn co http://svn.scipy.org/svn/numpy/trunk numpy
       pip install numpy

       brew install suite-sparse
       svn co http://svn.scipy.org/svn/scipy/trunk scipy
       pip install scipy
