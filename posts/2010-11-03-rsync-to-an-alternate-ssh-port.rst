.. title: rsync to an alternate ssh port
.. slug: 2010-11-03-rsync-to-an-alternate-ssh-port
.. date: 2010-11-03 13:36:57
.. type: text
.. tags: sciblog

-  Q: sometimes you try to copy files using rsync but the server uses an
   alternate port than the usual 22...
-  A: `` rsync -av -e 'ssh -p 2222' HOST:~/folder/* dest ``
