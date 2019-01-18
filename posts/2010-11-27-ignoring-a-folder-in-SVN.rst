.. title: ignoring a folder in SVN
.. slug: 2010-11-27-ignoring-a-folder-in-SVN
.. date: 2010-11-27 13:36:57
.. type: text
.. tags: sciblog

-  simply issue

   ::

        svn propset svn:ignore '*' data/


.. TEASER_END


-  then, you may change behavior by editing this setting:

   ::

        svn propedit svn:ignore  data/

-  then commit, this will aplly to all updated working copies
