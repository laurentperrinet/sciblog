#! /usr/bin/env python3
# -*- coding: utf-8 -*-
from __future__ import division, print_function, absolute_import
__author__ = "Laurent Perrinet INT - CNRS"
__licence__ = 'BSD licence'
DEBUG = True
DEBUG = False
"""

Séminaire NeuroMath

"""

import os
home = os.environ['HOME']

from slides import Slides

meta = dict(
    draft = DEBUG, # show notes etc
    width= 1600,
    height= 1000,
    margin= 0.,#1618,
    reveal_path = 'https://cdnjs.cloudflare.com/ajax/libs/reveal.js/3.4.1/',
    #reveal_path = 'file://' + home + '/pool/libs/numbers/ipython_slides/reveal.js/',quantic/RTC/ipython_slides/
    #reveal_path = 'file://' + home + '/quantic/RTC/ipython_slides/reveal.js/',
    theme='night',
    author='Laurent U Perrinet, INT',
    author_link='<a href="https://laurentperrinet.github.io">Laurent U Perrinet, INT</a>',
    title="Les illusions visuelles, un révélateur du fonctionnement de notre cerveau" ,
    short_title="Qu’est ce qu’une image?",
    conference="Tous connectés, Bibliothèque de Méjanes",
    Acknowledgements=" ",

sections= [ 'Espace visuel',
            'Naissance de la forme',
           'Prédire le présent'])
s= Slides(meta)
#####################################################################################
## Intro - 5''
#####################################################################################
#####################################################################################

intro = """
<h2 class="title">{title}</h2>
<h3>{author_link}</h3>
<img src="figures/troislogos.png" width=61%/>
{Acknowledgements}
<h3>{conference}</h3>
        """.format(**meta)
s.add_slide(content=intro,
            notes="""

Les illusions visuelles sont des créations d'artistes, de scientifiques et plus récemment, grâce aux réseaux sociaux, du grand public qui proposent des situations souvent incongrues, dans lesquelles l'eau remonte une cascade, les personnes volent dans les airs ou des serpents se mettent à tourner. Au-delà de leur indéniable coté ludique, ces illusions nous apprennent beaucoup sur le fonctionnement du cerveau. En tant que chercheur en Neurosciences à l'Institut de Neurosciences de la Timone à Marseille, je vous dévoilerai des aspects du fonctionnement du cerveau qui sont souvent méconnus. En particulier, nous verrons pourquoi un magicien peut tromper nos sens ou comment des objets peuvent voyager dans le temps. Surtout nous essaierons de comprendre le fonctionnement de notre perception visuelle sur les bases d'une théorie de la vision non pas comme une simple caméra qui enregistre des images mais comme un processus actif en relation avec le monde qui nous entoure.

""")
################################################################################
## Espace - 5''
################################################################################
s.open_section()
s.add_slide_outline(0, title="Plan de l'exposé")

