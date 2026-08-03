.. title: installing Dovecot on MacOsX using MacPorts
.. slug: 2010-11-04-installing-Dovecot-on-MacOsX-using-MacPorts
.. date: 2010-11-04 13:36:57
.. type: text
.. tags: using, macos, sciblog

.. TEASER_END
.. warning::

  This post is certainly obsolete...



-  master howto:
   `https://trac.macports.org/wiki/howto/SetupDovecot <https://trac.macports.org/wiki/howto/SetupDovecot>`__



-  Install

   ::

       sudo port install dovecot
       sudo port load dovecot

-  Configure

   ::

       sudo cp /opt/local/etc/dovecot/dovecot-example.conf  /opt/local/etc/dovecot/dovecot.conf

       sudo vim /opt/local/etc/dovecot/dovecot.conf

-  Mine reads (it's just meant to access imap files from the local mail
   server and not to serve outside the localhost):

   ::

       protocols = imap
       listen = localhost:10143
       disable_plaintext_auth = no
       ssl = no
       mail_location = maildir:~/Maildir
       protocol imap {
       }
       auth default {
         mechanisms = plain
         passdb pam {
           args = login
         }
         userdb passwd {
             args =
         }
       user = root
       dict {
       }

-  Reload

   ::

       sudo launchctl stop org.macports.dovecot
       sudo launchctl start org.macports.dovecot

-  It does not work on the first try... so read documentation

   ::

       less /opt/local//share/doc/dovecot/documentation.txt
       less /opt/local//share/doc/dovecot/auth-protocol.txt
       less /opt/local//share/doc/dovecot/wiki/PasswordDatabase.PAM.txt

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
