.. title: bundling using py2app
.. slug: 2010-09-27-bundling-using-py2app
.. date: 2010-09-27 13:36:57
.. type: text
.. tags: macos, sciblog

.. TEASER_END
.. warning::

  This post is certainly obsolete...

using macports
--------------

-  install py2app :

   ::

       sudo port install -u  py26-py2app




-  there's sometimes a problem in py2app to check the right architecture
   to build on:

   ::

       find /opt/local -name apptemplate/setup.py
       sudo vim /opt/local/Library/Frameworks/Python.framework/Versions/2.6/lib/python2.6/site-packages/py2app/apptemplate/setup.py

-  in this case, this can be done by adding the following lines to
   py2app/apptemplate/setup.py:

   ::

       gPreBuildVariants = [
           ...
           {
               'name': 'main-x86_64',
               'target': '10.6',
               'cflags': '-isysroot /Developer/SDKs/MacOSX10.6.sdk -arch x86_64',
               'cc': 'gcc-4.2',
           },
           {
               'name': 'main-i386',
               'target': '10.6',
               'cflags': '-isysroot / -arch i386',
               'cc': 'gcc-4.2',
           },
           ...
       ]

   . So, change to

   ::

       gPreBuildVariants = [
           {
               'name': 'main-x86_64',
               'target': '10.5',
               'cflags': '-isysroot /Developer/SDKs/MacOSX10.5.sdk -arch x86_64',
               'cc': 'gcc-4.2',
            },
       #     {
       #         'name': 'main-universal',
       #         'target': '10.5',
       #         'cflags': '-isysroot /Developer/SDKs/MacOSX10.5.sdk -arch i386 -arch ppc -arch ppc64 -arch x86_64',
       #         'cc': 'gcc-4.2',
       #     },
       #     {
       #         'name': 'main-fat3',
       #         'target': '10.5',
       #         'cflags': '-isysroot / -arch i386 -arch ppc -arch x86_64',
       #         'cc': 'gcc-4.2',
       #     },
       #     {
       #         'name': 'main-intel',
       #         'target': '10.5',
       #         'cflags': '-isysroot / -arch i386 -arch x86_64',
       #         'cc': 'gcc-4.2',
       #     },
       #     {
       #         'name': 'main-fat',
       #         'target': '10.3',
       #         'cflags': '-isysroot /Developer/SDKs/MacOSX10.4u.sdk -arch i386 -arch ppc',
       #         'cc': 'gcc-4.0',
       #     },
       ]

using homebrew
--------------

-  another route is homebrew:
   `http://gist.github.com/519418 <http://gist.github.com/519418>`__ /
