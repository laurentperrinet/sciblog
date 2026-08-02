.. title: discover ports on MacOSX
.. slug: 2012-09-30-discover-ports-on-MacOSX
.. date: 2012-09-30 13:36:57
.. type: text
.. tags: macos, sciblog


-  the network utility GUI is useful, but you may get the same results
   via the command line:



.. TEASER_END
.. warning::

  This post is certainly obsolete...



::

    $ cd /Applications/Utilities/Network\ Utility.app/Contents/Resources/
    $ ./stroke nas-meduz.local 548 550
    Port Scanning host: 192.168.0.5

             Open TCP Port:         548             afpovertcp
    $ ./stroke shazam.dyndns.org 548 550
    Port Scanning host: 82.231.23.196

             Open TCP Port:         548             afpovertcp
