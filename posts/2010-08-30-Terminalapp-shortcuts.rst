.. title: Terminal.app shortcuts
.. slug: 2010-08-30-Terminalapp-shortcuts
.. date: 2010-08-30 13:36:57
.. type: text
.. tags: macos, sciblog


-  from
   `http://superuser.com/questions/52483/terminal-tips-and-tricks-for-mac-os-x <http://superuser.com/questions/52483/terminal-tips-and-tricks-for-mac-os-x>`__

   ::

       To make Ctrl← and Ctrl→  useful again, that is going a word forward or backward like they usually do on Linux, you must make Terminal.app send the right string to the shell. In the preferences, go to the Settings tab and select your default profile. Go to Keyboard and set control cursor left and control cursor right to send string \033b and \033f respectively.

       While your're at it, you can also fix Home (\033[H), End (\033[F), Page Up (\033[5~) and Page Down (\033[6~) so that they send those keys to the shell instead of scrolling the buffer.
