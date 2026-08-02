.. title: Vim folding commands
.. slug: 2014-01-15-vim-folding-commands
.. date: 2014/01/15 11:20:10 UTC+02:00
.. tags: vim, python, latex
.. link:
.. description:
.. type: text

Using folds in Vim
==================

Folds are useful when having long files to have a good perspective on its
structure. Especially useful in LaTeX mode.

To install, I recommend using the ``python-mode`` described in http://unlogic.co.uk/2013/02/08/vim-as-a-python-ide/

The magical shortcut all begin with ``z``. Type ``:hep fold`` to learn more about
them.

.. TEASER_END

These are the most common shortcuts in my personal order of preference.

* ``zo`` opens a fold at the cursor.
* ``zc`` closes a fold at the cursor.
* ``zM`` closes all open folds.
* ``zO`` opens all folds at the cursor.
* ``[z`` move to start of open fold.
* ``]z`` move to end of open fold.
* ``zj`` moves the cursor to the next fold.
* ``zk`` moves the cursor to the previous fold.
* ``zf#j`` creates a fold from the cursor down # lines.
* ``zf/string`` creates a fold from the cursor to string .
* ``zm`` increases the foldlevel by one.
* ``zr`` decreases the foldlevel by one.
* ``zR`` decreases the foldlevel to zero -- all folds will be open.
* ``zd`` deletes the fold at the cursor.
* ``zE`` deletes all folds.
