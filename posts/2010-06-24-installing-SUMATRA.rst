.. title: installing SUMATRA
.. slug: 2010-06-24-installing-SUMATRA
.. date: 2010-06-24 13:36:57
.. type: text
.. tags: python, sciblog

installing SUMATRA
==================

-  notes from the
   `CodeJamNr4 from FACETS <https://laurentperrinet.github.io/grant/facets/>`__
-  this was using a fresh install of ETS 6.2


.. TEASER_END
.. warning::

  This post is certainly obsolete...


dependencies
------------

-  pysvn :

   -  had to uninstall stuff from MacPorts

      ::

          sudo port uninstall --follow-dependents subversion

   -  `get
      pysvn <http://pysvn.tigris.org/servlets/ProjectDocumentList?folderID=1762&expandFolder=1762&folderID=5842>`__

      -  make :

         ::

             cd Source
             python setup.py backport
             Create the Makefile using python setup.py configure
             make

   -  install

      ::

          sudo rsync -av pysvn /Library/Frameworks/Python.framework/Versions/6.2/lib/python2.6/site-packages/

      -  pysvn 1.7.1 worked for me

-  mercurial

   ::

       sudo easy_install mercurial

-  django

   ::

       sudo easy_install django django_tagging

with hg
-------

::

      525  svn export ../sci/dyva/Motion/particles hg_particles
      526  cd hg_particles/
      527  hg init
      528  hg add MotionParticles.py experiment_all.py
      529  hg commit
      530  hg commit -m 'test'
      531  echo $USER
      532  vim .hgrc
      533  vim ~/.hgrc
      534  hg commit -m 'my first HG commit'
      535  vim ~/.hgrc
      536  ipython
      537  ls
      538  smt init sumatraTest_hg
      539  smt info

with svn
--------

::

      501  cd sci/dyva/Motion/particles/
      502  smt init -h
      503  smt init sumatraTest
      504  smt info
     511  smt configure --simulator=python --main=experiment_all.py
      512  smt info
      513  smtweb &
      514  ls -a
      515  rm -fr .smt
      516  smt init sumatraTest
      517  smtweb &
      518  open experiment_all.py
      519  touch fake.param
      520  smt run
      521  smt run -s python -m experiment_dot.py fake.param
      522  smt info
      523  smt configure -h
      524  smt configure -c diff
      525  smt info
      526  smt run -s python -m experiment_dot.py fake.param
      529  smt run -s python -m experiment_dot.py fake.param
      534  rm mat/dot.npy
      535  python experiment_dot.py fake.param
      536  ls
      537  smt help configure
      538  smt configure -d ./figures/
      539  smt info
      540  smt configure -s python -m experiment_dot.py
      541  smt run fake.param
      542  rm mat/dot.npy
      543  smt run fake.param
      544  ls figures/
      545  rm figures/dot_*
      546  smt run fake.param
      547  smt info
      548  smt configure -d ./figures
      549  smt info
      550  rm figures/dot_*png
      551  smt configure -d ./figures
      552  smt run fake.param
      553  smt comment "apparently, it is worth NaN shekels."
      554  smt tag codejam
      558  rm figures/dot_*png
      559  rm mat/dot.npy
      560  smt run --reason="test effect of a bigger dot" fake.param dot_size=0.1
      561  ls
      562  ls -al .smt/
      563  less .smt/simulation_records
      564  sqlite3 .smt/simulation_records
