.. title: running embarassingly parallel simulations on a multicore machine using bash loops
.. slug: 2010-08-09-running-embarassingly-parallel-simulations-on-a-multicore-machine-using-bash-loops
.. date: 2010-08-09 13:36:57
.. type: text
.. tags: sciblog


-  I need to run a single-processor experiment on some parameters, say N
   times

.. TEASER_END

-  embarassingly parallel: ``python experiment_all.py`` scans all these
   parameters:

   ::

          1 for i in range(N):
          2     if experiment[i] is not finished and not locked:
          3         lock(experiment[i])
          4         run(experiment[i])

-  to run this on 8 cores, ``bash`` is your friend (may also apply to
   ``*sh`` where ``*`` is either z, c, tc, ...)

   ::

       for i in {1..8}; do cd /data/work/ && python experiment_all.py  & done

-  however, runnning them simultaneously may cause problems if the
   locking mechanism is not fast enough, so I introduce a random jitter

   ::

       for i in {1..8}; do cd /data/work/ && sleep 0.$(( RANDOM%1000 )) ; python experiment_all.py  & done
