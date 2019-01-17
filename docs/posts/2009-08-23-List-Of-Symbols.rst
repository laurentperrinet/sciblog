.. title: List Of Symbols
.. slug: 2009-08-23-List-Of-Symbols
.. date: 2009-08-23 13:36:57
.. type: text
.. tags: latex


symbols
-------

-  |(!)| Use `Detexify2 - LaTeX symbol
   classifier <http://detexify.kirelabs.org/classify.html>`__ to find
   out a particular symbol.

.. TEASER_END

-  list of symbols:
   `http://web.ift.uib.no/Fysisk/Teori/KURS/WRK/TeX/symALL.html <http://web.ift.uib.no/Fysisk/Teori/KURS/WRK/TeX/symALL.html>`__

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



    \begin{table}
    \begin{tabular}{*8l}
    \X\pm           &\X\cap         &\X\diamond             &\X\oplus     \\
    \X\mp           &\X\cup         &\X\bigtriangleup       &\X\ominus    \\
    \X\times        &\X\uplus       &\X\bigtriangledown     &\X\otimes    \\
    \X\div          &\X\sqcap       &\X\triangleleft        &\X\oslash    \\
    \X\ast          &\X\sqcup       &\X\triangleright       &\X\odot      \\
    \X\star         &\X\vee         &             &\X\bigcirc   \\
    \X\circ         &\X\wedge       &              &\X\dagger    \\
    \X\bullet       &\X\setminus    &            &\X\ddagger   \\
    \X\cdot         &\X\wr          &          &\X\amalg     \\
    \X+             &\X-
    \end{tabular}

    \caption{Binary Operation Symbols}\label{bin}
    \end{table}



    \begin{table}
    \begin{tabular}{*8l}
    \X\leq          &\X\geq         &\X\equiv       &\X\models      \\
    \X\prec         &\X\succ        &\X\sim         &\X\perp        \\
    \X\preceq       &\X\succeq      &\X\simeq       &\X\mid         \\
    \X\ll           &\X\gg          &\X\asymp       &\X\parallel    \\
    \X\subset       &\X\supset      &\X\approx      &\X\bowtie      \\
    \X\subseteq     &\X\supseteq    &\X\cong        &    \\
      & &\X\neq         &\X\smile       \\
    \X\sqsubseteq   &\X\sqsupseteq  &\X\doteq       &\X\frown       \\
    \X\in           &\X\ni          &\X\propto      &\X=            \\
    \X\vdash        &\X\dashv       &\X<            &\X>            \\
    \X:
    \end{tabular}

    \caption{Relation Symbols}\label{rel}
    \end{table}



.. |(!)| image:: http://invibe.net/moin_static196/moniker/img/idea.png
