.. title: Completely disable quarantine of downloaded files
.. slug: 2010-10-15-Completely-disable-quarantine-of-downloaded-files
.. date: 2013-03-13 13:36:57
.. type: text
.. tags: macos, sciblog





Starting in Leopard (I believe) when you open a file downloaded from the web, OS X asks if you really mean it. While it is intended to stop maliciousness, it is only a source of aggravation for me. While there are some hints here on working around it, it turns out that you can disable it completely using a Terminal command:

    defaults write com.apple.LaunchServices LSQuarantine -bool NO

.. TEASER_END
.. warning::

  This post is certainly obsolete...


After that, reboot, and you should be set.
(this was inspired by http://hints.macworld.com/article.php?story=20091208050655947 )
