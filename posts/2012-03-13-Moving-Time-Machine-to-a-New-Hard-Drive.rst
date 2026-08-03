.. title: Moving Time Machine to a New Hard Drive
.. slug: 2012-03-13-Moving-Time-Machine-to-a-New-Hard-Drive
.. date: 2012-03-13 13:36:57
.. type: text
.. tags: macos, sciblog


-  There exist some solution to move a time machine data folder to a new
   drive by making a clone of the drive. My problem is that I already
   have data on the new drive and that this data can difficultly be
   moved.



.. TEASER_END
.. warning::

  This post is certainly obsolete...




-  It try (after switching off Time machine of course) with ``rsync``
   while keeping hard links:

   ::

       sudo rsync -av -H  /Volumes/tera_enigma/Backups.backupdb /Volumes/2T_un/

-  This takes a while as rsync has to manage a lot of them (may take
   also a lot of memory, so be patient)
