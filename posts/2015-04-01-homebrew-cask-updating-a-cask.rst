.. title: homebrew cask : updating an existing cask
.. slug: 2015-04-01-homebrew-cask-updating-a-cask
.. date: 2015-04-01 13:36:57
.. type: text
.. tags: macos, sciblog, homebrew

- A new version of psychopy is out, I will try today to push that new infomation to http://caskroom.io/

- I will base things on this :doc:`previous contribution <2014-11-12-homebrew-cask-updating-a-cask>`

- set-up variables

   ::

       cd $(brew --prefix)/Library/Taps/caskroom/homebrew-cask
       github_user='meduz'
       project='psychopy'
       git remote -v

.. TEASER_END

-  creating a new branch for his project

   ::

       git branches
       git remote add $github_user https://github.com/$github_user/homebrew-cask
       git checkout -b $project

- finding my information and feeding to homebrew

   ::

       cd /tmp
       wget "http://downloads.sourceforge.net/project/psychpy/PsychoPy/StandalonePsychoPy-1.82.00-OSX.dmg?r=http%3A%2F%2Fsourceforge.net%2Fprojects%2Fpsychpy%2F%3Fsource%3Dtyp_redirect&ts=1427881364&use_mirror=freefr"
       sha256sum StandalonePsychoPy-1.82.00-OSX.dmg
       sha256sum StandalonePsychoPy-1.82.00-OSX.dmg | pbcopy
       brew cask edit $project

- testing with homebrew:

   ::

       brew cask install $project
       brew cask audit $project  --download

-  publishing results

   ::

       git status
       git commit -am"upgrading psychopy"
       git push $github_user $project

-  confirm the pull request

   ::

       open https://github.com/$github_user/homebrew-cask

-  come back to the ``master`` branch

   ::

       git checkout master

-  in the meanwhile, the change has been
   `merged <https://github.com/caskroom/homebrew-cask/pull/10354>`__
   and got approveded. Psychopy is updated!

