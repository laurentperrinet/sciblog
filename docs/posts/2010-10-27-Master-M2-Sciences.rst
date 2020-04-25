.. title: Master M2 Sciences
.. slug: 2010-10-27-Master-M2-Sciences
.. date: 2010-10-27 13:36:57
.. type: text
.. tags: talks, computationalneuroscience, sciblog

Neurosciences Computationelles : émergence dans des réseaux d'information
=========================================================================

Travaux pratiques : modèle bayesien de détection du mouvement d'objets
----------------------------------------------------------------------


.. TEASER_END


-  Le 27/10/2010, de 14h00 à 17h00 dans la salle formation de l'INCM
   (bâtiment N du GLM, 31, chemin Joseph Aiguier 13402 Marseille cedex).
-  |alert| me prévenir si vous n'avez pas un ordinateur portable
   personnel!

principe du TP
--------------

-  But: définition de la *probabilité de vraissemblance* pour des
   translations d'images grâce à l'utilisation d'un script générique
-  Méthode: montage d'expérience:

   #. expérience simple
   #. expérience avec vitesse entre 0 et une période
   #. effet du contraste sur le wagon wheel illusion

-  Résultats:

   #. une figure montrant 2 images successives d'un film, la densité de
      probabilité de mouvement. les images seront: un point, une ligne
      (réseau), un barber-pole, une image naturelle.
   #. une figure montrant l'influence d'un bruit ajouté sur ces images
   #. une figure montrant l'influence de la vitesse sur le mouvement
      d'un réseau

pré-requis
----------

-  les probabilités, les hypothèses, le cube de necker

   -  phénomènes bistables :
      `http://vision.psych.umn.edu/users/kersten/kersten-lab/shadows.html <http://vision.psych.umn.edu/users/kersten/kersten-lab/shadows.html>`__
      `http://en.wikipedia.org/wiki/The\_Spinning\_Dancer <http://en.wikipedia.org/wiki/The_Spinning_Dancer>`__
   -  un autre:
      `http://www.journalofvision.org/3/11/1/article.aspx#fig01 <http://www.journalofvision.org/3/11/1/article.aspx#fig01>`__

-  le théorème de Bayes: vraisemblance et probabilité a priori,
   probabilité a posteriori et décision MAP (maximum a posteriori)
-  installer le logiciel de simulation
-  télécharger la "boîte à outil":
   `motion\_plant.py </LaurentPerrinet/Presentations/10-10-27_M2_MasterSciences?action=AttachFile&do=get&target=motion_plant.py>`__

expérience simple
-----------------

-  pour charger la boîte à outils :

   ::

       import motion_plant as mp

-  pour visualiser une image

   ::

       I1, I2 = mp.generate(V_X = 3.5)
       mp.show_images(I1,I2)

-  Calcule la proba sur les vitesses V pour les 2 images:

   #. Il faut définir V avec la fonction velocity\_grid, par exemple:

      ::

          V= mp.velocity_grid(v_max = 5.)

      (v\_max est important il donne la valeur max des proba à tester)

   #. puis invoquer:

      ::

          P= mp.proba(V, I1, I2)

-  on peut voir la proba avec

   ::

       mp.show_proba(V, P)

-  et trouver celle qui correspond au maximum:

   ::

       mp.ArgMaxProba(V, P)

   ou la moyenne

   ::

       mp.MeanProba(V, P)

-  essayez différentes images...

   #. image naturelle

      ::

          I1, I2 = mp.lena()

   #. réseau carré

      ::

          I1, I2 = mp.generate(V_X = 2.5, square=True)

-  et différents paramètres, comme la variance de la vraissemblance

   ::

       sigmas = np.logspace(-2, 0, 10)

       for sigma in sigmas:
           I1, I2 = mp.generate(V_X = 2.5)
           P= mp.proba(V, I1, I2, sigma=sigma)
           mp.show_proba(V, P)
           pylab.title('sigma ' + str(sigma))
           print mp.ArgMaxProba(V, P), mp.MeanProba(V, P)

