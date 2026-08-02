.. title: latex within moinmoin
.. slug: 2010-07-08-latex-within-moinmoin
.. date: 2010-07-08 13:36:57
.. type: text
.. tags: moinmoin, sciblog, latex

-  installation d'après
   `http://johannes.sipsolutions.net/Projects/new-moinmoin-latex <http://johannes.sipsolutions.net/Projects/new-moinmoin-latex>`__
-  pour s'adapter à ma distribution pdflatex, j'ai changé

   ::

          1 # last arg must have %s in it!
          2 latex_args = ("--interaction=nonstopmode -output-format dvi", "%s.tex")

   dans le parser
   ``sudo open -e  ~/WebSites/moin/data/plugin/parser/latex.py``)


.. TEASER_END
.. warning::

  This post is certainly obsolete...

examples
~~~~~~~~

This is a red square:

::

    \usepackage{graphics,color}

    %%end-prologue%%
    \newsavebox{\mysquare}
    \savebox{\mysquare}{\textcolor{red}{\rule{1in}{1in} } }
    \usebox{\mysquare}

symboles

::

    % Math-mode symbol & verbatim
    \def\W#1#2{$#1{#2}$ &\tt\string#1\string{#2\string}}
    \def\X#1{$#1$ &\tt\string#1}
    \def\Y#1{$\big#1$ &\tt\string#1}
    \def\Z#1{\tt\string#1}

    % A non-floating table environment.
    \makeatletter
    \renewenvironment{table}%
       {\vskip\intextsep\parskip\z@
        \vbox\bgroup\centering\def\@captype{table}}%
       {\egroup\vskip\intextsep}
    \makeatother

    % All the tables are \label'ed in case this document ever gets some
    % explanatory text written, however there are no \refs as yet. To save
    % LaTeX-ing the file twice we go:
    \renewcommand{\label}[1]{}

    %%end-prologue%%
    \begin{table}
    \begin{tabular}{*8l}
    \X\alpha        &\X\theta       &\X o           &\X\tau         \\
    \X\beta         &\X\vartheta    &\X\pi          &\X\upsilon     \\
    \X\gamma        &\X\gamma       &\X\varpi       &\X\phi         \\
    \X\delta        &\X\kappa       &\X\rho         &\X\varphi      \\
    \X\epsilon      &\X\lambda      &\X\varrho      &\X\chi         \\
    \X\varepsilon   &\X\mu          &\X\sigma       &\X\psi         \\
    \X\zeta         &\X\nu          &\X\varsigma    &\X\omega       \\
    \X\eta          &\X\xi                                          \\
                                                                    \\
    \X\Gamma        &\X\Lambda      &\X\Sigma       &\X\Psi         \\
    \X\Delta        &\X\Xi          &\X\Upsilon     &\X\Omega       \\
    \X\Theta        &\X\Pi          &\X\Phi
    \end{tabular}
    \caption{Greek Letters}\label{greek}
    \end{table}

ou

::

    \begin{equation}
    x^3 =\int_{0}^{\infty} f(x,y) dy
    \end{equation}

-  et encore

   ::

       $$x^3 =\int_{0}^{\infty} f(x,y) dy + c$$

inline
~~~~~~

Because people requested an easier way to enter latex, I've added the
possibility to write $ ... $ to obtain inline formulas. This is
equivalent to writing ``\$ ...\$`` and has the same
single-line limitation (but everything else isn't really useful in
formulas anyway). In order to do this, install the ``inline\_latex.py``
parser add #format ``inline\_latex to your page (alternatively, configure
the default parser to be ``inline\_latex``). This parser accepts all regular
wiki syntax, but additionally the `\$ ... \$' syntax. Additionally, the
``inline\_latex`` formatter supports `\$\$....\$\$` style formulas (still limited
to a single line though!) which puts the formula into a paragraph on its
own.

Note: in the nikola blog, this is directly accomplished by using ReST :  ``\$\\lambda\$`` = $\lambda$