figpath = 'figures'
for fname in [
              'Ponzo_illusion.gif',
            'optical-illusions-part-2-63.jpg', # room
              'funny-perfectly-timed-photos-17__700.jpg', # au luxembourg
  'Grey_square_optical_illusion.svg',
  'Grey_square_optical_illusion_proof2.svg',
  #'Mach_bands_-_animation.gif',
  'Optical_grey_squares_orange_brown.svg',
              'Duck-Rabbit_illusion.jpg',
              'Spinning_Dancer.gif',
              'prior-optical-illusions-part-2-68.jpg', # face
              ]:
    #s.add_slide(image_fname=os.path.join(figpath, fname),
    s.add_slide(content=s.content_figures(
        [os.path.join(figpath, fname)],
        cell_bgcolor="black", #title='Experimental results', #: ' + label,
        height=s.meta['height']*.9
        ),
                      notes="""
it is the set of cognitive processes that allow to make sense from the visual inputs

- on peut apprendre rapidement qu'il ne faut pas croire tout ce qu'on voit
(surtout si c'est sur internet)
- priors

""")
s.close_section()
################################################################################
## Formes - 5''
################################################################################
################################################################################
s.open_section()
s.add_slide_outline(1, title="Plan de l'exposé")
for fname in [
'Dynamo-on.jpg',
 'Dynamo-off.jpg',
#'Dynamo-4.jpg',
              'Subjectively_constructed_water-color.gif',
              'Optical-illusion-checkerboard-twisted-cord.svg',
            'PinnaAsolo.jpg',
            'spiral.jpg',
            'pinna.jpg ',
            '1-ouchi.jpg',
            'ouchi.jpg',
             'power.png', # lee sedol
              ]:
    #s.add_slide(image_fname=os.path.join(figpath, fname),
    s.add_slide(content=s.content_figures(
        [os.path.join(figpath, fname)],
        cell_bgcolor="black", #title='Experimental results', #: ' + label,
        height=s.meta['height']*.9
        ),
                      notes="""

- illusions visuelles:  Anamorphose par Felice Varini "vingt-trois disques évidés plus douze moitiés et quatre quarts" Exposition:
"DYNAMO" Grand Palais, Paris 2013 Photo: André Morin
- ouchi / pinna
""")
s.close_section()
s.open_section()
s.add_slide_outline(2, title="Plan de l'exposé")
#####################################################################################
## Temps -  5''
#####################################################################################
#####################################################################################
#figpath = os.path.join(home, 'quantic/2015_RTC/2014-04-17_HDR/figures/')
s.add_slide(image_fname=os.path.join(figpath, 'tsonga.jpg'),
                      notes="""
Problem statement: optimal motor control under axonal delays. The central
nervous system has to contend with axonal delays, both at the sensory and the
motor levels. For instance, in the human visuo-oculomotor system, it takes
approximately $\tau_s=50~ms$ for the retinal image to reach the visual areas
implicated in motion detection, and a further $\tau_m=40~ms $ to reach the
oculomotor muscles.
""")
s.add_slide(image_fname=os.path.join(figpath, 'figure-tsonga.png'),
                      notes="""
* ... As a consequence, for a tennis player trying to intercept a
ball at a speed of $20~m.s^{-1}$, the sensed physical position is $1~m$ behind
the true position (as represented here by $\tau_s \cdot \vec{V}$), while the
position at the moment of emitting the motor command will be $.8~m$ ahead of
its execution ($\tau_m \cdot \vec{V}$).  * Note that while the actual position
of the ball when its image formed on the photoreceptors of the retina hits
visual read is approximately at $45$ degrees of eccentricity (red dotted line),
the player's gaze is directed to the ball at its **present** position (red
line), in anticipatory fashion. Optimal control directs action (future motion
of the eye) to the expected position (red dashed line) of the ball in the
future --- and the racket (black dashed line) to the expected position of the
ball when motor commands reach the periphery (muscles).
""")
#figpath = os.path.join(home, 'quantic/science/2016-02-02_Taouali15jnp/Communications/2015-02-09_Perrinet15abudhabi/figures/')
s.add_slide(content="""
    <video controls src="{}" autoplay=1 loop=1 width=99%/>
""".format(os.path.join(figpath, 'flash_lag.webm')),
                      notes="""
Indeed, in a standard empirical variant of the FLE, a first stimulus moves
continuously across the screen along the central horizontal axis.  As this
moving stimulus reaches the center of the screen, a second stimulus is flashed
nearby and in perfect vertical alignment with it.  Despite the fact that the
respective horizontal positions of each stimulus are physically identical when
the flash occurs, the moving stimulus is most often perceived \emph{ahead} of
the flashed one (see Figure~\ref{fig:FLE-cartoon}).
""")
#figpath = os.path.join(home, 'quantic/science/2016-02-02_Taouali15jnp/Communications/2015-02-09_Perrinet15abudhabi/figures/')
#for panel, label in zip(['1', '2', '3', '4'], ['short', 'medium', 'long', 'more cells']):
for panel, label in zip(['3'], ['long']):
    s.add_slide(content=s.content_figures(
        [os.path.join(figpath, 'ExperimentalResult_' + panel + '.png')],
        cell_bgcolor="black", title='Experimental results', #: ' + label,
        height=s.meta['height']*.8),
        notes="""
The first step was to analyze the raw data:

1. The results for the shortest trajectory shows a typical profile for which
the firing rate increases as the bar reaches the receptive field.

2. The results are different for the medium trajectory and the firing rate
increases before the bar reaches the receptive field.

3. We get a similar behaviour for the longest trajectory and the firing rate
increases well before the bar reaches the receptive field.


As a consequence, there seem to be some "priming" (to not say anticipation)
appears to be present in the response to indivual cells..

4. These results are observed in different cells (such as is shown here),
animals, and modalities (VSDI + LFP)

... can we decode the dynamics at the level of the population?
""")
s.close_section()

## Outro - 2''
s.open_section()
s.add_slide(content=intro,
            notes="""
Merci!
""")
s.close_section()

s.compile()
