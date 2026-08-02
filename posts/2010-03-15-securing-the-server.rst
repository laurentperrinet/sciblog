.. title: securing the server
.. slug: 2010-03-15-securing-the-server
.. date: 2010-03-15 13:36:57
.. type: text
.. tags: macos, sciblog


-  SSH (Secure Shell) is installed on most systems (here GnuLinuxUbuntu and MacOsX) so
   don't panic about compilations (try Putty on Windows). Try a simple
   ``ssh -V`` to check version or ``which ssh`` to locate the binary.


   .. TEASER_END

-  Thanks to ``ssh``, you can transport all your data (accessing files,
   merging repositories, lauching remote X programs) transparently using
   a secure connection. Thanks to tunneling, this is also simpler thus
   more secure for your computer and your provider. Having all security
   located in one interface sure is a big advantage: once your SSH
   communication channel is set-up, you should only focus on what you
   wish to do (SVN, etc...).
-  Most documentation may be found in ``man ssh``, ``man ssh-keygen``
   (remember that thanks to the underlying pager system, you can search
   for a keyword, for instance ``hello``, by typing ``\hello[ENTER]``).
   Many other sources of help exist, such as this
   `FAQ <http://www.employees.org/~satch/ssh/faq/ssh-faq.html>`__

Setting up SSH: spreading the good keys
=======================================

#. There are many ways to authenticate your session, but mainly password
   or keys. Keys are to be preferred to avoid typing your password 10
   times a day. It is also most secure (you type your key's password
   locally and not remotely).
#. Generate a private/public key pair. Simple command to do this:

   ::

       ssh-keygen -t rsa

#. Copy the key to the

   ::

       ssh-copy-id -i ~/.ssh/id_rsa.pub username@host

   . this can be also be done using

   ::

       scp ~/.ssh/id_rsa.pub username@host:~/mykey.pub
       ssh username@host
       cat mykey.pub >> .ssh/authorized_keys

#. Now try logging into the remote machine again from local

   ::

       ssh REMOTE_USERNAME@remote_host

#. Check that your public key is in the list of authorized keys:
   ``.ssh/authorized_keys``.
#. Change password regularly:

   ::

       ssh-keygen -p

   It is not advised to put an empty pass-phrase, rather use key agent
   (see below).

Aliasing
--------

-  it is possible to create alias of the ssh binary to hostnames... but
   more simply, you may put

   ::

       alias myserver='ssh -Y -p2221 myuser@myserver.domain.com'

   where 2221 is here the port used by the SSH server on
   ``myserver.domain.com``

-  more cleanly, you may edit your `` .ssh/config`` file with:

   ::

       Host myserver.domain.com
               User myuser
               Port 2221

   Be careful that properties are right : ``chmod 600 ~/.ssh/config``

key agent
=========

-  An agent loads your keys on the local machines:

   -  it's more secure, since all passwords are typed locally, you only
      send encrypted authentifications
   -  it's more practical, since you type your password once per session

-  `http://www.sshkeychain.org/mirrors/SSH-with-Keys-HOWTO/ <http://www.sshkeychain.org/mirrors/SSH-with-Keys-HOWTO/>`__
-  GUI interface on MacOsX :
   `http://www.sshkeychain.org/ <http://www.sshkeychain.org/>`__

   -  install with macports using ``sudo port install SSHKeychain``,
      you'll find it in ``/Applications/MacPorts``

tunnels
=======

-  `http://souptonuts.sourceforge.net/sshtips.htm <http://souptonuts.sourceforge.net/sshtips.htm>`__
-  `http://projects.tynsoe.org/en/stm/doc.php <http://projects.tynsoe.org/en/stm/doc.php>`__

securing the server
===================

-  Robots usually try common name / password combinations on your SSH
   server. If you're the only user ``admin_name`` of your server you may
   use in the SSH server configuration file (usually
   ``/etc/ssh/sshd_config``) the option ``AllowUsers admin_name`` to
   restrict access to user ``admin_name`` and avoid brute force attacks.
   Since robots are most of the time dumb, they'll get an immediate
   ``acces denied`` response to any connection request.
-  Robots usually sniff port ``22``. To change the port which is
   listened by the SSH server, either modify the default port in the SSH
   server configuration file (usually ``/etc/ssh/sshd_config``). Another
   way is to use your router to redirect the outside port (for instance
   ``2221``) to the default port of your server.
