.. title: WP5 Year 2 report: contribution of CNRS-INT (Institut de Neurosciences de la Timone)
.. slug: 2013-02-04-WP5-Year-2-report-contribution-of-CNRS-INT-(Institut-de-Neurosciences-de-la-Timone)
.. date: 2013-02-04 13:36:57
.. type: text
.. tags: sciblog, brainscales


During the first year of BrainScaleS, we have concentrated on
disseminating our work on the role of motion-based prediction in motion
detection. This led to a publication on the hypothesis that this prior
expectation may explain some phenomena explained otherwise by complex
arrangements of mechanisms, namely that motion-based prediction is
sufficient to solve the aperture problem (Perrinet and Masson, 2012).
During the second year, we extended this hypothesis to other types of
problems linked to the detection of motion. In particular, we focused on
the case were the stimulus is transiently and unexpectedly blanked, a
physiologically very relevant constraint occurring for instances during
blinks of the eye. For this, we have used the same theoretical framework
based on a Bayesian formulation and implemented using a particle
filtering scheme, but used a different experimental protocol inspired by
behavioral experiments conducted in the laboratory by CNRS-INT (Bogadhi,
2012). This is an important aspect as it allows to better understand the
dynamics of the neural representation without sensory input and more
generally to understand the interaction of the sensory flow with an
internal neural representation of the environment.


.. TEASER_END


+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| |Role of motion-based prediction in motion extrapolation|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|  *Role of motion-based prediction in motion extrapolation.* We show here the results of simulation of the motion-based prediction compared to velocity prediction (no position prediction). These models were tested for a dot moving in a straight trajectory but blanked (as given by the vertical bars) whether at the early stage (top panel) or in the late phase (bottom panel). This shows that compared to a control (condition with no blank), the system simply resumes the convergence to the veridical position at reappearance of the dot. In motion-based prediction, the systems catches up the trajectory and recovers more quickly to the response with no blank.   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Our results indicate that motion-based prediction is sufficient to
predict eye responses during the blank and ---more importantly--- the
dynamics of eye movements at the reappearance of the object. We compared
simulations of the motion-based predictive framework to a dot moving in
a straight trajectory which is transiently blanked, with a framework
where prediction is limited to the velocity domain but is not
anisotropically transported also in the position domain. This comparison
allowed to show that at the reappearance of the object, instead of just
resuming, the estimation of the position and velocity in the
motion-based prediction framework catches-up the error that may have
accumulated during the blank (see Figure). We have put in evidence that
this phenomenon is only present when the system converged to a "tracking
state", a phase transition that we first saw in our first study
(Perrinet and Masson, 2012) and that we studied systematically here.
Furthermore, we give some predictions as how the oculomotor response
should respond to the same protocol when visual input is perturbed by
noise, an experiment that has still not been performed behaviorally, and
that could confirm the validity of our probabilistic framework. These
results have been submitted for publication (Khoei, Masson and
Perrinet).

From this novel step, we wish to further study the role of prediction on
focusing on the neural implementation of these processes. Indeed, the
framework that we used so far used an abstract, probabilistic framework.
However, it is known to map well to a neural architecture such as those
developed in BrainScaleS at the modeling and hardware levels. Such a
venture was initiated in collaboration between CNRS-INT and KTH by
Bernhard Kaplan and we could give a sufficient large-scale network of
spiking neurons that could efficiently implement such algorithms. Our
plan is to resume this work in more generic conditions. One objective is
to apply it to different modalities,for instance to the somatosensory
system (collaboration with Dan Shulz, CNRS-UNIC). Also, we wish to
implement a model which is specifically more realistically accounting
for the properties of the primary visual cortex of primates and the
interaction this area may have with higher order areas. A post-doctoral
student was selected in year 2 to work on that issue in Years 3 and 4.
The ultimate goal of this work will be to have a pyNN-compatible network
that implements a realistic model of motion detection. This network will
be tested in light of the synthetic textures that we have generated
(Sanz et al. 2012, see WP4 task 1) and that we recently used to
disentangle the different read-outs that may be used by perception or
action (Simoncini et al., 2012). The use of neuromorphic hardware will
then be crucial to explore the configuration space of such large-scale
networks implementing motion detection.

-  Laurent U. Perrinet and Guillaume S. Masson. Motion-based prediction
   is sufficient to solve the aperture problem. *Neural Computation*,
   24(10):2726--50, 2012
-  Mina A. Khoei, Guillaume S. Masson and Laurent U. Perrinet. Role of
   motion-based prediction in motion extrapolation. *Submitted*.
-  Paula S. Leon, Ivo Vanzetta, Guillaume S. Masson and Laurent U.
   Perrinet. Motion Clouds: Model-based stimulus synthesis of
   natural-like random textures for the study of motion perception
   *Journal of Neurophysiology*, 107(11):3217--3226, 2012
-  Claudio Simoncini, Laurent U. Perrinet, Anna Montagnini, Pascal
   Mamassian and Guillaume S. Masson. More is not always better:
   dissociation between perception and action explained by adaptive gain
   control *Nature Neuroscience*, 2012



.. |Role of motion-based prediction in motion extrapolation| image:: https://invibe.net/LaurentPerrinet/Publications/Khoei13jpp?action=AttachFile&do=get&target=khoei13jpp_RMSE-Blank.png
   :target: /LaurentPerrinet/MotionPerception
