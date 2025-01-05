.. title: using a versioning system
.. slug: 2011-07-07-using-a-versioning-system
.. date: 2011-07-07 13:36:57
.. type: text
.. tags: macos, sciblog



.. TEASER_END
.. warning::

  This post is certainly obsolete...



using SubVersion (SVN)
----------------------


.. TEASER_END


`Version Control <http://software-carpentry.org/version.html>`__ is an
everyday tool to handle your important source files. It is useful:

-  to grab the latest source code from open source projects and to
   always keep up-to-date,
-  to share a bunch of files (a set of latex source code, python
   scripts, ...) allowing to work on different computers with different
   persons,
-  to keep track of revisions from your project.

SVN: Getting help
~~~~~~~~~~~~~~~~~

-  Versions are kept in a central repository (the **SVN server**) while
   you work with local **working copies** using your SVN client.
-  Help for svn can be found in the big `svn
   book <http://svnbook.red-bean.com/nightly/en/index.html>`__. Other
   ressources:

   -  cf.
      `http://svnbook.red-bean.com/nightly/en/svn-book.html <http://svnbook.red-bean.com/nightly/en/svn-book.html>`__
   -  `http://www.sujee.net/geeky/svn.html <http://www.sujee.net/geeky/svn.html>`__
   -  `http://www.abbeyworkshop.com/howto/misc/svn01/ <http://www.abbeyworkshop.com/howto/misc/svn01/>`__

-  Many solutions exist to integrate SVN to your file manager

   -  On MacOsX, integrate SVN to the
      ``Finder.app`` using `SCPlugin <http://scplugin.tigris.org/>`__

SVN: 2 minutes guide using the commandline
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  to just access a remote repository and make a local working copy
   ("checking-out") in a local ``my_projects`` folder, do

   ::

       cd my_projects/
       svn checkout svn+ssh://myname@svnserver/path/to/svn/project my_localcopy

   this basically copies the current version of the remote copy to your
   local computer as the folder ``my_localcopy``. Then, you just need to
   issue ``svn up`` in this folder to stay up-to-date.

