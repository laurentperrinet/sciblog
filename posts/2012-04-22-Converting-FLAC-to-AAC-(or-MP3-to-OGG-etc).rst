.. title: Converting FLAC to AAC (or MP3 to OGG etc...)
.. slug: 2012-04-22-Converting-FLAC-to-AAC-(or-MP3-to-OGG-etc)
.. date: 2012-04-22 13:36:57
.. type: text
.. tags: sciblog


-  the solution is
   `http://audiotools.sourceforge.net/ <http://audiotools.sourceforge.net/>`__



.. TEASER_END
.. warning::

  This post is certainly obsolete...



-  installation on MacOsX Lion (with homebrew) :

   ::

       brew install libcdio
       brew install lame two-lame mpg123 mp3gain
       brew install libogg libvorbis     vorbis-tools  vorbisgain
       brew install faac faad2
       git clone git://github.com/laurentperrinet/python-audio-tools.git  audio-tools
       cd audio-tools
       make
       make install

-  using it:

   ::

       track2track  -t aiff *.flac #lossless
       track2track  -q 0 -t m4a *.ogg #lossy

-  and on a whole folder, placing the files in the same directory:

   ::

       find a_folder/with/lots_of_flac -name *flac -exec sh -c 'echo "Processing $0"; track2track -t aiff  "$0" -o "${0%.flac}.aiff"' {} \;
       find a_folder/with/lots_of_ogg -name *ogg -exec sh -c 'echo "Processing $0"; track2track -t m4a  "$0" -o "${0%.flac}.m4a"' {} \;

-  tried as a formula in homebrew:
   `https://github.com/mxcl/homebrew <https://github.com/mxcl/homebrew>`__
   but closed it.
