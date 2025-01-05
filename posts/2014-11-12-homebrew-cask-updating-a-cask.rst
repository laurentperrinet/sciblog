.. title: homebrew cask : updating an existing cask
.. slug: 2014-11-12-homebrew-cask-updating-a-cask
.. date: 2014-11-12 13:36:57
.. type: text
.. tags: macos, sciblog, homebrew

- A new version of owncloud is out, I will try today to push that new infomation to http://caskroom.io/

- I will base things on :doc:`my contribution <2013-11-08-homebrew-cask-level-0-contributing-a-new-cask>`,
   though now `phinze-cask` paths are now `brew-cask`.

- set-up variables

   ::

       cd $(brew --prefix)/Library/Taps/caskroom/homebrew-cask
       github_user='meduz'
       project='owncloud'
       git remote -v

.. TEASER_END

-  creating a new branch for his project

   ::

       git branches
       git remote add $github_user https://github.com/$github_user/homebrew-cask
       git checkout remotes/origin/$project -b $project

- finding my information

   ::

       cd /tmp
       wget https://download.owncloud.com/desktop/stable/ownCloud-1.7.0.1339.pkg
       sha256sum ownCloud-1.7.0.1339.pkg
       brew cask edit owncloud
       brew cask install owncloud
       brew cask audit $project  --download

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
   `merged <https://github.com/caskroom/homebrew-cask/pull/7278>`__
   and (after some corrections) got approval: owncloud is now updated!



