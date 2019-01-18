.. title: Vim commands for moving around
.. slug: 2014-05-15-vim-moving-around.rst
.. date: 2014/05/15 11:20:10 UTC+02:00
.. tags: vim
.. link: 
.. description: 
.. type: text

Basics commands in Vim
======================

Sometimes, it's good to go back to the basics.

In command mode, typing ``:help usr_02.txt`` (or simplier something like ``:h usr_<TAB>02<TAB><ENTER>``), you learn the letters for navigating a file:

* these letters are ``HJKL`` - glad it works on an international keyboard.
* letters on the borders (``HL``) are for horizontal movements- obviously ``H`` for left, ``L`` for right
* letters on the inside are for vertical movements - ``J`` for down, ``K`` for up; a nice feature is that these keys are now quite widely used in the community, take for example in the gmail interface when switching to the next message.

I was still using the arrows keys, but taking this habit makes thinks easier, especially when switching often keyboards.

Simalarly, to scroll the text - you can use:

* ``<CTRL-U>`` to scroll a half-page up
* ``<CTRL-D>`` to scroll a half-page down

Here, the ``:h ctrl-u`` page will give you more info (or ``:help usr_03.txt``).

Note that to follow a link (think "searching a tag"), you can press `*` (or `#` to go backwards).
