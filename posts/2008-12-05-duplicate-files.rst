.. title: duplicate files
.. slug: 2008-12-05-duplicate-files
.. date: 2008-12-05 13:36:57
.. type: text
.. tags: info, sciblog

You may find yourself overwhelmed by files and in the need to keep the
filesystem organized. If deleting is the best option, you may consider
these 2 options:

preferred: Hardlink
-------------------

From
`http://code.google.com/p/hardlinkpy/ <http://code.google.com/p/hardlinkpy/>`__
, "hardlink.py is a tool to hardlink together identical files in order
to save space.". Thus the filesystem is the same, but duplicate files
are checked so they are actually written *once* on the hard drive.

.. TEASER_END
.. warning::

  This post is certainly obsolete...


Dupinator
---------

Dupinator, tries to find duplicates and to report them in order to
clean-up the organization of your files.

changelog
~~~~~~~~~

-  dupinator 2 : version 2 :
   `http://www.shearersoftware.com/personal/weblog/2005/01/14/dupinator-ii <http://www.shearersoftware.com/personal/weblog/2005/01/14/dupinator-ii>`__
-  dupinator 1 : The latest version can be found at
   `http://svn.red-bean.com/bbum/trunk/hacques/dupinator.py <http://svn.red-bean.com/bbum/trunk/hacques/dupinator.py>`__.
   It is a one-off that solved a problem, not an attempt to write the
   world's best python script.
   `http://www.pycs.net/bbum/2004/12/29/ <http://www.pycs.net/bbum/2004/12/29/>`__

It works by:
~~~~~~~~~~~~

-  launched via command line by passing a set of directories to be
   scanned
-  traverses all directories and groups all files by size
-  scans all sets of files of one size and checksums (md5) the first
   1024 bytes
-  for all files that have the same checksum for the first 1024 bytes,
   checksums the whole file and collects together all real duplicates
-  deletes all duplicates of any one file, leaving the first encountered
   file as the one remaining copy
