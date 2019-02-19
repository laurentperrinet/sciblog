.. title: Master M2 Sciences
.. slug: 2010-10-20-Master-M2-Sciences
.. date: 2010-10-20 13:36:57
.. type: text
.. tags: talks, computationalneuroscience, sciblog

.. TEASER_END

=========================================================================
Neurosciences Computationelles : émergence dans des réseaux d'information
=========================================================================

|http://2010.neurocomp.fr/images/neurocomplog.png|

Laurent Perrinet

+---------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| |https://crac.dsi.cnrs.fr/image/logo_cnrs.gif|    | Laurent Perrinet - Team `InViBe </LaurentPerrinet/InViBe>`__, `Institut de Neurosciences de la Timone <http://www.int.univ-amu.fr/PERRINET-Laurent>`__ (UMR 7289)   |
|                                                   |  CNRS - Aix-Marseille Université                                                                                                                                    |
|                                                   |  *Researcher*                                                                                                                                                       |
|                                                   |  `https://invibe.net/LaurentPerrinet <https://invibe.net/LaurentPerrinet>`__                                                                                          |
+---------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+




Les Neurosciences Computationelles étudient l'émergence dans les réseaux
neuronaux (structure) des fonctions cognitives (fonction). Durant ce
cours, nous allons définir ce paradigme de façon générique avant de
l'appliquer à trois cas particuliers. D'abord nous allons étudier un
exemple de réseau de type Bayesien appliqué à la détection du mouvement
visuel. Ensuite, nous étudierons un exemple de réseau de neurones
abstraits appliqué au codage adaptatif d'images. Enfin, l'étude de
différents types de connectivité dans des réseaux de neurones
impulsionnels réalistes.


Plan du cours
-------------

#. `Neurosciences
   computationnelles? </LaurentPerrinet/Presentations/10-10-20_M2_MasterSciences/017_Emergence>`__
#. `Une première application fonctionnelle: détection du mouvement
   utilisant des modèles
   probabilistes. </LaurentPerrinet/Presentations/10-10-20_M2_MasterSciences/035_MotionPerception>`__
#. `Réseaux optimaux pour le calcul de la représentation d'une
   image </LaurentPerrinet/Presentations/10-10-20_M2_MasterSciences/060_SparseCoding>`__
#. `Vers des implantations
   neurales... </LaurentPerrinet/Presentations/10-10-20_M2_MasterSciences/070_NeuralCoding>`__

Le cerveau est-elle une machine de Turing ?
===========================================

|http://www.ecs.syr.edu/faculty/fawcett/handouts/webpages/pictures/turingMachine.gif|

Le Système Nerveux Central: quelques chiffres
---------------------------------------------

-  Cerveau = 100 milliards de neurones (cerveau humain)
-  2% du poids, 20% de la consommation énergétique (5W)
-  1mm^3 = 90 000 neurones / 700.000.000 synapses / 4 km d’axone / 0,5
   km de dendrites

|http://upload.wikimedia.org/wikipedia/commons/c/c2/SnowflakesWilsonBentley.jpg|

Émergence dans des réseaux d'information
----------------------------------------

-  Approche classique: réductionisme , atomisme
-  *computere*
-  émergence ( `{en} <http://en.wikipedia.org/wiki/Emergence>`__
   `{fr} <http://fr.wikipedia.org/wiki/Emergence>`__ )

Neurosciences Computationelles?
===============================

|http://parasol.tamu.edu/~neilien/research/neurons.jpg|

-  Les **Neurosciences Computationelles** étudient l'émergence dans les
   *réseaux neuronaux* (structure) des *fonctions cognitives* (fonction)
   en termes de *traitement d'information* (méthode).

   |alert| ne pas confondre Neurosciences Computationelles et
   NeuroInformatique !

-  convergence interdisciplinaire de :

   -  neurosciences (physiologie, psychophysique)
   -  mathématiques (EDP, physique statistique, probabilités et
      statistiques, calcul stochastique, théorie des graphes, physique
      statistique, ...)
   -  informatique (théorie de l'information, théorie computationnelle,
      simulation de modèles)

-  applications à la compréhension de la biologie, à répondre aux
   pathologies + création de nouveaux paradigmes computationnels

