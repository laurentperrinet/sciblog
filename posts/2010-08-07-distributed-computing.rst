.. title: distributed computing
.. slug: 2010-08-07-distributed-computing
.. date: 2010-08-07 13:36:57
.. type: text
.. tags: sciblog


-  guess you have a bunch (4000) of embarrassingly parallel tasks (one
   hour each) and access to about 40 CPUs through SSH. All tasks would
   run easily on each node, and they all share some network drive (NFS).
   Would be nice to run everything from just one place (script,
   command-line, web interface, ...)

.. TEASER_END


a bunch of existing tools
-------------------------

-  `http://sourceforge.net/projects/mussh/ <http://sourceforge.net/projects/mussh/>`__
-  `http://code.google.com/p/csshx/ <http://code.google.com/p/csshx/>`__
-  `http://www.occam.com/sa/rshall.pdf <http://www.occam.com/sa/rshall.pdf>`__
-  `http://web.taranis.org/shmux/#related <http://web.taranis.org/shmux/#related>`__
-  `http://tentakel.biskalar.de/similar/ <http://tentakel.biskalar.de/similar/>`__
-  `http://guichaz.free.fr/gsh/ <http://guichaz.free.fr/gsh/>`__ (sse
   btw
   `http://guichaz.free.fr/pysize/ <http://guichaz.free.fr/pysize/>`__ )

what we can do
--------------
