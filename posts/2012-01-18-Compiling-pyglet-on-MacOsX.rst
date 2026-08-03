.. title: Compiling pyglet on MacOsX
.. slug: 2012-01-18-Compiling-pyglet-on-MacOsX
.. date: 2012-01-18 13:36:57
.. type: text
.. tags: macos, sciblog


-  you may get errors if trying to install pyglet using the traditional
   way, using ``pip`` for instance (was my case on MacOs X Lion 10.7.0 +
   python 64bits from EPD or homebrew). in cause is the carbon code that
   has been abandonned in the 64bits libraries that come with the OS


.. TEASER_END
.. warning::

  This post is certainly obsolete...


-  the solution comes from the
   `https://code.google.com/p/cocoa-python/ <https://code.google.com/p/cocoa-python/>`__
   package

   #. clone the package
      ``hg clone https://code.google.com/p/cocoa-python ``
   #. insert the code in your PYTHONPATH:
      ``rsync -av cocoapy /usr/local/lib/python2.7/site-packages/pyglet/libs/darwin``

-  a simpler solution is to install the pyglet code from
   `https://code.google.com/r/evilphillip-cocoa-ctypes2/ <https://code.google.com/r/evilphillip-cocoa-ctypes2/>`__
   :

   #. ``hg clone https://code.google.com/r/evilphillip-cocoa-ctypes2/``
   #. ``cd evilphillip-cocoa-ctypes2/``
   #. ``python setup.py install``

-  works!
