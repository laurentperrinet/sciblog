.. title: installing Dovecot on QNAP
.. slug: 2012-08-27-installing-Dovecot-on-QNAP
.. date: 2012-08-27 13:36:57
.. type: text
.. tags: using, sciblog


-  master howto:
   `http://forum.qnap.com/viewtopic.php?f=143&t=33376&start=30 <http://forum.qnap.com/viewtopic.php?f=143&t=33376&start=30>`__



.. TEASER_END


-  Configure

   ::

       sh xdove.sh stop
       cd /share/HDA_DATA/.qpkg/XDove
       vim dovecot/etc/dovecot/dovecot.conf

-  Mine reads (it's just meant to access imap files from the local mail
   server and not to serve outside the localhost):

   ::

       auth_user = admin
       login_user = dovecot
       login_chroot = no
       protocols = imaps
       listen = localhost:993
       log_path = /var/log/dovecot/dovecot.log
       info_log_path = /var/log/dovecot/dovecot-info.log
       #ssl_disable = yes
       #ssl = no
       #disable_plaintext_auth = no
       ssl = yes
       ssl_cert_file = /etc/stunnel/stunnel.pem
       ssl_key_file = /etc/stunnel/stunnel.pem
       mail_location = maildir:/var/MailRoot/domains/%d/%n/Maildir
       first_valid_uid = 10

       dotlock_use_excl=yes
       mailbox_idle_check_interval = 30
       maildir_stat_dirs = no
       maildir_copy_with_hardlinks = no

       auth_executable = /usr/libexec/dovecot/dovecot-auth
       auth_username_chars = abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ01234567890.-_@
       auth_verbose = yes
       auth_debug = yes
       auth_debug_passwords = yes
       mail_debug = yes

       protocol imap {
       #       login_greeting_capability = yes
               imap_client_workarounds = tb-extra-mailbox-sep
               login_executable = /usr/libexec/dovecot/imap-login
               mail_executable = /usr/libexec/dovecot/imap
               #imap_client_workarounds = outlook-idle
       }

       auth default {
              mechanisms = plain
              passdb checkpassword {
              args = /usr/bin/checkpassword
              }

              userdb static {
              args = uid=xmail gid=xmail home=/var/MailRoot/domains/%d/%n/Maildir
              }
       }

-  Reload

   ::

       sh xdove.sh restart
