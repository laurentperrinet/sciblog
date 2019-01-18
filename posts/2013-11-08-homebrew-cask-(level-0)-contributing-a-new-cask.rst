.. title: homebrew cask (level 0): contributing a new cask
.. slug: 2013-11-08-homebrew-cask-(level-0)-contributing-a-new-cask
.. date: 2013-11-08 13:36:57
.. type: text
.. tags: homebrew, macos, sciblog


-  homebrew casks are `a friendly homebrew-style CLI workflow for the
   administration of Mac applications distributed as
   binaries <https://github.com/phinze/homebrew-cask>`__. Something I
   always needed, hoped to get with the app store, frowned when
   openoffice or vlc were absent, and here they are!
-  see my `list of casks I currently
   use <https://github.com/meduz/dotfiles/blob/master/init/osx_cask_base.sh>`__
   (it is also a script to install them)

.. TEASER_END

-  preparing by forking the

   ::

       cd $(brew --prefix)/Library/Taps/phinze-cask
       github_user='meduz'
       echo $github_user
       git remote add $github_user https://github.com/$github_user/homebrew-cask

.. TEASER_END

-  create, then install / edit cycle

   ::

       project='texshop'
       brew cask create $project
       brew cask install $project
       brew cask edit $project
       brew cask install $project
       brew cask audit $project  --download

-  publishing results

   ::

       git status
       git checkout -b $project
       git add Casks/$project.rb
       git commit -v
       git push $github_user $project

-  confirm the pull request

   ::

       open https://github.com/$github_user/homebrew-cask

-  result is
   `https://github.com/phinze/homebrew-cask/pull/1530 <https://github.com/phinze/homebrew-cask/pull/1530>`__
-  come back to the ``master`` branch

   ::

       git checkout master

-  this was easy! ... but wait, I  :doc:`mystyped <2013-11-09-homebrew-cask-(level-1)-correcting-a-pull-request>` something...
