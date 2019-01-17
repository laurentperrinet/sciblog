.. title: How To Change Your Time Machine Backup Interval
.. slug: 2013-02-02-How-To-Change-Your-Time-Machine-Backup-Interval
.. date: 2013-02-02 13:36:57
.. type: text
.. tags: macos, sciblog


+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| tl;dr `` sudo /usr/libexec/PlistBuddy -c 'set  :LaunchEvents:com.apple.time:"Backup Interval":Interval 86400' /System/Library/LaunchDaemons/com.apple.backupd-auto.plist ``   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

-  summarizing the instructions in
   `http://maketecheasier.com/change-your-time-machine-backup-interval/2009/06/05 <http://maketecheasier.com/change-your-time-machine-backup-interval/2009/06/05>`__
   :



.. TEASER_END
.. warning::

  This post is certainly obsolete...



-  make a backup

   ::

       sudo cp /System/Library/LaunchDaemons/com.apple.backupd-auto.plist /System/Library/LaunchDaemons/com.apple.backupd-auto.plist.backup

method 1 : vim (or any editor)
------------------------------

-  open the file for edition

   ::

       sudo vim /System/Library/LaunchDaemons/com.apple.backupd-auto.plist

-  replace 36000 (one hour) by 86400 (one day), then quit:

   ::

       :%s/3600/86400/g
       :wq!

method 2 : plistbuddy
---------------------

-  you can make it in one line:

   ::

       sudo /usr/libexec/PlistBuddy -c 'set  :LaunchEvents:com.apple.time:"Backup Interval":Interval 86400' /System/Library/LaunchDaemons/com.apple.backupd-auto.plist

-  this method use the `PlistBuddy <http://invibe.net/LaurentPerrinet/PlistBuddy>`__
   method to read / write the file. this utility can be used
   interactively

   ::

       sudo /usr/libexec/PlistBuddy  /System/Library/LaunchDaemons/com.apple.backupd-auto.plist

-  but also directly:

   ::

       sudo /usr/libexec/PlistBuddy -c 'print  ' /System/Library/LaunchDaemons/com.apple.backupd-auto.plist
       sudo /usr/libexec/PlistBuddy -c 'print  :LaunchEvents:com.apple.time ' /System/Library/LaunchDaemons/com.apple.backupd-auto.plist
       sudo /usr/libexec/PlistBuddy -c 'print  :LaunchEvents:com.apple.time:"Backup Interval" ' /System/Library/LaunchDaemons/com.apple.backupd-auto.plist
       sudo /usr/libexec/PlistBuddy -c 'print  :LaunchEvents:com.apple.time:"Backup Interval":Interval ' /System/Library/LaunchDaemons/com.apple.backupd-auto.plist
       sudo /usr/libexec/PlistBuddy -c 'set  :LaunchEvents:com.apple.time:"Backup Interval":Interval 3600' /System/Library/LaunchDaemons/com.apple.backupd-auto.plist

finally
-------

-  reboot.