-  ou la variance du prior

   ::

       sigmas = np.logspace(-1, 1, 10)

       for sigma_p in sigmas:
           I1, I2 = mp.generate(V_X = 2.5)
           P= mp.proba(V, I1, I2, sigma_p=sigma_p)
           mp.show_proba(V, P)
           pylab.title('sigma_p ' + str(sigma_p))
           print mp.ArgMaxProba(V, P), mp.MeanProba(V, P)

expérience avec différents niveaux de bruit
-------------------------------------------

-  pour créer une liste de bruits à tester, utiliser

   ::

       noises = np.linspace(0, 2., 10)

       for noise in noises:
           I1, I2 = mp.generate(V_X = 2.5, noise=noise)
           mp.show_images(I1,I2)
           P= mp.proba(V, I1, I2, sigma_p=1.)
           print mp.ArgMaxProba(V, P), mp.MeanProba(V, P)

-  à comparer avec le cas où on est plus conservateur:

   ::

       pylab.close('all')
       N_contrast =10
       contrasts = np.linspace(0, 1., N_contrast)
       V_hat = np.zeros((N_contrast,2))
       for i, contrast in enumerate(contrasts):
           I1, I2 = mp.generate(V_X = 2.5, contrast=contrast, noise=.2,)
           P= mp.proba(V, I1, I2, sigma_p=10.)
           V_hat[i,:] = mp.MeanProba(V, P)

       pylab.plot(contrasts, V_hat[:,0], 'r')
       pylab.plot(contrasts, V_hat[:,1], 'r--')

       V_hat = np.zeros((N_contrast,2))
       for i, contrast in enumerate(contrasts):
           I1, I2 = mp.generate(V_X = 2.5, contrast=contrast, noise=.2,)
           P= mp.proba(V, I1, I2, sigma_p=1.)
           V_hat[i,:] = mp.MeanProba(V, P)

       pylab.plot(contrasts, V_hat[:,0], 'g')
       pylab.plot(contrasts, V_hat[:,1], 'g--')

-  ou avec une image naturelle:

   ::

       pylab.close('all')
       N_contrast =10
       contrasts = np.linspace(0, 1., N_contrast)
       V_hat = np.zeros((N_contrast,2))
       for i, contrast in enumerate(contrasts):
           I1, I2 = mp.lena()
           P= mp.proba(V, I1, I2, sigma_p=10.)
           V_hat[i,:] = mp.MeanProba(V, P)

       pylab.plot(contrasts, V_hat[:,0], 'b')
       pylab.plot(contrasts, V_hat[:,1], 'b--')

expérience avec un réseau à différentes vitesses
------------------------------------------------

-  pour créer une liste de vitesses à tester, utiliser

   ::

       speeds = np.linspace(0, 10., 10)
       V_hat = np.zeros((10,2))
       for i, V_X in enumerate(speeds):
           I1, I2 = mp.generate(V_X = V_X, frequence=12)
           P= mp.proba(V, I1, I2, sigma_p=1.)
           V_hat[i,:] = mp.ArgMaxProba(V, P)

       pylab.plot(speeds, V_hat[:,0], 'g')
       pylab.plot(speeds, V_hat[:,1], 'g--')

-  ... c'est le Wagon-wheel effect!

références
----------

-  Le Wagon-wheel effect:

   -  `http://www.michaelbach.de/ot/mot\_wagonWheel/index.html <http://www.michaelbach.de/ot/mot_wagonWheel/index.html>`__
   -  `http://en.wikipedia.org/wiki/Wagon-wheel\_effect <http://en.wikipedia.org/wiki/Wagon-wheel_effect>`__
   -  `http://en.wikipedia.org/wiki/Temporal\_aliasing <http://en.wikipedia.org/wiki/Temporal_aliasing>`__
   -  `http://fr.wikipedia.org/wiki/Effet\_stroboscopique <http://fr.wikipedia.org/wiki/Effet_stroboscopique>`__

-  Python

   -  `http://matplotlib.sourceforge.net/ <http://matplotlib.sourceforge.net/>`__

.. |alert| image:: https://invibe.net/moin_static196/moniker/img/alert.png
