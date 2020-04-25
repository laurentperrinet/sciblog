.. title: using tabs in vim
.. slug: 2013-03-25-using-tabs-in-vim
.. date: 2013-03-25 13:36:57
.. type: text
.. tags: info, sciblog


-  call vim to open more files

   ::

        vim -p file1 file2 file3


.. TEASER_END

-  or open one in your editing session

   ::

       :tabf <pattern>

   (will find the file corresponding to <pattern>)

-  to switch tab, use ``gt``
