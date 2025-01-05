.. title: managing defaults on MacOsX
.. slug: 2012-04-05-managing-defaults-on-MacOsX
.. date: 2012-04-05 13:36:57
.. type: text
.. tags: sciblog


-  when managing multiple machines, it is sometimes a pain to reset all
   default parameters. Still you want the same behaviour everywhere...




.. TEASER_END
.. warning::

  This post is certainly obsolete...


-  this repository
   `https://github.com/mathiasbynens/dotfiles/blob/master/.osx <https://github.com/mathiasbynens/dotfiles/blob/master/.osx>`__
   display a large number of useful comands for your mac :

   ::

       # Always show scrollbars
       defaults write NSGlobalDomain AppleShowScrollBars -string "Always"

       # Enable full keyboard access for all controls (e.g. enable Tab in modal dialogs)
       defaults write NSGlobalDomain AppleKeyboardUIMode -int 3

       # Enable subpixel font rendering on non-Apple LCDs
       defaults write NSGlobalDomain AppleFontSmoothing -int 2

       # Enable the 2D Dock
       defaults write com.apple.dock no-glass -bool true

       # Automatically hide and show the Dock
       defaults write com.apple.dock autohide -bool true

       # Make Dock icons of hidden applications translucent
       defaults write com.apple.dock showhidden -bool true

       # Enable iTunes track notifications in the Dock
       defaults write com.apple.dock itunes-notifications -bool true

       # Show all filename extensions in Finder
       defaults write NSGlobalDomain AppleShowAllExtensions -bool true

       # Show status bar in Finder
       defaults write com.apple.finder ShowStatusBar -bool true

       # Expand save panel by default
       defaults write NSGlobalDomain NSNavPanelExpandedStateForSaveMode -bool true

       # Expand print panel by default
       defaults write NSGlobalDomain PMPrintingExpandedStateForPrint -bool true

       # Disable the “Are you sure you want to open this application?” dialog
       defaults write com.apple.LaunchServices LSQuarantine -bool false

       # Disable shadow in screenshots
       defaults write com.apple.screencapture disable-shadow -bool true


       # Display full POSIX path as Finder window title
       defaults write com.apple.finder _FXShowPosixPathInTitle -bool true

       # Increase window resize speed for Cocoa applications
       defaults write NSGlobalDomain NSWindowResizeTime -float 0.001

       # Avoid creating .DS_Store files on network volumes
       defaults write com.apple.desktopservices DSDontWriteNetworkStores -bool true


       # Disable send and reply animations in Mail.app
       defaults write com.apple.Mail DisableReplyAnimations -bool true
       defaults write com.apple.Mail DisableSendAnimations -bool true

       # Copy email addresses as `foo@example.com` instead of `Foo Bar <foo@example.com>` in Mail.app
       defaults write com.apple.mail AddressesIncludeNameOnPasteboard -bool false

       # Disable Resume system-wide
       defaults write NSGlobalDomain NSQuitAlwaysKeepsWindows -bool false

-  there is much more on

   ::

       git clone https://github.com/mathiasbynens/dotfiles.git && cd dotfiles && ./bootstrap.sh

-  TODO: make default changes for a french keyboard
