.. title: upgrading owncloud to 5.0.0
.. slug: 2013-03-23-upgrading-owncloud-to-500
.. date: 2013-03-23 13:36:57
.. type: text
.. tags: sciblog


-  from
   `http://doc.owncloud.org/server/5.0/admin\_manual/maintenance/update.html <http://doc.owncloud.org/server/5.0/admin_manual/maintenance/update.html>`__
-  backup

   ::

       rsync -a owncloud/ owncloud_bkp`date +"%Y%m%d"`/


.. TEASER_END
.. warning::

  This post is certainly obsolete...


-  download

   ::

       mkdir tmp; cd tmp
       wget http://download.owncloud.org/community/owncloud-5.0.0.tar.bz2

-  remove old (except data and config)

   ::

       rm COPYING-* AUTHORS README *php db_structure.xml themes search lib l10n ocs core settings files apps 3rdparty backup
       tar -xzjf owncloud-5.0.0.tar.bz2
       rsync --inplace -rtv tmp/owncloud/ owncloud/

-  clean-up

   ::

       rm -fr tmp
