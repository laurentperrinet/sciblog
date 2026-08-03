.. title: scripting MoinMoin to get, change or rename pages
.. slug: 2011-07-06-scripting-MoinMoin-to-get-change-or-rename-pages
.. date: 2011-07-06 13:36:57
.. type: text
.. tags: moinmoin, sciblog


-  MoinMoin is hugely useful for day to day use. Scripting is even
   better. Here, I show how to get, edit and rename pages on your wiki.
   To avoid bad surprise, this is based on a copy of the remote server
   using a local server with a ``wikiconfig.py`` script.


.. TEASER_END

-  it heavily uses examples shown in
   `http://moinmo.in/MoinAPI/Examples?highlight=%28xmlrpc%29 <http://moinmo.in/MoinAPI/Examples?highlight=%28xmlrpc%29>`__
-  first define the server and import the library

   ::

          1 wikiurl = "http://localhost:8080"
          2 username, password = 'YourName', 'yur)s3cr3t-pwd'
          3
          4 import xmlrpclib

-  let's try to read a page

   ::

          1     pagename = u'NewsEvents' # not protected
          2     pagename = u'Publications/Perrinet06ciotat' # protected
          3     homewiki = xmlrpclib.ServerProxy(wikiurl + "?action=xmlrpc2", allow_none=True)
          4     auth_token = homewiki.getAuthToken(username, password)
          5     mc = xmlrpclib.MultiCall(homewiki)
          6     mc.applyAuthToken(auth_token)
          7     mc.getPage(pagename)
          8     result = mc()
          9     success, raw = tuple(result)
         10     if isinstance(result, tuple) and tuple(result)[0] == "SUCCESS":
         11         print "reading page '%s' : %s" % (pagename, tuple(result)[0])
         12     else:
         13         print tuple(result)[0]

-  and now to write another one

   ::

          1     pagename = u'TestingPage'
          2     text = """
          3     This is a line of TEXT
          4
          5 AND     This is another line of text
          6
          7     """
          8     homewiki = xmlrpclib.ServerProxy(wikiurl + "?action=xmlrpc2", allow_none=True)
          9     auth_token = homewiki.getAuthToken(username, password)
         10     mc = xmlrpclib.MultiCall(homewiki)
         11     mc.applyAuthToken(auth_token)
         12     mc.putPage(pagename, text)
         13     result = mc()
         14     if isinstance(result, tuple) and tuple(result)[0] == "SUCCESS":
         15         print "page '%s' created: %s" % (pagename, tuple(result)[0])
         16     else:
         17         print 'You did not change the page content, not saved!'

-  so we may now read a page, replace some text and write it

   ::

          1     old, new = 'Category', 'Tag'
          2
          3     homewiki = xmlrpclib.ServerProxy(wikiurl + "?action=xmlrpc2", allow_none=True)
          4     auth_token = homewiki.getAuthToken(username, password)
          5     mc = xmlrpclib.MultiCall(homewiki)
          6     mc.applyAuthToken(auth_token)
          7     mc.getPage(pagename)
          8     result = mc()
          9     if tuple(result)[0] == "SUCCESS":
         10         print "page '%s' to modify: %s" % (pagename, tuple(result)[0])
         11         raw = tuple(result)[1]
         12         if raw.find(old)>-1:
         13             raw = raw.replace(old, new)
         14 #            print raw
         15             mc.putPage(pagename, raw)
         16             result = mc()
         17             print result[0]
         18         else:
         19             print 'not modified'
         20     else:
         21         print tuple(result)[0]

-  let's now do that on the whole website

   ::

          1     old, new = '^= reference =$', '^== reference ==$'
          2     homewiki = xmlrpclib.ServerProxy(wikiurl + "?action=xmlrpc2", allow_none=True)
          3     auth_token = homewiki.getAuthToken(username, password)
          4     mc = xmlrpclib.MultiCall(homewiki)
          5     mc.applyAuthToken(auth_token)
          6     mc.getAllPages()#opts={'include_system':False, 'include_underlay':False})
          7     result = mc()
          8     pagelist = tuple(result)[1]
          9     for pagename in pagelist:
         10         homewiki = xmlrpclib.ServerProxy(wikiurl + "?action=xmlrpc2", allow_none=True)
         11         auth_token = homewiki.getAuthToken(username, password)
         12         mc = xmlrpclib.MultiCall(homewiki)
         13         mc.applyAuthToken(auth_token)
         14         mc.getPage(pagename)
         15         try:
         16             result = mc()
         17             if tuple(result)[0] == "SUCCESS":
         18                 raw = tuple(result)[1]
         19                 if raw.find(old)>-1:
         20                     raw = raw.replace(old, new)
         21                     mc.applyAuthToken(auth_token)
         22                     mc.putPage(pagename, raw)
         23                     result = mc()
         24                     print ":-) page '%s' modified: %s" % (pagename, tuple(result)[0])
         25             else:
         26                 print tuple(result)[0]
         27         except:
         28             print 'failed', pagename

-  let's now rename one page

   ::

          1     homewiki = xmlrpclib.ServerProxy(wikiurl + "?action=xmlrpc2", allow_none=True)
          2     auth_token = homewiki.getAuthToken(username, password)
          3     mc = xmlrpclib.MultiCall(homewiki)
          4     mc.applyAuthToken(auth_token)
          5     mc.renamePage(u'TestingPage', u'TestPage2')
          6     result = mc()
          7     print result[0]

-  and now some more pages (here to reflect changes in the links)

   ::

          1     homewiki = xmlrpclib.ServerProxy(wikiurl + "?action=xmlrpc2", allow_none=True)
          2     auth_token = homewiki.getAuthToken(username, password)
          3     mc = xmlrpclib.MultiCall(homewiki)
          4     old, new = 'Category', 'Tag'
          5     for pagename in homewiki.getAllPages():
          6         if pagename.find(old)>-1:
          7             mc = xmlrpclib.MultiCall(homewiki)
          8             mc.applyAuthToken(auth_token)
          9             mc.renamePage(pagename, pagename.replace(old, new))
         10             result = mc()
         11             print ":-) page '%s' modified: %s" % (pagename, tuple(result)[0])
