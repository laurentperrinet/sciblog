.. title: ubuntu : starting sshd at boot
.. slug: 2011-01-18-ubuntu-starting-sshd-at-boot
.. date: 2011-01-18 13:36:57
.. type: text
.. tags: sciblog


-  ssh server installed but not starting at boot (I certainly messed up
   something):

   ::

       $ ls -l /etc/init.d/*ssh*
       -rwxr-xr-x 1 root root 3704 2010-09-14 19:20 /etc/init.d/ssh
       $ ls -l /etc/rc2.d/*ssh*
       ls: cannot access /etc/rc2.d/*ssh*: No such file or directory
       $ ls -l /etc/rc1.d/*ssh*


.. TEASER_END


-  a solution is to use ``update-rc.d``:

   ::

       usage: update-rc.d [-n] [-f] <basename> remove
              update-rc.d [-n] <basename> defaults [NN | SS KK]
              update-rc.d [-n] <basename> start|stop NN runlvl [runlvl] [...] .
              update-rc.d [-n] <basename> disable|enable [S|2|3|4|5]
                       -n: not really
                       -f: force

       The disable|enable API is not stable and might change in the future.

-  by issuing :

   ::

       $ sudo update-rc.d ssh defaults
       update-rc.d: warning: ssh stop runlevel arguments (0 1 6) do not match LSB Default-Stop values (none)
        Adding system startup for /etc/init.d/ssh ...
          /etc/rc0.d/K20ssh -> ../init.d/ssh
          /etc/rc1.d/K20ssh -> ../init.d/ssh
          /etc/rc6.d/K20ssh -> ../init.d/ssh
          /etc/rc2.d/S20ssh -> ../init.d/ssh
          /etc/rc3.d/S20ssh -> ../init.d/ssh
          /etc/rc4.d/S20ssh -> ../init.d/ssh
          /etc/rc5.d/S20ssh -> ../init.d/ssh

-  should work now |:-)|

   ::

       $ ls -l /etc/rc1.d/*ssh*
       lrwxrwxrwx 1 root root 13 2011-01-18 21:33 /etc/rc1.d/K20ssh -> ../init.d/ssh



.. |:-)| image:: https://invibe.net/moin_static196/moniker/img/smile.png
