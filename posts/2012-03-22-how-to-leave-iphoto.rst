.. title: how to leave iphoto
.. slug: 2012-03-22-how-to-leave-iphoto
.. date: 2012-03-22 13:36:57
.. type: text
.. tags: macos, sciblog


-  iphoto.app is certainly a nice tool, but it is also

   #. slow, unresponsive and locks you in some ugly closed-source
      format.
   #. also, try to look in forums when you want to share pictures on
      different {computers / OSs / iphoto versions / places / users} =
      nightmare!
   #. on top of that, the \*cloud stuff is intellectually just very
      corrupted...
   #. what decided me to drop it entirely was a sudden corruption of the
      library. It took 2 days to recover my files and re-rotate
      correctly all pictures...
   #. last nail in the coffin was the fact that libraries are not
      backward compatible : you have to upgrade to the new *product*.


.. TEASER_END
.. warning::

  This post is certainly obsolete...



-  so time to take back possession of your pictures!
-  I found some supporting arguments here:
   `http://accretiondisc.com/blog/2011/10/26/leaving-iphoto/ <http://accretiondisc.com/blog/2011/10/26/leaving-iphoto/>`__
-  solution: put the files in folders according to a date organization
   of the type ``2011/P0747444.jpg``, other tools for tagging, etc...
   follow naturally (and you share as you share folders on dropbox or
   whatever)
-  first, let's set the default application for upcoming pictures from
   cameras:

   #. With your camera connected, open Image Capture
   #. You will see your camera under devices. Click the icon.
   #. Down at the bottom, you will see “Connecting this iPhone opens…”
      with a pull-down menu under it.
   #. select "autoimport" (I choose "delete after importation")
   #. another solution is to use a feature from dropbox...

-  then, let's export the data from iPhoto: ``File.../Export...``. I
   kept the original file names but with the modifications (mainly
   rotations that were applied to my old camera without a gravity
   sensor). you should end up with lots of files in one directory. but
   it ... does not work as iphoto raises a completly unmeaningful error
   ('could not create file').
-  so, let's explore the library:

   #. it is package, and we can right-click in the finder to 'show
      package content'
   #. click the Masters folder to open it, and you'll see folders
      organized by year; inside are more folders organized by date and
      album, and inside them are photos in JPG format and video clips.

-  then I found
   `https://github.com/BMorearty/exportiphoto <https://github.com/BMorearty/exportiphoto>`__
   and you just have to type

   ::

       python exportiphoto.py Pictures/iPhoto\ Library Pictures/Photos

   to achieve the export

   -  I used the following commands to post-process all

      ::

          counting if everything was moved (there was some corruption in the library file with MOVies)
          find ~/Pictures/iPhoto\ Library/Masters/2012 -iname *MOV |wc -l
          find ~/Pictures/iPhoto\ Library/Masters -iname *MOV |wc -l
          find ~/Pictures/Photos -iname *MOV |wc -l

          # brute force to compare the content of the trees (brute force for the computer, you can get a coffee)
          mkdir ~/Pictures/Photos/2011
          chmod -R u+rwX ~/Pictures/Photos/2011
          find ~/Pictures/iPhoto\ Library/Masters/2011 -iname *MOV -exec cp {} ~/Pictures/Photos/2011/ \;
          mkdir ~/Pictures/Photos/2012
          find ~/Pictures/iPhoto\ Library/Masters/2012 -iname *MOV -exec cp {} ~/Pictures/Photos/2012/ \;

      (for the last exampls, see
      `http://en.wikipedia.org/wiki/Xargs <http://en.wikipedia.org/wiki/Xargs>`__
      )

-  at the end, the great relief is to remove all this iphoto cr\*p:

   ::

       cd ~/Pictures/
       rm -rf iPhoto*
       cd ~/Library/Caches
       rm -rf com.apple.iPhoto

-  I'll be glad to help anybody with similar problem