Histoire des Neurosciences Computationelles
===========================================

-  suit d'abord l'histoire des neurosciences
   |http://upload.wikimedia.org/wikipedia/commons/7/75/Duck_of_Vaucanson.jpg|
-  1930 : Turing
   |http://longstreet.typepad.com/.a/6a00d83542d51e69e20120a5d6fc90970c-500wi|
-  1950 : Hebb / von Neumann
-  1950 : réseaux de neurones, parallelisme (PDP, Rosenblatt)
-  1980 : étude des systèmes complexes, arrivée de l'émergence (Amari,
   Grossberg, Kohonen, Hopfield, physique statistique), premières
   définitions des Neurosciences Computationelles (congrès de Carmel)
-  1990 : machine learning (NIPS)
-  2000 : machines hybrides, science de la complexité (probabilités),
   approche système (explosion du volume de données)
   |http://people.csail.mit.edu/koen/wholeBrainAtlasMesh.gif|
-  2010 : ...

Niveaux d'analyse de David Marr
===============================

+----------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **fonction** / définition                                                                                                                                      | **algorithmique** / méthode                                                                                                                                                                                                                                                                                                    | **hardware** / structure, support neural                                                                                                                                                                                                                             |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| analyse spectrale                                                                                                                                              | décomposition de Fourier                                                                                                                                                                                                                                                                                                       | FFT                                                                                                                                                                                                                                                                  |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| cognition et comportement (modèles de prise de décision; conditionnement classique; conditionnement opérant; apprentissage par réenforcement; neuroéconomie)   | Traitement de l'information (traitement sensoriel; filtres linéaires et champs récepteurs; estimation des champs récepteurs; détecteurs de contour; modèle de Hubel et Wiesel; statistiques des images naturelles; théorie de l'information; analyse en composantes indépendante; décodage neuronale; codage par population)   | Dynamique et mécanismes (biophysique d'un neurone; génération de potentiels d'action; réseaux de neurones feedforward et récurrent; réseaux attracteurs; fonctions d'énergie, énergie de Liapounov; apprentissage et plasticité synaptique; mémoires associatives)   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Modèles des systèmes neuronaux : La perception visuelle, système vestibulaire, contrôle oculomoteur, contrôle des membres, prise de décision.                  | Théorie des réseaux neuronaux : Codage neuronaux, apprentissage supervisé et non supervisé, apprentissage par renforcement.                                                                                                                                                                                                    | Modèles de neurones : Modèles de membrane, potentiels d’action, équation Hodgkin-Huxley, modèles de compartiments, canaux, synapses.                                                                                                                                 |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| *suivi d'objet*                                                                                                                                                | *détection d'objet*                                                                                                                                                                                                                                                                                                            | *circuit V1-MT/MST-FEF*                                                                                                                                                                                                                                              |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Suivi d'objet: l'exemple de l'Occular Following Response
========================================================

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|     |grating_contrast| |grating_size| |full_field_barberpole|                                                                                                                                                                  |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `Figure </LaurentPerrinet/Figures/Perrinet07neurocomp/FigureZero>`__ **Stimuli used for testing OFR.** *(Left) Grating in a disk aperture with varying contrast and*\ (Middle)*with varying diameters.*\ (Right) Barberpole.   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

|https://invibe.net/LaurentPerrinet/Figures/Perrinet07neurocomp/FigureUn?action=AttachFile&do=get&target=summary.png|

|Figures/Perrinet04tauc/FigureUn/inverse.png|

Modèles Probabilistes
=====================

|model_simple.png|

Avantages des représentations probabilitistes
---------------------------------------------

#. Règles de calcul probabiliste / lien avec la théorie de l'information
#. Le modèle génératif (*vraissemblance*) permet de baser inférence
   (échelle temporelle du codage) et apprentissage (échelle temporelle
   de l'adaptation)
#. Modèles hiérarchiques
#. Réseaux bayesiens

La règle de Bayes
-----------------

#. $P( \\vec{V} \| {\\bf I} ) \\propto P( {\\bf I} \| \\vec{V} ). P(
   \\vec{V} )$ :

   #. on veut calculer la probabilité *a posteriori*,
   #. Le modèle génératif permet de définir la probabilité de
      *vraissemblance* de tous les modèles directs,
   #. On introduit un prior (ici perceptif) modulant cette probabilité.

De la mesure aux probabilités
=============================

-  Soit $\\mathbf{I}$ une image contenant du mouvement
-  La meilleure estimation de la vitesse de translation est:
   $$\\vec{v}^\\ast = E( \\vec{V} \| \\mathbf{I} ) = \\int \\vec{V} dP(
   \\vec{v} \| \\mathbf{I} )$$

|../050_ProbabilisticModels/model_simple.png|

Bayes
-----

-  $$P( \\vec{V} \| {\\bf I} ) \\propto P( {\\bf I} \| \\vec{V} ). P(
   \\vec{V} )$$

Un modèle du mouvement
----------------------

-  Connaissant $\\vec{V}$, on estime que $\\mathbf{I}(\\vec{x},t)
   \\approx \\mathbf{I}(\\vec{x} - \\vec{V} . dt ,t-dt)$
-  $$P( {\\bf I} \| \\vec{V} ) \\propto \\exp(- \\frac{C\ :sup:`2 .
   \\mathcal{T}(\\mathbf{I}_{100})`\ 2}{2.\\sigma_m^2})$$

   -  avec $\\mathcal{T}(\\mathbf{I}_{100}) = \\\|
      \\mathbf{I}_{100}(\\vec{x},t) - \\mathbf{I}_{100}(\\vec{x} -
      \\vec{V} . dt ,t-dt) \\\|$
   -  Son contraste est $C$ par rapport à une référence:
      $\\mathbf{I}=C.\\mathbf{I}_{100}$

-  Hypothèse quadratique: $$P( {\\bf I} \| \\vec{V} ) = \\mathcal{N}(
   \\vec{V_m} , \\sigma_m )$$

inclusion d'un prior basse vitesse
----------------------------------

-  $$P( \\vec{V} ) = \\mathcal{N}( 0 , \\sigma_p )$$
-  On en déduit: $$ P( \\vec{V} \| \\mathbf{I} ) \\propto \\exp(-
   \\frac{C\ :sup:`2 . \\\| \\vec{V}-\\vec{V_m}
   \\\|`\ 2}{2.\\sigma_m\ :sup:`2 } - \\frac{ \\\| \\vec{V}
   \\\|`\ 2}{2.\\sigma_p^2 })$$

|naka_rushton.png|

Naka-Rushton
------------

-  On définit le gain $$\\gamma (C) = \\frac{ \\vec{V}(C)}{ \\vec{V_m}
   }$$
-  On trouve: $$\\gamma (C) \\propto
   \\frac{C\ :sup:`2}{C_{50}`\ 2+C^2}$} with $C_{50} \\propto
   \\frac{\\sigma_p}{\\sigma_m}$$