-  to create from scratch your own folder in an existing repository (,
   do

   ::

       cd my_projects/
       svn add new_project
       svn ci new_project -m'Committing my modifications'

   . Then you just need to issue the
   ``svn ci new_project -m'Committing my modifications'`` command to
   commit new modifications to the server. Don't forget to
   ``svn add newfiles`` or to ``svn rm obsolete_files``.

random SVN tips
~~~~~~~~~~~~~~~

-  roll-back to a previous version (e.g. 3421) of a file ``myfile``:

   ::

       svn up -r 3421 myfile

-  Create a repository

   -  use the database backend

      ::

              svnadmin create /ih/funk/svn/projects

-  use the filesystem backend

   ::

          svnadmin create --fs-type=fsfs PATH

-  Import a revision

   ::

        svn import -m "Initial import" Eccos file:///ih/funk/svn/projects

-  Check out a revision

   ::

        svn co file:///ih/funk/svn/projects

-  Dump a repository

   ::

        svnadmin dump /ih/funk/svn/projects | gzip -9 > dump.gz
        svnadmin dump /ih/funk/svn/projects | gzip -9 > `date "+Eccosdump%Y-%m-%d_%H:%M:%S.gz"`
       svnadmin dump /ih/funk/svn/projects | gzip -9 > `date "+projects_dump%Y-%m-%d_%H:%M:%S.gz"`

-  Load contents of a dump into a repository

   ::

        gunzip -c dump.gz | svnadmin load /data/svn/projects

-  Import from an existing directory, no need to check it out again

   -  It should work, but you could also check it out right into /etc.
      Something

      like this:

      ::

            $ svnadmin create /var/svnrepos/admin
            $ svn mkdir -m "initial setup" file:///var/svnrepos/admin/trunk
            c:> svn mkdir -m "initial setup" file:///c:/fhs/svn_repos/trunk
            $ cd /etc
            $ svn co file:///var/svnrepos/admin/trunk .
            $ svn add passwd group
            $ svn commit -m "start loading it in"

            I tested the 'svn co' into '.' just now. Works great.

-  svn propset

   ::

         svn propset svn:keywords "LastChangedDate LastChangedRevision Id Author" weather.txt
         svn propset svn:keywords "LastChangedDate LastChangedRevision Id" slides.tex

-  Before an update you could use the following to get the log messages
   of the changes:

   ::

        svn log -rBASE:HEAD

-  Upgrade to a new subversion version

   ::

        $ mv repos repos.tmp
        $ svnadmin create repos
        $ svnadmin-old dump repos.tmp | svnadmin load repos
        $ # copy over any hook scripts and stuff from repos.tmp to repos

-  Checkout from a repository over ssh

   ::

         svn co svn+ssh://felix/home/reichr/svn_repos/XSteveData/trunk data

-  Change the path of the repository for a working copy

   ::

        svn switch --relocate file:///original/path/to/repos file:///new/path

   WARNING: this will not work if
   ``file:///original/path/to/repos`` is not *exactly* the original URL.
   BE sure to check before with ``svn info``.

-  Network a repository via svn+ssh:

   -  create the repository on the repository host:

      ::

             svnadmin create rp1  -- this is located at /home/svtest/rp1

   -  Import data to the repository:

      ::

             svn import -m"Initial import" svn+ssh://svtest@host/rp1/trunk

   -  Checkout the project:

      ::

             svn co svn+ssh://svtest@host/home/svtest/rp1/trunk p1

-  Generate a patch to undo some local changes and redo them later: What
   usually happens to me is that I've changed N files in M different >
   directories distributed all over the filesystem, and I want to check
   in N-1 of them. If I need to commit all but one file, I do this:

   ::

         % svn diff path/to/file_not_committing > /tmp/patch.txt
         % svn revert path/to/file_not_committing
         % svn ci -m "committing all the stuff i wanted to"
         % patch -p0 < /tmp/patch.txt

   Revert is your friend. Learn it, use it, looooooooooove it.

-  Revert to a previous version

   ::

         svn co project
         <edit foo.c, adding bugs>
         svn ci foo.c (commits to r348)
         <realize terrible error>
         svn merge -r348:347 foo.c
         svn ci foo.c (commits 349)

   note the ordering of the revision numbers in the merge command. what
   this really says is "make a diff between revision 348 and 347, and
   apply it immediately to foo.c" if you are trying to revert a
   directory tree with moves or deletes in it, and are getting arcane
   errors, try the --ignore-ancestry flag.

-  Edit the commit/log messages after the commit Read chapter 7,
   regarding unversioned properties attached to revisions. You want to
   change the svn:log property:

   ::

         $ svn propedit -r N --revprop svn:log URL

an alternative : Git
--------------------

-  The place to
   `begin <http://www.kernel.org/pub/software/scm/git/docs/gittutorial.html>`__.
-  From the SVN world:
   `http://git-scm.com/course/svn.html <http://git-scm.com/course/svn.html>`__
-  `Everyday <http://www.kernel.org/pub/software/scm/git/docs/everyday.html>`__'s
   git.

+-------------------+-----------------------+
| git clone *url*   | svn checkout *url*    |
+-------------------+-----------------------+
| git pull          | svn up                |
+-------------------+-----------------------+
| git commit        | svn commit            |
+-------------------+-----------------------+
| git push *url*    | *(no such a thing)*   |
+-------------------+-----------------------+

-  to set-up

   ::

       git config --global user.name "Your Name Comes Here"
       git config --global user.email you@yourdomain.example.com
       git config --global color.diff auto
       git config --global color.status auto
       git config --global color.branch auto

using Git with SVN
------------------

-  install git-svn and use

   ::

       git svn fetch
