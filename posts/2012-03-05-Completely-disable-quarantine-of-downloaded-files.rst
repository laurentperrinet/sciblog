.. title: Completely disable quarantine of downloaded files
.. slug: 2012-03-05-Completely-disable-quarantine-of-downloaded-files
.. date: 2012-03-05 13:36:57
.. type: text
.. tags: macos, sciblog


+---------------------------------------------------------------------------------------------------------------------------------------------------------+
| copy and paste from `http://hints.macworld.com/article.php?story=20091208050655947 <http://hints.macworld.com/article.php?story=20091208050655947>`__   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------+

Starting in Leopard when you open a file downloaded from the web, OS X
asks if you really mean it. While it is intended to stop maliciousness,
it is only a source of aggravation for me. While there are some hints
here on working around it, it turns out that you can disable it
completely using a Terminal command:


.. TEASER_END
.. warning::

  This post is certainly obsolete...



::

    defaults write com.apple.LaunchServices LSQuarantine -bool NO

After that, reboot.

To know the state of your system, use

::

    defaults read com.apple.LaunchServices LSQuarantine

, to go back to default, use

::

    defaults write com.apple.LaunchServices LSQuarantine -bool YES
