.. title: installing linux on imac hardware
.. slug: 2012-09-09-installing-linux-on-imac-hardware
.. date: 2012-09-09 13:36:57
.. type: text
.. tags: sciblog


-  on a 2007 imac that will slow to a crawl since mountain lion, I have
   installed linux mint (why not debian?)



.. TEASER_END


-  works as expected and the speed to check e-mails / browse the web is
   back
-  some bugs like this silly swapping of keys:
   `https://bugs.launchpad.net/ubuntu/+source/linux/+bug/214786 <https://bugs.launchpad.net/ubuntu/+source/linux/+bug/214786>`__
-  fix :
   ``echo 0 | sudo tee /sys/module/hid_apple/parameters/iso_layout``
