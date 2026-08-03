.. title: how to find stuff
.. slug: 2010-12-27-how-to-find-stuff
.. date: 2010-12-27 13:36:57
.. type: text
.. tags: info, sciblog


-  the most simple command is ``locate`` :

   ::

       locate Python.h

   ; it is based on a database updated regulalry (most often daily).


.. TEASER_END


-  the most powerful is ``find`` :

   ::

       # To find all files modified in ~/Sites three days ago:
       find ~/Sites -mtime 3
       # and 10 minutes ago:
       find ~/Sites -mmin 10
       #A time specified by -n means less than, while +n means more than.

       #To find all files in you home directory modified within the last week use:
       find ~ -mtime -7
       find ~ -newer last-backup.log

       # will find all files changed (or created) since last-backup.log was files larger than 2 megabytes (4000 of these 512 byte blocks):
       find ~ -size +4000
       find empty files% find . -empty