intégration d'informations indépendantes
========================================

|https://invibe.net/LaurentPerrinet/Figures/Perrinet08areadne/FigureDeux?action=AttachFile&do=get&target=model_rog.png|

-  $\\mathcal{N} (\\vec{V}_
   \\bf n
   C
   \\bf n
   )=\\frac{1}{\\sqrt{det(2 \\pi C
   \\bf n
   )}}.exp(\\frac{1}{2} (\\vec{V}-\\vec{V}_
   \\bf n
   )\ :sup:`T C{{\\bf n}}`\ {-1} (\\vec{V} - \\vec{V}_
   \\bf n
   )$
-  avec $C_

   \\bf n

   $ donné par

   ::

       \begin{eqnarray*}%
       \left( \begin{array}{ccc}%
       \cos(\theta) & -\sin(\theta) \\%
       \sin(\theta) & \cos(\theta)%
       \end{array} \right)%
       \left( \begin{array}{ccc}%
       \sigma_{{\bf n}}^2 & 0 \\%
       0 & \sigma_2^2%
       \end{array} \right)%
       \end{eqnarray*}%

-  Indépendence des bruits de mesure: $ P( \\vec{V} \| \\mathbf{I} ) =
   \\Pi_

   \\bf n

   P( \\vec{V} \| \\mathbf{I} , {\\bf n})=\\mathcal{N} (\\vec{v}_m,C)$
   avec :

   ::

       \begin{eqnarray*}
       \left\{
       \begin{array}{rcl}
       C^{-1}              &=& \sum C^{-1}_{{\bf n}}\\
       C^{-1} . \vec{v}_m &=& \sum C^{-1}_{{\bf n}} \vec{v}_{{\bf n}}
        \end{array}
        \right.
       \end{eqnarray*}

-  d'où

   ::

       \begin{eqnarray*}%
       C_{{\bf n}}^{-1} = %
       \left( \begin{array}{ccc}
       \cos(\theta) & \sin(\theta) \\
       -\sin(\theta) & \cos(\theta)
       \end{array} \right)
       \left( \begin{array}{ccc}
       \sigma_{{\bf n}}^{-2}  & 0 \\
       0 & \sigma_2^{-2}
       \end{array} \right)
       \end{eqnarray*}

intégration spatio-temporelle
=============================

|https://invibe.net/LaurentPerrinet/Figures/Perrinet08areadne/FigureTrois?action=AttachFile&do=get&target=fit_BRF.png|

-  intégration sur la surface d'un disque:

   ::

       \begin{eqnarray*}%
       \gamma(d) = \frac{C^2}{C_e^2} . \frac{ 1- \exp(-\frac{d^2}{2.\omega^2}) }{ 1 + \frac{C^2}{C_e^2}.(1- \exp(-\frac{d^2}{2.\omega^2})) }%
       \end{eqnarray*}%

-  avec un champ inhibiteur

   ::

       \begin{eqnarray*}
       \gamma(d_c) = \frac{ \frac{C^2}{C_e^2} . g_e }{ 1 + \frac{C^2}{C_i^2}. g_i  + \frac{C^2}{C_e^2}. g_e}
       \mbox{ with }
       \left\{
       \begin{array}{rcl}
       g_e              &=& 1- \exp(-\frac{d_c^2}{2.\omega^2}) \\
       g_i &=& 1- \exp(-\frac{d_c^2}{2.\omega_i^2})
        \end{array}
        \right.
       \end{eqnarray*}

-  extensible à d'autres formes d'intégration

|Animation of the formation of RFs during aSSC learning|

Des probas à une définition du coût neural
==========================================

$$ {\\bf I} = \\Psi \\cdot \\vec{c} + \\vec{\\nu} $$

$$ \\mathcal{C}( {\\bf I} \| \\vec{c} , \\Psi) = -\\log P( {\\bf I} \|
\\vec{o} , \\Psi ) $$ $$ \\mathcal{C}( {\\bf I} \| \\vec{c} , \\Psi ) =
\\log Z + \\frac{1}{2\\sigma_n\ :sup:`2} \\\| {\\bf I} - \\Psi \\cdot
\\vec{c} \\\|`\ 2 - \\sum_i \\log P(c_i \| \\Psi)$$ $$ \\mathcal{C}(
{\\bf I} \| \\vec{c} , \\Psi ) = \\log Z +
\\frac{1}{2\\sigma_n\ :sup:`2} \\\| {\\bf I} - \\Psi \\cdot \\vec{c}
\\\|`\ 2 - \\lambda \\\| \\vec{c} \\\|_0$$

-  un problème inverse insoluble (NP-complet). Soyons gourmants!

du coût neural au code neuronal
===============================

apprentissage par descente de gradient
--------------------------------------

-  connaissant le $\\vec{c}$ optimal, $\\forall i, \\Psi_{i} $ devient
   $ \\Psi_{i} + \\eta c_{i} ({\\bf I} - \\Psi\\cdot\\vec{c}) $

codage par Matching Pursuit
---------------------------

#. pour un $\\Psi$ donné, on choisit $ i^\\ast =
   \\mbox{`ArgMax </LaurentPerrinet/ArgMax>`__\ }_i (\\rho_i)$ avec
   $\\rho_i = <\\frac
   \\bf I
   {\\\| {\\bf I} \\\|} , \\frac{ \\Psi_i}{\\\| \\Psi_i\\\|} > $
#. comme $ {\\bf I} = a_{i\ :sup:`\\ast} \\dico_{i`\\ast} + \\bf{R} $,
   utilisons $\\bf{R}$ et retournons à **1.**

Pour plus d'informations, voir `Perrinet, Neural Computation
(2010) </LaurentPerrinet/Publications/Perrinet10shl>`__.

|Figures/Perrinet03ieee/FigureZero/v1_tiger.gif|

D'autres modèles de plasticité
==============================

|http://topographica.org/Tutorials/images/oo_or_map.png|

Apprentissage non-supervisé
---------------------------

#. Apprentissage Hebbien linéaire (PCA), décorrelation
#. Réseaux Winner-take-all, clustering
#. Codes distribués parcimonieux (sparse coding)

Plasticité et cartes corticales
-------------------------------

#. Self-organizing maps, Kohonen nets
#. Modèles de ré-organisation topographique
#. Apprentissage de sous-variétés

Codage Neural et systèmes dynamiques linéaires
==============================================

|http://upload.wikimedia.org/wikipedia/en/3/3f/LinDynSysTraceDet.jpg|

-  systèmes dynamiques linéaires $$ \\frac{d}{dt} \\mathbf{x}(t) =
   \\mathbf{A} \\mathbf{x}(t) $$
-  Les racines de $det(A- \\lambda I)$ sont les valeurs propores de $A$.
   Le signe des racines determine la stabilité du système.
-  Pour 2-dimensions, le polynôme characteristique est de la forme
   $\\lambda\ :sup:`2-\\tau\\lambda+\\Delta=0$. Les racines sont donc:
   $$ \\lambda=\\frac{\\tau \\pm \\sqrt{\\tau`\ 2-4\\Delta}}{2}$$

|http://upload.wikimedia.org/wikipedia/en/5/55/LinearFields.png|

Codage Neural et systèmes dynamiques NON linéaires
==================================================

|Figures/Voges10neurocomp/FigureTrois|

Codage Neural et systèmes dynamiques NON linéaires (2)
======================================================

|Figures/Voges09cosyne/FigureModel|

Codage Neural et systèmes dynamiques NON linéaires (3)
======================================================

|Figures/Kremkow10jcns/FigureTrois|

Des points à retenir
====================

-  Importance de poser (toutes) les hypothèses: a-t-on compris
   l'ensemble du signal?
-  Compréhension de la cognition à différents niveaux d'analyse, à
   différentes échelles.
-  Nous quittons le siècle de l'information. Nous entrons dans le siècle
   de la complexité.


.. |http://2010.neurocomp.fr/images/neurocomplog.png| image:: http://2010.neurocomp.fr/images/neurocomplog.png
.. |https://crac.dsi.cnrs.fr/image/logo_cnrs.gif| image:: https://crac.dsi.cnrs.fr/image/logo_cnrs.gif
.. |http://www.ecs.syr.edu/faculty/fawcett/handouts/webpages/pictures/turingMachine.gif| image:: http://www.ecs.syr.edu/faculty/fawcett/handouts/webpages/pictures/turingMachine.gif
.. |http://upload.wikimedia.org/wikipedia/commons/c/c2/SnowflakesWilsonBentley.jpg| image:: http://upload.wikimedia.org/wikipedia/commons/c/c2/SnowflakesWilsonBentley.jpg
.. |http://parasol.tamu.edu/~neilien/research/neurons.jpg| image:: http://parasol.tamu.edu/~neilien/research/neurons.jpg
.. |alert| image:: https://invibe.net/moin_static196/moniker/img/alert.png
.. |http://upload.wikimedia.org/wikipedia/commons/7/75/Duck_of_Vaucanson.jpg| image:: http://upload.wikimedia.org/wikipedia/commons/7/75/Duck_of_Vaucanson.jpg
.. |http://longstreet.typepad.com/.a/6a00d83542d51e69e20120a5d6fc90970c-500wi| image:: http://longstreet.typepad.com/.a/6a00d83542d51e69e20120a5d6fc90970c-500wi
.. |http://people.csail.mit.edu/koen/wholeBrainAtlasMesh.gif| image:: http://people.csail.mit.edu/koen/wholeBrainAtlasMesh.gif
.. |grating_contrast| image:: https://invibe.net//Figures/Perrinet07neurocomp/FigureZero?action=AttachFile&do=get&target=grating_contrast.gif
.. |grating_size| image:: https://invibe.net//Figures/Perrinet07neurocomp/FigureZero?action=AttachFile&do=get&target=grating_size.gif
.. |full_field_barberpole| image:: https://invibe.net//Figures/Perrinet07neurocomp/FigureZero?action=AttachFile&do=get&target=full_field_barberpole.gif
.. |https://invibe.net/LaurentPerrinet/Figures/Perrinet07neurocomp/FigureUn?action=AttachFile&do=get&target=summary.png| image:: https://invibe.net/LaurentPerrinet/Figures/Perrinet07neurocomp/FigureUn?action=AttachFile&do=get&target=summary.png
.. |Figures/Perrinet04tauc/FigureUn/inverse.png| image:: https://invibe.net//Figures/Perrinet04tauc/FigureUn?action=AttachFile&do=get&target=inverse.png
.. |model_simple.png| image:: https://invibe.net//Presentations/10-10-20_M2_MasterSciences/050_ProbabilisticModels?action=AttachFile&do=get&target=model_simple.png
.. |../050_ProbabilisticModels/model_simple.png| image:: https://invibe.net//Presentations/10-10-20_M2_MasterSciences/050_ProbabilisticModels?action=AttachFile&do=get&target=model_simple.png
.. |naka_rushton.png| image:: https://invibe.net//Presentations/10-10-20_M2_MasterSciences/055_ProbabilisticModelsForMotionPerception?action=AttachFile&do=get&target=naka_rushton.png
.. |https://invibe.net/LaurentPerrinet/Figures/Perrinet08areadne/FigureDeux?action=AttachFile&do=get&target=model_rog.png| image:: https://invibe.net/LaurentPerrinet/Figures/Perrinet08areadne/FigureDeux?action=AttachFile&do=get&target=model_rog.png
.. |https://invibe.net/LaurentPerrinet/Figures/Perrinet08areadne/FigureTrois?action=AttachFile&do=get&target=fit_BRF.png| image:: https://invibe.net/LaurentPerrinet/Figures/Perrinet08areadne/FigureTrois?action=AttachFile&do=get&target=fit_BRF.png
.. |Animation of the formation of RFs during aSSC learning| image:: https://invibe.net//SparseHebbianLearning?action=AttachFile&do=get&target=ssc.gif
.. |Figures/Perrinet03ieee/FigureZero/v1_tiger.gif| image:: https://invibe.net//Figures/Perrinet03ieee/FigureZero?action=AttachFile&do=get&target=v1_tiger.gif
.. |http://topographica.org/Tutorials/images/oo_or_map.png| image:: http://topographica.org/Tutorials/images/oo_or_map.png
.. |http://upload.wikimedia.org/wikipedia/en/3/3f/LinDynSysTraceDet.jpg| image:: http://upload.wikimedia.org/wikipedia/en/3/3f/LinDynSysTraceDet.jpg
.. |http://upload.wikimedia.org/wikipedia/en/5/55/LinearFields.png| image:: http://upload.wikimedia.org/wikipedia/en/5/55/LinearFields.png
.. |Figures/Voges10neurocomp/FigureTrois| image:: https://invibe.net//Figures/Voges10neurocomp/FigureTrois?action=AttachFile&do=get&target=Voges10Fig3.jpg
   :target: https://invibe.net/LaurentPerrinet/Figures/Voges10neurocomp/FigureTrois
.. |Figures/Voges09cosyne/FigureModel| image:: https://invibe.net//Figures/Voges09cosyne/FigureModel?action=AttachFile&do=get&target=nicole.jpg
   :target: https://invibe.net/LaurentPerrinet/Figures/Voges09cosyne/FigureModel
.. |Figures/Kremkow10jcns/FigureTrois| image:: https://invibe.net//Figures/Kremkow10jcns/FigureTrois?action=AttachFile&do=get&target=KremkowFig3.png
   :target: https://invibe.net/LaurentPerrinet/Figures/Kremkow10jcns/FigureTrois
