.. title: homebrew cask : updating an existing cask
.. slug: 2015-02-16-homebrew-cask-updating-a-cask
.. date: 2015-02-16 13:36:57
.. type: text
.. tags: macos, sciblog, homebrew

- A new version of owncloud is out, I will try today to push that new infomation to http://caskroom.io/

- I will base things on :doc:`my contribution <2014-11-12-homebrew-cask-updating-a-cask>`

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
       git checkout $project

- finding my information

   ::

       cd /tmp
       wget https://download.owncloud.com/desktop/stable/ownCloud-1.7.1.1655.pkg
       sha256sum ownCloud-1.7.1.1655.pkg
       sha256sum ownCloud-1.7.1.1655.pkg | pbcopy
       brew cask edit owncloud
       brew cask install owncloud
       brew cask audit $project  --download

-  publishing results

   ::

       git status
       git commit -am"upgrading owncloud"
       git push $github_user $project

-  confirm the pull request

   ::

       open https://github.com/$github_user/homebrew-cask

-  come back to the ``master`` branch

   ::

       git checkout master

-  in the meanwhile, I will wait till the change has been
   `merged <https://github.com/caskroom/homebrew-cask/pull/9613>`__
   and gets approval such that owncloud is updated!

