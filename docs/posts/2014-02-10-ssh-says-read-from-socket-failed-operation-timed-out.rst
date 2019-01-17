.. title: SSH says 'Read from socket failed: Operation timed out'
.. slug: 2014-02-10-ssh-says-read-from-socket-failed-operation-timed-out
.. date: 2014/02/10 14:38:18
.. tags: ssh, int
.. link: 
.. description: I report here a strange bug we had in establishing a SSH connection.
.. type: text

While SSH is rock solid, we stumbled on a strange bug while trying to establish a connection:

    $ ssh myname@myserver.fr -vvv

    OpenSSH_6.2p2, OSSLShim 0.9.8r 8 Dec 2011

    (...)

    Read from socket failed: Operation timed out

Nothing worked. The usual check of keys, encodings, permissions gave nothing.

.. TEASER_END

The culprit could be the OS, the version of the OS or whatever magical spell. However, after investigating the issue it appears the issue was isolated for certain cases, in particular within some homemade LAN, but not for a laptop computer thatcame freshly unpacked with no homemade setting.

This rang a bell, and by checking network settign I remembered that I had set "jumbo frames", that is I increased the MTU of my network card (in the hardware tab from the network settings on MacOsX) from 1500 (standard) to 9000 (jumbo).

Going back to the default velues restored the capacity to connect. Many thanks to Jimmy for finding that one!
