.. title: handling processes in bash
.. slug: 2011-01-29-handling-processes-in-bash
.. date: 2011-01-29 13:36:57
.. type: text
.. tags: sciblog


-  Give detailed information on all python processes:

   ::

       ps -fp $(pgrep -d, -x python)


.. TEASER_END


-  Make all python processes run nicer so that they do not obstruct
   other processes / users:

   ::

       renice 14 `pgrep python`

-  listing processes in the current bash session:

   ::

       jobs -l

-  stopping all python processes :

   ::

       pkill -s STOP python

-  resuming all python processes ( |alert| to test ... ) :

   ::

       pkill -s CONT python



.. |alert| image:: http://invibe.net/moin_static196/moniker/img/alert.png
