.. title: homebrew cask : creating a new cask
.. slug: 2016-11-04-homebrew-cask-creating-a-cask
.. date: 2016-11-04 09:36:57
.. type: text
.. tags: macos, sciblog, homebrew

A new version of https://nteract.io/ is out, I will try today to push that new infomation to http://caskroom.io/ by creating a new cask for this application.  I will base things on this :doc:`previous contribution <2015-12-08-homebrew-cask-updating-a-cask>` where I was simply editing an existing cask.

- getting the token

    ::

        "$(brew --repository)/Library/Taps/caskroom/homebrew-cask/developer/bin/generate_cask_token" '/Applications/nteract.app'

- set-up variables

   ::

       cd "$(brew --prefix)"/Homebrew/Library/Taps/caskroom/homebrew-cask
       github_user='laurentperrinet'
       project='nteract'
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
       wget https://github.com/nteract/nteract/releases/download/v0.0.14/nteract-0.0.14.dmg
       sha256sum nteract-0.0.14.dmg | pbcopy
       appcast_url='https://github.com/nteract/nteract/releases.atom'
       curl --compressed --location --user-agent 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.152 Safari/537.36' "{{appcast_url}}" | /usr/bin/sed 's|<pubDate>[^<]*</pubDate>||g' | shasum --algorithm 256
       brew cask edit $project

- testing with homebrew:

   ::

       brew cask install $project
       brew cask audit $project  --download

-  publishing results

   ::

       git status
       git add Casks/"$project".rb
       git commit -am"adding nteract v0.0.14"
       git push $github_user $project

-  confirm the pull request

   ::

       open https://github.com/$github_user/homebrew-cask

-  come back to the ``master`` branch

   ::

       git checkout master

-  in the meanwhile, the change has been
   `merged <https://github.com/caskroom/homebrew-cask/pull/26400>`__

- such that now you can simply install nteract using

   ::

       brew cask install nteract

Happy hacking!
