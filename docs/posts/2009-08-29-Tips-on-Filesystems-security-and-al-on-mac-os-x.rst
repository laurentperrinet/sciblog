.. title: Tips on Filesystems, security and al on mac os x
.. slug: 2009-08-29-Tips-on-Filesystems-security-and-al-on-mac-os-x
.. date: 2009-08-29 13:36:57
.. type: text
.. tags: macos, sciblog


-  mount with AFP sharepoints from the command line (thanks to this
   `hint <http://plumblossom.org/macclt.html>`__) :

   ::

       # mount_afp [-i] [-o options] afp_url node
       mkdir /Volumes/truc
       mount_afp afp://user:PASSWORD@server/truc /Volumes/truc
       umount /Volumes/truc
       rmdir /Volumes/truc


.. TEASER_END

finder nags when changing a file's extension
--------------------------------------------

-  read the default value (should be 0)

   ::

       defaults read com.apple.finder FXEnableExtensionChangeWarning

-  change it:

   ::

        defaults write com.apple.finder FXEnableExtensionChangeWarning False

Make spell check show only desired languages
--------------------------------------------

-  `http://www.macosxhints.com/article.php?story=20090512175846504 <http://www.macosxhints.com/article.php?story=20090512175846504>`__

HFS+
----

-  `Mac OS X
   Filesystems <http://www.kernelthread.com/mac/osx/arch_fs.html>`__
-  One feature of HFS volumes is that fle are referred to as links: for
   instance you can read a PDF file while changing the name at the same
   time. No problem!
-  Safely remove '.\_' files created by HFS(+)

   ::

       find . -name '._*' -print0 | xargs -0 rm

Spotlight
---------

-  to remove the remaining index files on the volume using the command:
   `` sudo mdutil -E /Volumes/volume_name `` utilitaires CLI :

   ::

       sudo mdutil --help
       mdutil: unrecognized option `--help'
       usage: mdutil -pE volume ...
               mdutil can be used to manage the metadata stores used by Spotlight.
               -p              publish metadata for the provided volumes.
               -i (on|off)     set indexing status for the provided volumes.
               -E              erase the master copy of the metadata stores for the provided volumes.
               -s              print indexing status for the provided volumes.

System & Security
-----------------

-  `http://www.macgeekery.com/tips/security/basic\_mac\_os\_x\_security <http://www.macgeekery.com/tips/security/basic_mac_os_x_security>`__
-  Synthesis of unauthorized accesses to your machine:

   ::

       sudo grep "failed to auth" /var/log/secure.log | sed 's/^.*user \(.*\) for.*$/\1/' | sort | uniq -c

nmap
----

-  to scan for open ports on a remote machine :

   ::

       sudo nmap -T3 -vv -sS -p 1-65535 -P0 google.com
       Starting nmap 3.81 ( http://www.insecure.org/nmap/ ) at 2006-04-05 16:32 CEST
       Initiating SYN Stealth Scan against google.com [65535 ports] at 16:32
       Discovered open port 80/tcp on google.com
       SYN Stealth Scan Timing: About 2.18% done; ETC: 16:55 (0:22:26 remaining)

-  to scan for open ports on your local network (see https://stackoverflow.com/questions/13669585/how-to-get-a-list-of-all-valid-ip-addresses-in-a-local-network#15351073 ):

   ::

       nmap -sP 192.168.1.*

Dash board
----------

-  Don't use Dashboard? No particular reason to leave it running,
   consuming memory. Following
   `http://www.macosxhints.com/article.php?story=20050723123302403 <http://www.macosxhints.com/article.php?story=20050723123302403>`__,
   you can turn Dashboard off by doing:

   ::

       defaults write com.apple.dashboard mcx-disabled -boolean YES
       killall Dock

-  Unsurprisingly, you change YES to NO to re-enable Dashboard:

   ::

       defaults write com.apple.dashboard mcx-disabled -boolean NO
       killall Dock

Unix - X11
----------

-  `http://xquartz.macosforge.org/ <http://xquartz.macosforge.org/>`__
-  install quickly
   `http://trac.macosforge.org/projects/xquartz <http://trac.macosforge.org/projects/xquartz>`__
   :

   ::

       wget http://xquartz.macosforge.org/downloads/X11-2.4.0.dmg
       sudo installer -pkg X11-2.4.0.pkg  -target /
       rm  X11-2.4.0.pkg

Change login window on (Snow) Leopard
-------------------------------------

-  disrupted by the look of the plasma flames? think it looks like a
   cheap star trek sundae? check
   `http://paulstamatiou.com/2007/10/31/how-to-change-leopards-login-wallpaper <http://paulstamatiou.com/2007/10/31/how-to-change-leopards-login-wallpaper>`__
   :

   ::

       cd /System/Library/CoreServices
       sudo rm DefaultDesktop.jpg
       #sudo mv DefaultDesktop.jpg DefaultDesktop_old.jpg # if you want to keep the Aurora stuff (it stills around, do a 'locate Aurora'
       sudo ln -s /Library/Desktop\ Pictures/Nature/Stones.jpg DefaultDesktop.jpg
