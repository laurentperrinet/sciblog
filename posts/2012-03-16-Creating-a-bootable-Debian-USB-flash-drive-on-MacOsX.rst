.. title: Creating a bootable Debian USB flash drive on MacOsX
.. slug: 2012-03-16-Creating-a-bootable-Debian-USB-flash-drive-on-MacOsX
.. date: 2012-03-16 13:36:57
.. type: text
.. tags: info, macos, sciblog


-  largely adapted from
   `https://help.ubuntu.com/community/Installation/FromUSBStick#From\_Mac\_OSX <https://help.ubuntu.com/community/Installation/FromUSBStick#From_Mac_OSX>`__



.. TEASER_END
.. warning::

  This post is certainly obsolete...




-  download the iso

   ::

       wget http://napoleon.acc.umu.se/debian-cd/6.0.4/i386/iso-cd/debian-6.0.4-i386-CD-1.iso # or http://debian.ens-cachan.fr/ftp/debian-cd/6.0.4/i386/iso-cd/debian-6.0.4-i386-xfce+lxde-CD-1.iso
       hdiutil convert -format UDRW -o target.img debian-6.0.4-i386-CD-1.iso
       mv target.img.dmg target.img

-  identify where is your USB stick

   ::

       diskutil list

-  unmount the USB stick

   ::

       diskutil unmountDisk /dev/disk2

-  write on the stick

   ::

       mv target.img.dmg target.img
       sudo dd if=target.img of=/dev/rdisk2 bs=1m

- eject the USB stick

   ::

    diskutil eject /dev/disk2
