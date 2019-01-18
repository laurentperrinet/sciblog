.. title: homebrew cask (level 1): correcting a pull request
.. slug: 2013-11-09-homebrew-cask-(level-1)-correcting-a-pull-request
.. date: 2013-11-09 13:36:57
.. type: text
.. tags: homebrew, macos, sciblog


-  I mistyped :doc:`my contribution <2013-11-08-homebrew-cask-(level-0)-contributing-a-new-cask>`,
   so I have to modify my pull request
-  set-up variables

   ::

       cd $(brew --prefix)/Library/Taps/phinze-cask
       github_user='meduz'
       project='texshop'
       git remote -v

.. TEASER_END

-  jumping to my branch

   ::

       git branches
       git checkout remotes/origin/$project -b $project
       vim Casks/texshop.rb

-  publishing results

   ::

       git status
       git commit -v
       git push $github_user $project

-  confirm the pull request

   ::

       open https://github.com/$github_user/homebrew-cask

-  come back to the ``master`` branch

   ::

       git checkout master

-  in the meanwhile, the change has been
   `merged <https://github.com/phinze/homebrew-cask/commit/6205e80f4403b2c99ad55ddb2b2c92402b3a883c>`__
   and texshop is now available as a cask!



