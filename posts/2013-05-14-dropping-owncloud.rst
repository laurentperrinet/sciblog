.. title: dropping owncloud
.. slug: 2013-05-14-dropping-owncloud
.. date: 2013-05-14 13:36:57
.. type: text
.. tags: sciblog


-  since about 6 months, I was using `ownCloud <http://owncloud.org>`__
   as a remplacement of dropbox, but I had unfortunately lots of
   problems and finally decided to drop wasting time on maintaining it.

.. TEASER_END

.. warning::


  This post is obsolete - things have improved greatly since that period!

-  it is certainly a useful service, but there are certainly simpler
   things to use to sync files accross computers and implement "your own
   cloud". here, I give some reasons for my choice and hope they may be
   useful for further developpment of owncloud or any other alternative
   to dropbox:

   -  first of all, you need an efficient file syncing. it is
      dangerously buggy in owncloud:

      #. generates zillions of conflict files, takes ages to sync a
         folder with lots of files.
      #. the client happened to delete some files with no warning
      #. gives little feedback on how things are processed (the info
         dialog in client 1.2.5 is not functional). it took me a while
         to find a way to get some logfile (by calling the client with
         the ``--logfile`` argument) - but it is not documented
         elsewhere. the icons and error codes are not always
         informative.
      #. does not compile on snow leopard / 32-bit.

   -  the server is simple to install but is too shiny over-the-top
      compared to its raw functionality.

      #. the upgrade process was rarely smooth due to "maintenance
         problems" related to the database (one day wasted for 5.0.4 >
         5.0.5). this hints me that there may be security issues that
         are unresolved.
      #. the media server / photo gallery is merely useless

   -  I *bought* the apps for iOS and android, and they are a joke

      #. you need to synchronize all your files, no choice is possible -
         thus it is just not useful and I could never access any file
         off-line
      #. uploading photos is buggy, videos are ignored

   -  the ecosystem:

      #. based on a set of developers (some part of a company) and a set
         of users complaining about bugs that get closed is not
         reassuring
      #. the motto "you have a dropbox problem" is not pushing issues
         forward. certainly when comparing to the quality of the dropbox
         service

-   everything I say here is with a QNAP server (and I am not a
   sysdamin), so it is certainly partly my fault.
