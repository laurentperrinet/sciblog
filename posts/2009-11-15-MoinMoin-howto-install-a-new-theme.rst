.. title: MoinMoin: howto install a new theme
.. slug: 2009-11-15-MoinMoin-howto-install-a-new-theme
.. date: 2009-11-15 13:36:57
.. type: text
.. tags: sciblog


-  locally

   ::

       scp Downloads/moniker18_2.1.1.zip  perrinet@195.221.164.4:/var/www/moin/perrinet/data/plugin/theme/tmp

       .. TEASER_END


-  on the server

   ::

       cd /var/www/moin/perrinet/data/plugin/theme/
       export USER=www-data
       export GROUP=www-data
       export INSTANCE=/usr/share/moin/htdocs/moniker
       unzip moniker18_2.1.1.zip
       cd moniker18_2.1.1
       cat read\ me\ on\ installing.txt
       cp -r moniker /usr/share/moin/htdocs/
       cp moniker18.py ../../
       chgrp -R $GROUP $INSTANCE
       chgrp -R $GROUP ../../moniker18.py
       vim ../../../../../../perrinet.py # set moniker18 as default
