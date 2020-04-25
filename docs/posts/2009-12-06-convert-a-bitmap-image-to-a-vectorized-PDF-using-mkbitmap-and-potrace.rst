.. title: convert a bitmap image to a vectorized PDF using mkbitmap and potrace
.. slug: 2009-12-06-convert-a-bitmap-image-to-a-vectorized-PDF-using-mkbitmap-and-potrace
.. date: 2009-12-06 13:36:57
.. type: text
.. tags: sciblog


-  to convert a bitmap image to a vectorized PDF, use
   `potrace <http://potrace.sourceforge.net/samples.html>`__ and
   `mkbitmap <http://potrace.sourceforge.net/mkbitmap.html>`__

.. TEASER_END
.. warning::

  This post is certainly obsolete...

-  it' a snap to install using MacPorts

   ::

       $ port info potrace
       potrace @1.8 (graphics)
       Variants:             a4_default, metric_default, universal

       Description:          Potrace is a utility for tracing a bitmap, which means, transforming a bitmap into a smooth, scalable image. The
                             input is a bitmap (PBM, PGM, PPM, or BMP), and the default output is one of several vector file formats. A
                             typical use is to create EPS files from scanned data, such as company or university logos, handwritten notes,
                             etc. The resulting image is not jaggy like a bitmap, but smooth. It can then be rendered at any resolution.
       Homepage:             http://potrace.sourceforge.net/

       Library Dependencies: zlib
       Platforms:            darwin
       License:              unknown
       Maintainers:          nomaintainer@macports.org
       manga:~ lup$ port variants potrace
       potrace has the variants:
          a4_default: compile potrace with A4 as the default page size.
          metric_default: compile potrace with centimeters as the default unit  instead of inches.
          universal: Build for multiple architectures

-  to install

   ::

       sudo port install potrace +a4_default +metric_default

-  check man pages and open your input for inspection

   ::

       man mkbitmap
       man potrace
       open dubout.png

-  you can use directly this workflow

   ::

       convert dubout.png ppm:- | mkbitmap -f 2 -s 2 -t 0.48 | potrace -t 5 --progress -b pdf -o dubout.pdf

-  but ``convert`` being what it is, first do

   ::

       convert dubout.png dubout.ppm

-  to take some more time fine tuning parameters:

   ::

       cat dubout.ppm | mkbitmap  -t 0.48 | potrace -t 15 --progress -b pdf -o dubout.pdf

-  in particular, the ``-x`` option resets defaults:

   ::

       cat dubout.ppm | mkbitmap  -x -s 2 -3 -t 0.5 | potrace -t 25 --progress -b pdf -o dubout.pdf

-  wait and ... enjoy!

| **Please Note**
|  This is a code snippet.
