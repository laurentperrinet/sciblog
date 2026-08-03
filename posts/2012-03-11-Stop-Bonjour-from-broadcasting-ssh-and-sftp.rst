.. title: Stop Bonjour from broadcasting ssh and sftp
.. slug: 2012-03-11-Stop-Bonjour-from-broadcasting-ssh-and-sftp
.. date: 2012-03-11 13:36:57
.. type: text
.. tags: int, macos, sciblog


+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| largely a copy-and-paste from `http://hints.macworld.com/article.php?story=20070622210507844 <http://hints.macworld.com/article.php?story=20070622210507844>`__ ; Jun 25, '07 07:30:00AM • Contributed by: delight1   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

-  After doing a backup, edit the following file:

   ::

       sudo vim /System/Library/LaunchDaemons/ssh.plist


.. TEASER_END
.. warning::

  This post is certainly obsolete...



-  In the editor, the goal is to delete these two lines:

   ::

       <string>ssh</string>
       <string>sftp-ssh</string>

-  They should be found around lines 22 and 23. In ``vim``, this is
   easily done by typing ``\ssh``, then ``n`` until you are on the right
   line. Then type ``d2d`` to delete these 2 line. Finally issue ``wq!``
   to save and quit.
-  Save the file and quit the editor. Then go to System Preferences »
   Sharing » Services, unlock it, disable Remote Login, and final
   re-enable Remote Login. You can check if things worked by using
   Bonjour Browser or some such similar app to be sure ssh/sftp no
   longer show up.
-  A simple ``grep -ir bonjour /System/Library/LaunchDaemons/`` gives:

   ::

       /System/Library/LaunchDaemons/com.apple.AppleFileServer.plist:                  <key>Bonjour</key>
       /System/Library/LaunchDaemons/com.apple.bld.bulletd.plist:                      <key>Bonjour</key>
       /System/Library/LaunchDaemons/com.apple.eppc.plist:                        <key>Bonjour</key>
       /System/Library/LaunchDaemons/com.apple.FileSyncAgent.sshd.plist:                       <key>Bonjour</key>
       /System/Library/LaunchDaemons/com.apple.msrpc.echosvc.plist:                    <key>Bonjour</key>
       /System/Library/LaunchDaemons/com.apple.msrpc.echosvc.plist:                    <key>Bonjour</key>
       /System/Library/LaunchDaemons/com.apple.msrpc.lsarpc.plist:                     <key>Bonjour</key>
       /System/Library/LaunchDaemons/com.apple.msrpc.lsarpc.plist:                     <key>Bonjour</key>
       /System/Library/LaunchDaemons/com.apple.msrpc.mdssvc.plist:                     <key>Bonjour</key>
       /System/Library/LaunchDaemons/com.apple.msrpc.netlogon.plist:                   <key>Bonjour</key>
       /System/Library/LaunchDaemons/com.apple.msrpc.srvsvc.plist:                     <key>Bonjour</key>
       /System/Library/LaunchDaemons/com.apple.msrpc.srvsvc.plist:                     <key>Bonjour</key>
       /System/Library/LaunchDaemons/com.apple.msrpc.wkssvc.plist:                     <key>Bonjour</key>
       /System/Library/LaunchDaemons/com.apple.msrpc.wkssvc.plist:                     <key>Bonjour</key>
       /System/Library/LaunchDaemons/com.apple.odproxyd.plist:                 <key>Bonjour</key>
       /System/Library/LaunchDaemons/com.apple.screensharing.plist:                    <key>Bonjour</key>
       /System/Library/LaunchDaemons/com.apple.smbd.plist:                     <key>Bonjour</key>
       /System/Library/LaunchDaemons/ftp.plist:                        <key>Bonjour</key>
       /System/Library/LaunchDaemons/ssh.plist:                        <key>Bonjour</key>
       Binary file /System/Library/LaunchDaemons/telnet.plist matches

   so, you may want to change these too.
