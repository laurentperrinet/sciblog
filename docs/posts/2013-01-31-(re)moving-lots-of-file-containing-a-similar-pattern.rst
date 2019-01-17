.. title: (re)moving lots of file containing a similar pattern
.. slug: 2013-01-31-(re)moving-lots-of-file-containing-a-similar-pattern
.. date: 2013-01-31 13:36:57
.. type: text
.. tags: sciblog


-  I use `ownCloud <http://owncloud.org>`__ as a remplacement of
   dropbox, but I had unfortunately lots of conflicts files (on client
   and server)
-  these contain the ``_conflict-`` pattern, so a solution is to move
   all of them to a backup folder:

   ::

       cd /share/DriveOne/Web/owncloud/data/admin/files
       find . -name *_conflict-* -exec mv {} /share/Backups/backups/duplicate-photos/ \;
