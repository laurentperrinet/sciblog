.. title: setting the umask to define default permissions for created files
.. slug: 2012-11-28-setting-the-umask-to-define-default-permissions-for-created-files
.. date: 2012-11-28 13:36:57
.. type: text
.. tags: int, sciblog


-  the parameter to use is umask
   `https://en.wikipedia.org/wiki/Umask <https://en.wikipedia.org/wiki/Umask>`__



.. TEASER_END



-  on a cluster I get

   ::

       $ umask
       0022
       $ touch test
       $ ls -l test
       -rw-r--r-- 1 perrinet.l invibe 0 Nov 28 11:32 test
       $ umask u=rwx,g=rwx,o=
       $ touch test2
       $ ls -l test2
       -rw-rw---- 1 perrinet.l invibe 0 Nov 28 11:33 test2

-  so I did:

   ::

       perrinet.l@frioul:~$ vim .profile

       # ~/.profile: executed by the command interpreter for login shells.
       # This file is not read by bash(1), if ~/.bash_profile or ~/.bash_login
       # exists.
       # see /usr/share/doc/bash/examples/startup-files for examples.
       # the files are located in the bash-doc package.

       # the default umask is set in /etc/profile; for setting the umask
       # for ssh logins, install and configure the libpam-umask package.
       #umask 022
       # https://en.wikipedia.org/wiki/Umask
       umask u=rwx,g=rwx,o=

       # if running bash
       if [ -n "$BASH_VERSION" ]; then
           # include .bashrc if it exists
           if [ -f "$HOME/.bashrc" ]; then
               . "$HOME/.bashrc"
           fi
       fi

       # set PATH so it includes user's private bin if it exists
       if [ -d "$HOME/bin" ] ; then
           PATH="$HOME/bin:$PATH"
       fi

-  before loging out I have

   ::

       perrinet.l@frioul:~$ umask
       0022

-  and after

   ::

       perrinet.l@frioul:~$ logout
       Connection to frioul.int.univ-amu.fr closed.
       [11:36:49]int-users-4-058: ~/Desktop/Dropbox/TROPIQUE/demos/12-11-11_projection $ frioul

        ######  #####      #     ####   #    #  #
        #       #    #     #    #    #  #    #  #
        #####   #    #     #    #    #  #    #  #
        #       #####      #    #    #  #    #  #
        #       #   #      #    #    #  #    #  #
        #       #    #     #     ####    ####   ######

       perrinet.l@frioul:~$ umask
       0007
       perrinet.l@frioul:~$ touch test
       perrinet.l@frioul:~$ ls -l test
       -rw-rw---- 1 perrinet.l invibe 0 Nov 28 11:37 test
       perrinet.l@frioul:~$

-  Done!
