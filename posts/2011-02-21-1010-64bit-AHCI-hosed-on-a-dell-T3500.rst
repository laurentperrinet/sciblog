.. title: Ubuntu 10.10 64bit AHCI hosted on a dell T3500
.. slug: 2011-02-21-1010-64bit-AHCI-hosed-on-a-dell-T3500
.. date: 2011-02-21 13:36:57
.. type: text
.. tags: sciblog, ubuntu


.. warning::

  This post is certainly obsolete...



-  quoting
   `http://ubuntuforums.org/showpost.php?p=10189331&postcount=35 <http://ubuntuforums.org/showpost.php?p=10189331&postcount=35>`__
   : "For those (like me) who aren't familiar with grub tampering,
   here's what I did to make the change automatic:"


   .. TEASER_END


   ::

       sudo cp /boot/grub/grub.cfg /boot/grub/grub.cfg.orig
       sudo cp /etc/default/grub /etc/default/grub.orig
       sudo vi /etc/default/grub
       # < # GRUB_CMDLINE_LINUX=""
       # < GRUB_CMDLINE_LINUX="pci=nocrs"
       # ---
       # > GRUB_CMDLINE_LINUX=""
       sudo update-grub
