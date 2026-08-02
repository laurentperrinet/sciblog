.. title: setting some conventions common in Bibdesk (to work with bibtex, citeUlike)
.. slug: 2013-03-06-setting-some-conventions-common-in-Bibdesk-(to-work-with-bibtex-citeUlike)
.. date: 2013-03-06 13:36:57
.. type: text
.. tags: sciblog


-  I found this set useful to collaborate:

   -  citekey `` %a1%y%u0 ``
   -  rangement semi-automatique papiers: `` %f{Cite Key}%n0%e ``
   -  Topic = use citekey of related papers
   -  Comment (instead annote) to put... comments (as annote gets
      printed in the manuscript that would use the entry)


.. TEASER_END


-  to do that automatically, one may use this
   `tricks <http://sourceforge.net/apps/mediawiki/bibdesk/index.php?title=Tips_and_Tricks>`__:

   ::

       defaults write edu.ucsd.cs.mmccrack.bibdesk "Cite Key Format" -string "%a1%y%u0"¬
       defaults write edu.ucsd.cs.mmccrack.bibdesk BDSKLocalFileFormatKey -string "%f{Cite Key}%n0%e"

-  this is included in this script @
   `https://github.com/laurentperrinet/dotfiles/blob/master/init/install\_tex\_live.sh <https://github.com/laurentperrinet/dotfiles/blob/master/init/install_tex_live.sh>`__
