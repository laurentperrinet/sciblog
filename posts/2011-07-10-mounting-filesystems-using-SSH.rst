.. title: mounting filesystems using SSH
.. slug: 2011-07-10-mounting-filesystems-using-SSH
.. date: 2011-07-10 13:36:57
.. type: text
.. tags: info, macos, sciblog

install on ubuntu
-----------------


.. TEASER_END


#. ::

       $ sudo apt-get install sshfs
       [sudo] password for toto:
       Reading package lists... Done
       Building dependency tree
       Reading state information... Done
       The following NEW packages will be installed
         sshfs
       0 upgraded, 1 newly installed, 0 to remove and 0 not upgraded.
       Need to get 43.7 kB of archives.
       After this operation, 160 kB of additional disk space will be used.
       Get:1 http://gb.archive.ubuntu.com/ubuntu/ natty/main sshfs amd64 2.2-1build1 [43.7 kB]
       Fetched 43.7 kB in 0s (1,477 kB/s)
       Selecting previously deselected package sshfs.
       (Reading database ... 342224 files and directories currently installed.)
       Unpacking sshfs (from .../sshfs_2.2-1build1_amd64.deb) ...
       Processing triggers for man-db ...
       Setting up sshfs (2.2-1build1) ...

#. ::

       $ sudo gpasswd -a $USER fuse
       Adding user toto to group fuse

install on macosx
-----------------

#. install
   `http://code.google.com/p/macfuse <http://code.google.com/p/macfuse>`__
#. follow
   `http://code.google.com/p/macfuse/wiki/MACFUSE\_FS\_SSHFS <http://code.google.com/p/macfuse/wiki/MACFUSE_FS_SSHFS>`__
#. on a 64 bits system, you have to install a proper version,
   follow
   `http://superuser.com/questions/75332/is-truecrypt-macfuse-supported-on-snow-leopard-with-64-bit-kernel <http://superuser.com/questions/75332/is-truecrypt-macfuse-supported-on-snow-leopard-with-64-bit-kernel>`__

using sshfs (mac and ubuntu)
----------------------------

#. Create a mountpoint and give yourself ownership

   ::

       sudo mkdir /media/mount-name
       sudo chown your-username /media/mount-name

#. Mount the filesystem

   ::

       sshfs remote-system-name:/remote-folder /media/mount-name

#. Unmount the filesystem

   ::

       fusermount -u /media/mount-name

automating the process sshfs (mac and ubuntu)
---------------------------------------------

#. script to ``mount_cluster.sh`` :

   ::

       mkdir ~/spawn
       sshfs toto@server:~/spawn ~/spawn

#. script to unmount ``umount_cluster.sh`` :

   ::

       fusermount -u  ~/spawn
       rmdir ~/spawn
