.. title: installing MoinMoin on a OVH server
.. slug: 2012-01-07-installing-MoinMoin-on-a-OVH-server
.. date: 2012-01-07 13:36:57
.. type: text
.. tags: moinmoin, sciblog


-  due to a disruption on my previous server, I had to move in a rush to
   a new server.


.. TEASER_END

-  choosing the right provider

   -  `http://240plan.ovh.net/infos/python.cgi <http://240plan.ovh.net/infos/python.cgi>`__
   -  `http://240plan.ovh.net/net2ftp/index.php <http://240plan.ovh.net/net2ftp/index.php>`__

-  getting a basic MoinMoin instance running

   -  `http://moinmo.in/via\_ftp\_on\_vserver <http://moinmo.in/via_ftp_on_vserver>`__
   -  `http://hg.moinmo.in/moin/1.9/raw-file/1.9.3/docs/REQUIREMENTS <http://hg.moinmo.in/moin/1.9/raw-file/1.9.3/docs/REQUIREMENTS>`__

-  getting the path of the pages on the server using the ``explore.py``
   script in
   `http://wiki.python.org/jython/HelpOnInstalling/ApacheOnLinuxFtp <http://wiki.python.org/jython/HelpOnInstalling/ApacheOnLinuxFtp>`__
-  setting up an empty MoinMoin instance, using:

   -  the following ``cgi-bin/index.cgi`` script:

      ::

             1 #!/usr/bin/python
             2
             3 import sys, os
             4
             5 sys.path.insert(0, '/homez.52/invibe/moin')
             6
             7 os.environ['FCGI_FORCE_CGI'] = 'N' # 'Y' for (slow) CGI, 'N' for FCGI
             8
             9 from MoinMoin.web.flup_frontend import CGIFrontEnd
            10 CGIFrontEnd().run()

   -  setting up the right path in ``xikiconfig.py`` :

      ::

             1     data_dir = '/homez.52/invibe/moin/data/'
             2     data_underlay_dir = '/homez.52/invibe/moin/underlay_min/'
             3     url_prefix_static = '/moin_static193'
             4     url_mappings = {'/cgi-bin/index.cgi':'/LaurentPerrinet'}

   -  note that I installed the htdocs as ``www/moin_static193``

-  once functional, getting my old stuff on the new server

   -  do not forget to set up permissions to ``755`` on the site (I used
      their online ftp tool for that -
      `http://240plan.ovh.net/net2ftp/index.php <http://240plan.ovh.net/net2ftp/index.php>`__
      )

-  rewrite rule

   -  `http://rabaix.net/en/articles/2007/08/31/how-to-install-django-on-ovh-net <http://rabaix.net/en/articles/2007/08/31/how-to-install-django-on-ovh-net>`__
   -  `http://guide.ovh.com/HtaccessModRewrite <http://guide.ovh.com/HtaccessModRewrite>`__
   -  I opted for this config in the ``www/.htaccess`` file:

      ::

          Options +FollowSymlinks
          RewriteEngine on
          RewriteRule ^LaurentPerrinet$  LaurentPerrinet/ [L]
          RewriteRule ^LaurentPerrinet(.*)$  /cgi-bin/index.cgi$1 [L]
          RewriteRule !(moin_static193|images|robots.txt|favicon.ico|cgi-bin) LaurentPerrinet  [L]

-  overall, this process was not linear and quite frustrating as there
   is no ssh (only a ftp) access and absolutely no simple guide and
   worse, no logfile from apache (you see quite often an "error 500"
   without any cue as what is going wrong)
