.. title: SparkleShare on a QNAP
.. slug: 2013-11-04-SparkleShare-on-a-QNAP
.. date: 2013-11-04 13:36:57
.. type: text
.. tags: using, sciblog

-  SparkleShare is a great alternative to DropBox
-  Fetch the Dazzle script on
   `https://github.com/hbons/Dazzle <https://github.com/hbons/Dazzle>`__

   ::

         curl https://raw.github.com/hbons/Dazzle/master/dazzle.sh   --output /usr/bin/dazzle && chmod +x /usr/bin/dazzle


.. TEASER_END

.. warning::

  This post is certainly obsolete...


-  set-up variables:

   ::

       export DAZZLE_USER=admin
       export DAZZLE_HOME=/share/Multimedia/dazzle

-  do it:

   ::

       dazzle setup
       dazzle create pool # a first project
       dazzle create-encrypted passwords # this one is completely encrypted on the server side and before the files leave the client
