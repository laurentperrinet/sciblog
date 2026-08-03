.. title: SpikeStream & Nemo
.. slug: 2011-03-10-SpikeStream-&-Nemo
.. date: 2011-03-10 13:36:57
.. type: text
.. tags: sciblog


-  `SpikeStream <http://spikestream.sourceforge.net/pages/download.html>`__
   & Nemo are (ultra fast) neural simulation frameworks. cool. but how to compile
   on ubuntu?


.. TEASER_END
.. warning::

  This post is certainly obsolete...



-  dependencies:

   -  ::

          sudo apt-get install cmake libboost-all-dev libltdl-dev libgmp3-dev  libqwt-dev

   -  CUDA :
      `http://www.nvidia.com/object/thankyou.html?url=/compute/cuda/3\_2\_prod/toolkit/cudatoolkit\_3.2.16\_linux\_64\_ubuntu10.04.run <http://www.nvidia.com/object/thankyou.html?url=/compute/cuda/3_2_prod/toolkit/cudatoolkit_3.2.16_linux_64_ubuntu10.04.run>`__

-  now download and install Nemo with a standard

   ::

       mkdir build
       cd build
       cmake .. -D NEMO_MATLAB_ENABLED=NO ..
       make
       sudo make install

-  now download and install SpikeStream ... FAIL!
