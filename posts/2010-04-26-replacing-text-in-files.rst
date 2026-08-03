.. title: replacing text in files
.. slug: 2010-04-26-replacing-text-in-files
.. date: 2010-04-26 13:36:57
.. type: text
.. tags: sciblog


using sed
---------

-  The UNIX command sed is useful to find and replace text in single or
   multiple files. This page lists some common commands in using ``sed``
   to improve editing code.

   .. TEASER_END

-  To replace foo with foo\_bar in a single file:

   ::

       sed -i 's/foo/foo_bar/g' my_script.py

   -  -i = edit the file "in-place": sed will directly modify the file
      if it finds anything to replace
   -  s = substitute the following text
   -  foo = the text string to be substituted
   -  foo\_bar = the replacement string
   -  g = global, match all occurrences in the line

-  To replace foo with foo\_bar in multiple files:

   ::

       sed -i 's/foo/foo_bar/g'  *.py

-  Consult the manual pages of the operating system that you use:
   ``man sed``
-  in the particular case of changing a scaling parameter in a set of
   experiment files:

   ::

       sed -i 's/size = 6/size = 7/g'  experiment*.py
       sed -i 's/size = 7/size = 6/g'  experiment*.py

using vim
---------

-  on the current buffer, with confirmation

   ::

       :%s/old_text/new_text/cg

-  on the current buffer

   ::

       :%s/old_text/new_text/g

-  to get help

   ::

           :help substitute

-  one could pass the required files to 'args' and apply whatever
   command to all these files using the command 'argdo'. First I will
   apply the substitute 's' command and then 'update' which will only
   save the modified files.

   ::

           :args *.py
           :argdo :%s/old_text/new_text/g | update

using python
------------

-  `http://muharem.wordpress.com/2007/05/20/python-find-files-using-unix-shell-style-wildcards/ <http://muharem.wordpress.com/2007/05/20/python-find-files-using-unix-shell-style-wildcards/>`__
