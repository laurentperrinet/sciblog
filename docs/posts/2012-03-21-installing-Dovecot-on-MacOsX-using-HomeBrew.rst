.. title: installing Dovecot on MacOsX using HomeBrew
.. slug: 2012-03-21-installing-Dovecot-on-MacOsX-using-HomeBrew
.. date: 2012-03-21 13:36:57
.. type: text
.. tags: using, macos, sciblog


-  master howto:
   `https://trac.macports.org/wiki/howto/SetupDovecot <https://trac.macports.org/wiki/howto/SetupDovecot>`__




.. TEASER_END
.. warning::

  This post is certainly obsolete...


-  Install

   ::

       brew install dovecot
       sudo vim /Library/LaunchDaemons/homebrew.mxcl.dovecot.plist

-  Configure

   ::

       sudo cp /usr/local/etc/dovecot/dovecot-example.conf  /usr/local/etc/dovecot/dovecot.conf
       sudo vim /usr/local/etc/dovecot/dovecot.conf

-  Mine reads (it's just meant to access imap files from the local mail
   server and not to serve outside the localhost):

   ::

       disable_plaintext_auth = no
       mail_location = maildir:~/Maildir
       ssl = no
       default_login_user = lup
       passdb {
         args = login
         driver = pam
       }
       protocols = imap
       service auth {
         user = root
       }
       service imap-login {
         inet_listener imap {
           address = 127.0.0.1
           port = 10143
         }
         inet_listener imaps {
           address = 127.0.0.1
           port = 10943
         }
       }
       userdb {
         driver = passwd
       }

-  Reload

   ::

       sudo launchctl unload homebrew.mxcl.dovecot.plist
       sudo launchctl load homebrew.mxcl.dovecot.plist

-  It does not work on the first try... so read documentation

   ::

       less /usr/local/share/doc/dovecot/documentation.txt
       less /usr/local/share/doc/dovecot/auth-protocol.txt
       less /usr/local/share/doc/dovecot/wiki/PasswordDatabase.PAM.txt

-  Authentification

   ::

       ls -l /etc/pam.d/
       sudo vim /etc/pam.d/dovecot

   with ``/etc/pam.d/dovecot`` being

   ::

       auth       required       pam_permit.so
       account    required       pam_permit.so
       password   required       pam_deny.so
       session    required       pam_uwtmp.so
