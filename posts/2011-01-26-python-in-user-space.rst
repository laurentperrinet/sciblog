.. title: python in user space
.. slug: 2011-01-26-python-in-user-space
.. date: 2011-01-26 13:36:57
.. type: text
.. tags: sciblog

-  with a setup.py package,
   `http://docs.python.org/install/index.html <http://docs.python.org/install/index.html>`__

   ::

       python setup.py install --home=$HOME/Python2.6


.. TEASER_END
.. warning::

  This post is certainly obsolete...




-  not bad... can't we do something better? Trying to setup distutils
   according to
   `http://docs.python.org/install/index.html <http://docs.python.org/install/index.html>`__
   , I was ending up with nasty errors (like "error: install-base or
   install-platbase supplied, but installation scheme is incomplete"),
   stumbled on
   `http://pwang.wordpress.com/2010/09/20/contortions-and-eventual-success-with-pydistutils-cfg/ <http://pwang.wordpress.com/2010/09/20/contortions-and-eventual-success-with-pydistutils-cfg/>`__
   and
   `http://stackoverflow.com/questions/3560865/problems-defining-install-platlib-in-pydistutils-cfg <http://stackoverflow.com/questions/3560865/problems-defining-install-platlib-in-pydistutils-cfg>`__
   to finally end up doing:

   #. ``vim ~/.pydistutils.cfg ``
   #. put

      ::

          [install]
          install-base=$HOME/python
          install-purelib=$base/site-packages
          install-platlib=$base/plat-mac
          install-headers=$base/Include
          install-scripts=$base/bin
          install-data=$base/data

   #. add ``$HOME/python/site-packages/`` to your PYTHONPATH and
      ``$HOME/python/bin/`` to your PATH in your ``.profile``
      environment
   #. you may have to refresh your ``ENV`` and create the appropriate
      directories:

      ::

          source .bashrc
          mkdir  ~/python
          mkdir  ~/python/site-packages/

   #. now simply issue

      ::

          python setup.py install

   #. or even

      ::

          pip install progressbar

   #. if you do not have pip, try first:

      ::

          easy_install pip
