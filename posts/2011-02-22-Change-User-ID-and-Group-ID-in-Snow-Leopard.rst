.. title: Change User ID and Group ID in Snow Leopard
.. slug: 2011-02-22-Change-User-ID-and-Group-ID-in-Snow-Leopard
.. date: 2011-02-22 13:36:57
.. type: text
.. tags: macos, sciblog


-  find source and traget UID / GID using the ``id`` command on unix and
   ``dscl localhost read /Local/Default/Users/lup`` in MacOsX


.. TEASER_END
.. warning::

  This post is certainly obsolete...



-  from
   `http://macosx.com/tech-support/change-user-idgroup-id-in-leopard/336380.html <http://macosx.com/tech-support/change-user-idgroup-id-in-leopard/336380.html>`__
   :

   ::

       dscl . -change $HOME UniqueID 41167 545
       dscl . -change $HOME PrimaryGroupID 41167 1007
       chown -R 545:1007 $HOME

-  Remember to run the chown command afterwards, or you will not be able
   to access your home directory. Finally, log out and log in.
-  you may have to propagate changes on other drives (backup disks and
   such)
