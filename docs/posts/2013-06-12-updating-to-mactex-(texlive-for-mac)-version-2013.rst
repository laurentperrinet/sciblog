.. title: updating to mactex (texlive for mac), version 2013
.. slug: 2013-06-12-updating-to-mactex-(texlive-for-mac)-version-2013
.. date: 2013-06-12 13:36:57
.. type: text
.. tags: latex, sciblog


-  mactex is not there yet, but pre-relaeses are.

.. TEASER_END
.. warning::

  This post is certainly obsolete...


-  you can install the package from this
   `script <https://github.com/meduz/dotfiles/blob/master/init/osx_install_tex_live.sh>`__,
   or more simply

   ::

       wget http://ctan.ijs.si/mirror/tlpretest/mactex-2013.pkg # pre-release of TexLive 2013
       sudo installer -pkg mactex-2013.pkg -target /

-  to update your resource location to update packages, use

   ::

       sudo tlmgr option location  http://ftp.math.utah.edu/pub/texlive/tlpretest/

-  to upgrade

   ::

       sudo tlmgr update --self
       sudo tlmgr update --all
