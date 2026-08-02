.. title: installing Dovecot on debian
.. slug: 2012-02-08-installing-Dovecot-on-debian
.. date: 2012-02-08 13:36:57
.. type: text
.. tags: using, sciblog


-  master howto:
   `https://trac.macports.org/wiki/howto/SetupDovecot <https://trac.macports.org/wiki/howto/SetupDovecot>`__
-  Install

   ::

       sudo aptitude install dovecot


.. TEASER_END
.. warning::

  This post is certainly obsolete...


-  Configure

   ::

       sudo vim /etc/dovecot/dovecot.conf

-  Mine reads (it's just meant to access imap files from the local mail
   server and not to serve outside the localhost):

   ::

       protocols = imaps
       listen = localhost:10943
       mail_location = maildir:~/Maildir
       protocol imap {
           ssl_listen = *:993
       }
       ssl_disable = no
       ssl_cert_file = /etc/ssl/certs/ssl-cert-snakeoil.pem
       ssl_key_file = /etc/ssl/private/ssl-cert-snakeoil.key

-  Reload

   ::

       sudo service dovecot restart
