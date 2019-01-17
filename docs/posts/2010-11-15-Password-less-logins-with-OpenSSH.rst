.. title: Password-less logins with OpenSSH
.. slug: 2010-11-15-Password-less-logins-with-OpenSSH
.. date: 2010-11-15 13:36:57
.. type: text
.. tags: sciblog

-  from
   `http://www.debian-administration.org/articles/152 <http://www.debian-administration.org/articles/152>`__

Because OpenSSH allows you to run commands on remote systems, showing
you the results directly, as well as just logging in to systems it's
ideal for automating common tasks with shellscripts and cronjobs. One
thing that you probably won't want is to do though is store the remote
system's password in the script. Instead you'll want to setup SSH so
that you can login securely without having to give a password.


.. TEASER_END


Thankfully this is very straightforward, with the use of public keys.

To enable the remote login you create a pair of keys, one of which you
simply append to a file upon the remote system. When this is done you'll
then be able to login without being prompted for a password - and this
also includes any cronjobs you have setup to run.

If you don't already have a keypair generated you'll first of all need
to create one.

To generate a new keypair you run the following command:

::

    skx@lappy:~$ ssh-keygen -t rsa

This will prompt you for a location to save the keys, and a pass-phrase:

::

    Generating public/private rsa key pair.
    Enter file in which to save the key (/home/skx/.ssh/id_rsa):
    Enter passphrase (empty for no passphrase):
    Enter same passphrase again:
    Your identification has been saved in /home/skx/.ssh/id_rsa.
    Your public key has been saved in /home/skx/.ssh/id_rsa.pub.

If you accept the defaults you'll have a pair of files created, as shown
above, with no passphrase. This means that the key files can be used as
they are, without being "unlocked" with a password first. If you're
wishing to automate things this is what you want.

Now that you have a pair of keyfiles generated, or pre-existing, you
need to append the contents of the .pub file to the correct location on
the remote server.

Assuming that you wish to login to the machine called mystery from your
current host with the id\_rsa and id\_rsa.pub files you've just
generated you should run the following command:

::

    ssh-copy-id -i ~/.ssh/id_rsa.pub username@mystery

This will prompt you for the login password for the host, then copy the
keyfile for you, creating the correct directory and fixing the
permissions as necessary.

The contents of the keyfile will be appended to the file
~/.ssh/authorized\_keys2 for RSA keys, and ~/.ssh/authorised\_keys for
the older DSA key types.

Once this has been done you should be able to login remotely, and run
commands, without being prompted for a password:

::

    skx@lappy:~$ ssh mystery uptime
     09:52:50 up 96 days, 13:45,  0 users,  load average: 0.00, 0.00, 0.00
