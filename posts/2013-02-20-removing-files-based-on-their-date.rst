.. title: removing files based on their date
.. slug: 2013-02-20-removing-files-based-on-their-date
.. date: 2013/02/20 16:18:42
.. tags: find, oss
.. link:
.. description:
.. type: text


Everything (almost) can be done by the ``find`` command:

 * finding in the current directory (``.``) all files containing a ``lock`` pattern::

    find . -name *lock*


.. TEASER_END


 * displaying more information by piping to ``ls -l``::

    find . -name *lock*  -exec ls -l {} \;

 * filtering files that were changed just from now to one day ago::

    find . -name *lock*  -mtime 0 -exec ls -l {} \;

 * filtering files that were changed just from now to 5 hours ago::

    find . -name *lock*  -mmin 300 -exec ls -l {} \;

 * filtering files that are at least 5 hours old (not just from now to 5 hours ago)::

    find . -name *lock* `-not -mmin 300 -exec ls -l {} \;

 * removing of ``lock`` files older than 5 hours::

    find . -name *lock*  -not -mmin 300 -exec  rm -f {} \;
