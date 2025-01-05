.. title: using grin
.. slug: 2010-04-07-using-grin
.. date: 2010-04-07 13:36:57
.. type: text
.. tags: sciblog


-  I just discovered `grin <http://pypi.python.org/pypi/grin>`__, "grep
   my way"

.. TEASER_END
.. warning::

  This post is certainly obsolete...

-  install:

   ::

       sudo easy_install grin

-  search recursively

   ::

       grin  expression

-  search recursively in a specific directory

   ::

       grin  expression /this/directory

-  search recursively python files

   ::

       grin -I "*.py"  expression
