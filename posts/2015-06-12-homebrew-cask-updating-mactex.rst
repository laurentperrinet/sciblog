.. title: homebrew cask : updating mactex
.. slug: 2015-06-12-homebrew-cask-updating-mactex
.. date: 2015-06-12 13:36:57
.. type: text
.. tags: macos, sciblog, homebrew

- A new version of (MacTex)[http://www.tug.org/mactex/mactex-download.html] is out, I will try today to push that new infomation to http://caskroom.io/

- I will base the steps I use on this :doc:`previous contribution <2015-03-17-homebrew-cask-updating-a-cask>`

- set-up variables

   ::

       cd $(brew --prefix)/Library/Taps/caskroom/homebrew-cask
       github_user='meduz'
       project='mactex'
       git remote -v

.. TEASER_END

-  creating a new branch for his project

   ::

       git branches
       git remote add $github_user https://github.com/$github_user/homebrew-cask
       git checkout -b $project

- finding my information and feeding to homebrew

   ::

       cd ~/Downloads
       wget http://mirrors.ircam.fr/pub/CTAN/systems/mac/mactex/mactex-20150609.pkg
       sha256sum mactex-20150609.pkg
       sha256sum mactex-20150609.pkg | pbcopy
       brew cask edit $project

- testing with homebrew:

   ::

       brew cask install $project
       brew cask audit $project  --download

-  publishing results

   ::

       git status
       git commit -am"upgrading mactex"
       git push $github_user $project

-  confirm the pull request

   ::

       open https://github.com/$github_user/homebrew-cask

-  come back to the ``master`` branch

   ::

       git checkout master

-  in the meanwhile, the change has been
   `pulled <https://github.com/caskroom/homebrew-cask/pull/11854>`__
   and got approveded. MacTex is updated!

