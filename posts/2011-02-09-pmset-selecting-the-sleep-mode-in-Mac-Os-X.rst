.. title: pmset: selecting the sleep mode in Mac Os X
.. slug: 2011-02-09-pmset-selecting-the-sleep-mode-in-Mac-Os-X
.. date: 2011-02-09 13:36:57
.. type: text
.. tags: sciblog, macos

.. warning::

  This post is certainly obsolete...



-  from
   `http://www.fscklog.com/2008/02/schnellschlaf-s.html <http://www.fscklog.com/2008/02/schnellschlaf-s.html>`__:

To select one of the different sleep modes of the Mac use the
command-line tool ``pmset``:


.. TEASER_END


-  To show the current settings:

   ::

       pmset -g

-  The hibernatemode can be 3 (default: safeSleep, i.e. the RAM content
   is also written to disk when the lid is closed), 0 (pure RAM sleep),
   1 (pure deep-sleep). Turn the safeSleep off:

   ::

       sudo pmset -a hibernatemode 0
