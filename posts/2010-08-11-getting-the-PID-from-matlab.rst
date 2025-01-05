.. title: getting the PID from matlab
.. slug: 2010-08-11-getting-the-PID-from-matlab
.. date: 2010-08-11 13:36:57
.. type: text
.. tags: sciblog

-  I need the pid to know if one of the many simulations I run are still
   running. There's no native solution in matlab to my knowledge.

.. TEASER_END
.. warning::

  This post is certainly obsolete...

-  using hint @
   `http://www.mathworks.cn/matlabcentral/newsreader/view\_thread/268529 <http://www.mathworks.cn/matlabcentral/newsreader/view_thread/268529>`__
-  create ``getpid.c`` with

   ::

          1 #include "mex.h"
          2 #include <unistd.h>
          3 mexFunction(int nlhs, mxArray *plhs[ ], int nrhs, const mxArray *prhs[ ])
          4 {
          5   plhs[0] = mxCreateDoubleScalar((double) getpid());
          6 }

-  compile with ``mex getpid.c``
-  use in matlab as ``pid = getpid()``
-  this is part of the package in
   `SparseHebbianLearning <https://laurentperrinet.github.io/publication/perrinet-19-hulk>`__
