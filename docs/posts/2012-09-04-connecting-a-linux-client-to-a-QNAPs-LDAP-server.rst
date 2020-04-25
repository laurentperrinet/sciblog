.. title: connecting a linux client to a QNAP's LDAP server
.. slug: 2012-09-04-connecting-a-linux-client-to-a-QNAPs-LDAP-server
.. date: 2012-09-04 13:36:57
.. type: text
.. tags: info, sciblog


-  after installing a linux client, you usually wish to have the same
   users as on your QNAP server. A LDAP server is one useful solution.



.. TEASER_END

.. warning::

  This post is certainly obsolete...


-  on the server side, setup according to:
   `http://web.qnap.com/pro\_application.asp?ap\_id=847 <http://web.qnap.com/pro_application.asp?ap_id=847>`__

   -  one note: the domain name is a name you choose for your server
      (not the domain name of your local network), something useful for
      the LDAP server to recognise itself (like my-nas.local).

-  on the client side, there are several HOWTOs, like:

   -  my favorite:
      `http://mcwhirter.com.au/craige/blog/2006/Making-a-Debian-or-Ubuntu-Machine-an-LDAP-Authentication-Client <http://mcwhirter.com.au/craige/blog/2006/Making-a-Debian-or-Ubuntu-Machine-an-LDAP-Authentication-Client>`__
   -  `http://www.linuxhomenetworking.com/wiki/index.php/Quick\_HOWTO\_:\_Ch31\_:\_Centralized\_Logins\_Using\_LDAP\_and\_RADIUS#Configuring\_The\_LDAP\_Client <http://www.linuxhomenetworking.com/wiki/index.php/Quick_HOWTO_:_Ch31_:_Centralized_Logins_Using_LDAP_and_RADIUS#Configuring_The_LDAP_Client>`__
   -  `http://beginlinux.com/server\_training/server-managment-topics/1017-ldap-client-on-ubuntu-804 <http://beginlinux.com/server_training/server-managment-topics/1017-ldap-client-on-ubuntu-804>`__
   -  `http://doc.ubuntu-fr.org/ldap\_client <http://doc.ubuntu-fr.org/ldap_client>`__
      (in french)
   -  it usually takes two minutes if you copy and paste on the client
      side the information of your NAS server's LDAP page

-  unfortunately, it failed with "failed to bind to LDAP server
   ldap://192.168.0.5/: Invalid credentials"

   -  the (undocumented) solution was to:
   -  generate a password on the server side using the slappasswd
      command
   -  on the client side, copy and paste the generated SHA password
      instead of the password in clear text in the /etc/ldap.conf
      configuration file
