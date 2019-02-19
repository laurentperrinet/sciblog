.. title: Deliverable M9-3: Workshop for definition of a detailed version of the V1 hypercolumn model
.. slug: 2007-10-22-Deliverable-M9-3-Workshop-for-definition-of-a-detailed-version-of-the-V1-hypercolumn-model
.. date: 2007-10-22 13:36:57
.. type: text
.. tags: pynn, neuralensemble, facets, sciblog


-  |(!)| This page `as a
   PDF <https://invibe.net/LaurentPerrinet/SciBlog/2007-10-22?action=AttachFile&do=view&target=Meeting_V1WorkshopMarseille_2007.pdf>`__

The INCM was holding a `workshop on the V1 hypercolumn model on the 22nd and 23rd of October 2007 <https://facets.kip.uni-heidelberg.de/private/wiki/index.php/Meeting_V1WorkshopMarseille_2007>`__.
The purpose of the workshop was to promote the coordination of modeling
efforts within the consortium and in particular to organize
collaboration in WP9T2 and associated work-packages. It is labeled as
deliverable M9-3: "Workshop for definition of a detailed version of the
V1 hyper-column model" for WP9-2 (workpackage 9 task 2), but is also
linked by its subject to WP5. In contrast to the previous meeting, we
started with brief presentations of the results from each group to
expose the different efficient aspects of each model. This allowed us in
the second half of the workshop to converge to some main issues and
prioritize the neural features that are the most important for the
efficiency of V1. As for the format, we proposed that PhD students and
post-docs should have the opportunity to present this work to give them
experience and reduce the burden on busy chiefs. We felt it was
important to involve as many in this workshop as possible as we approach
a crucial stage in integrating the different models.

.. TEASER_END

Program
-------

**Afternoon of Monday, 22 October 07: Framework**

12:30-14:00

Registration and Lunch

**14:00-18:00 (First session)**

Introduction: coordination of modeling efforts for WP9T2

14:00-14:10

Guillaume Masson (INCM): **Welcome**

14:10-14:30

*       Laurent presented some examples of using the benchmark structure
        proposed in `NeuroTools <http://neuralensemble.org/trac/NeuroTools/>`__
        and the new `SpikeList <http://neuralensemble.org/trac/NeuroTools/wiki/signals>`__
        object. The benchmark will be the privileged way of spreading the
        different benchmarks to all partners and is a practical way of
        describing a benchmark as a list of experiments, storing the result of
        the experiments, distribute and run the experiments on a cluster and
        finally for plotting figures. In a second part, Laurent presented the `SpikeList <http://neuralensemble.org/trac/NeuroTools/wiki/signals>`__
        object as an answer to the difficulty of finding a common format for
        describing lists of spikes. Some experimental example and an interface
        with `PyNN <http://neuralensemble.org/trac/PyNN>`__ was shown as a proof
        of concept. Jan suggested that the internal representation could be
        sparse. This should be easily done by using the format methods (See
        `SpikeList <http://neuralensemble.org/trac/NeuroTools/wiki/signals>`__).

14:40-15:10

*       Andrew and Jens presented a system's approach to modeling the visual
        system. Partners in FACETS need to exchange knowledge on their modeling
        progress and this approach allowed to construct a model from composite
        parts (retina, LGN, V1) from the “LEGO bricks” of the different groups.
        A practical example with INRIA/INCM retina and a INCM V1-layer 4 was
        shown. An LGN brick is to be developed. Brick for higher areas (MT) can
        also be developed.

15:20-16:00

*Coffee*

16:00-16:20

*       Andrew proposed a format specification for benchmarks : 1) the input is
        provided as zipped PNG files, storing is done in the FACETS knowledge
        base (every stimulus has a unique URL), 2) A specification scheme for
        writing benchmarks and a whole experiment was presented with a proposed
        format using a XML interface.

16:30-16:50

*       Adrien presented his physiologically realistic retina, emphasizing on
        the contrast gain control. His model uses the INRIA simulator but with
        an open architecture and specification compatible with the FACETS
        specification. The retina uses a feed-back on the bipolar cells to
        achieve realistic contrast gain control which was compared with
        classical experiments (Shapley and Victor, 79, Enroth and Cugell XX). A
        possible extent is to study the importance of the spike profile at image
        onset which reveals first the luminance image and then the edges (Enroth
        Cugell 83 Bernadete-Kaplan 99). He also approached a mean field approach
        valid for gratings.

17:00-17:20

*       Klaus presented the retina used at the TUG. It is based on a
        spatio-temporal decorrelation model from Dong and Attick (1995) for the
        linear part and on a gamma renewal process (Gazères, 1998) for the
        spiking part. It is available to FACETS partners in the SVN1 and will
        converted to the format specified in the VisualSytem class (See
        `https://www.kip.uni-heidelberg.de/repos/FACETSCOMMON/facetsmodel/LGN/trunk/graz <https://www.kip.uni-heidelberg.de/repos/FACETSCOMMON/facetsmodel/LGN/trunk/graz>`__
        ).

17:30-18:00

 **General Discussion**

* conclusions on benchmarking progress and decisions about their
  future development and use.
* We concluded on benchmarking progress and
  decided about their future development and use. In particular, the
  unification proposed by the Benchmark class and the
  `SpikeList <http://neuralensemble.org/trac/NeuroTools/wiki/signals>`__
  object from Laurent and the specification proposed by Andrew seemed to
  fit to the needs of the partners and we agreed to use the proposed
  schemes.
* We agreed on further definition of the visual benchmarks
  `WP9T2-VisionBenchmarks <https://facets.kip.uni-heidelberg.de/private/wiki/index.php/WP9T2-VisionBenchmarks>`__
  (while respecting the standards from
  `FACETS\_Benchmarks <https://facets.kip.uni-heidelberg.de/private/wiki/index.php/FACETS_Benchmarks>`__).
  This will be implemented in a coming deliverable.
* The question if we can reach the goal a single, common framework
  for multiple V1 models in FACETS was left open due to the wide variety
  of approaches in the consortium. However, the discussion suggested some
  collaborations of groups on some specific scientific questions.

**Morning of Tuesday, 23rd of october 07**

**09:00-13:00 (Second session)**

**Progress in Modeling V1**

* 09:00-09:20*

* Mike described current progress towards a neural model of motion
  perception in V1/MT, a collaborative project with CNRS/INCM. The model
  is based on the recurrent neural circuitry between a V1 hypercolumn and
  area MT, and uses a Kalman-Bucy approach to estimate the velocity of the
  moving object by integration of local motion information. The model will
  be suitable for testing using the FACETS visual motion benchmark
  stimuli, in particular the CNRS/INCM data on motion integration for
  smooth eye pursuit.*

09:30-09:50

* The KTH model was presented by Jan, with the latest changes and
  additions and some preliminary results. HH neuronal models, hierarchical
  columnar structure. The horizontal connectivity is specified by the
  LISSOM model while the vertical connectivity is inspired by biology.*

10:00-10:20

* Klaus presented the TUG model with the latest changes and some
  preliminary results. He illustrated the use of Izhikievitch neurons, the
  data from Alex Thomson (and not from Binzegger) by showing some results
  of the columnar model in particular by studying the influence of NMDA.*

10:30-10:50

* Jens presented progress of the INCM/ALUF cooperation emphasizing on
  progress in the specification of the thalamo-cortical projections. He
  presented results of applying the different benchmarks proposed to
  reveal the functional properties of the model. It emerged that the
  inhibition scheme used allowed a normalization of the input at the
  network level. This was put into evidence using the spike-triggered
  conductance profile which were consistent with some recent data from
  Rudolph et al. (2007).*

11:00-11:30

*Coffee*

11:30-13:00

* Round-table discussion: questions, problems, and issues of modeling V1.
  Moderator: G. Masson
* Retina model: shouldn't we use a more standardized input? How should
  we set up background noise? Biologists need to specify what they intend
  by background (on-going) activity to be simulated in large scale neural
  networks.
* Back to back cooperation between experimentalists and modelers for
  defining benchmarks in connections with dissemination of experimental
  data.
* Link with more high-level task, as the one presented by Mike and in
  WP9T3 or the work done in collaboration INCM-INRIA. Since they use the
  same benchmarks (such as motion integration), these approaches can
  better defined the computational rules to be implemented in large scale
  neural networks. One good example in the role of asymmetric diffusion of
  information/activity in the network, thanks to feedback from higher
  areas.

**13:00-14:00**

**Lunch**

**Afternoon of Tuesday, 23rd of october 07**

**14:00-16:30 (Third session)**

**Scientific questions coming from the Biology of V1**

14:00-14:20

*       Julian presented a review of different results on the physiology and
        anatomy of the cat retino-thalamo-cortical projections. In fact, though
        the question of the architecture of these projections was questioned
        during the workshop, little is known with general agreement. Correlating
        different works from the literature, a detailed quantification was
        reviewed suggesting a disagreement between anatomy and physiology.
        Presenting the work of Ringach (2004), he concluded by showing own
        simulations suggesting that the properties and diversity of the
        receptive field of cat's area 17 simple cells may be captured by a
        wiring scheme based on the specific quantization of the parameters of
        the retino-thalamo-cortical pathway.*

14:30-14:50

*       Cyril reviewed different models of the emergence of orientation and
        direction selectivity before emphasizing on the results of different
        groups on the role of conductance profile in this function. This
        revealed a diversity of behavior between push-pull model where
        inhibitory and excitatory profiles are in overlap and other
        configuration This was put in light with results obtained at the UNIC.*

15:00-15:20

*       Alex presented preliminary results of center-surround interactions
        using VSD optical imaging in the primate V1 cortex. In the retinotopic
        position of the center the response to the center appears with
        decreasing latency for increasing contrast. The response of the 80%
        contrast surround reaches the center at a latency equivalent to approx.
        15% contrast, leaving open the question of the interaction of these two
        information streams. Preliminary results show suppression for high
        contrasts but facilitation for low center contrast. Further analysis (of
        latency, propagation) suggests the functional role of horizontal
        propagation in this configuration.*

15:30-16:00

*Coffee*

16:00-16:30

General Discussion Moderator: Yves Fregnac (UNIC)

16:30-17:30

 **Outcome: Planning of Implementation plans / priorities for WP9T2.**

*       Several actions need to be taken. 1) We keep the idea of one annual
        meeting on V1 modeling. The meeting shall be held in June instead of
        October, to prepare for Annual reports and implementation plan. We will
        post a call for the organization of the 2008 meeting. We should also try
        to bring more biologists in these meetings. 2) We will organize a
        phone/video conference once every 3 months to exchange information and
        compare outputs for each benchmark steps. 3) We shall provide a timeline
        for delivering benchmark tools and objectives, as well as deadline for
        collecting results for testing models. Such a timeline will be added to
        the D9-2 in which we will describe the different benchmarks. 4) We will
        set a discussion list on the FACETS Wiki website to propose new
        questions from modelers to biologist and vice-versa. The idea is to put
        information for which there is a general agreement rather than having an
        on-going forum. Answers shall be concise, with reference to published
        work and or available data. 5) We shall promote active collaboration
        between sites with the objectives of common publication of one specific
        aspects of visual tasks to be develop in FACETS (on-going activity,
        local cortical point spread function ….)

Questions
---------

Below are some questions modelers (please add to this list) would like
the biologists at the meeting to answer during the round-table
discussion (11:30-13:30 on 23 October):

-  What is the purpose of the Y-type pathway input to layer 4 of cat
   area 17?
-  Is the tuning of cortical neurons dynamic or not (e.g. for
   orientation)?
-  Can simple or complex cortical cells be directionally selective but
   untuned for orientation?
-  Are inhibitory neurons in cortex generally tuned for orientation or
   not?
-  Do inhibitory fast-spiking (FS) neurons have a higher spiking
   threshold than excitatory regular-spiking (RS) neurons?
-  Is modelling corticothalamic feedback essential for models of V1?
-  What common mistakes do modellers make that annoy you and fellow
   biologists the most?
-  How can modellers best help the biologists?

For the sake of fairness, we would also like some questions from the
biologists for modellers to answer during the same discussion session.

Organization
------------

When and where?
~~~~~~~~~~~~~~~

The date for the workshop is Monday, 22 and Tuesday, 23 October 07. It
will take place at the INCM in Marseille as last meeting (see
`Marseille\_November2006 <https://invibe.net/LaurentPerrinet/SciBlog/2006-11-20>`__ ).

-  Meeting will be salle George Morin (INCM's seminar room),
-  Lunch at the CNRS on place,
-  monday dinner at "La Pôz" 1, Boulevard Saint-Anne , 13008 Marseille
   Tel : 04 91 77 70 00
-  local organization: Laurent Perrinet Tél +33 6 19 47 81 20
-  directions for
   `http://www.cnrs.fr/provence/delegation/Accueil\_Delegation/Acces\_en\_Voiture/plan\_d\_acces/plan\_acces\_par\_route.gif?popup=grande
   the
   lab <http://www.cnrs.fr/provence/delegation/Accueil_Delegation/Acces_en_Voiture/plan_d_acces/plan_acces_par_route.gif?popup=grande%20the%20lab>`__
   from the
   `http://www.cnrs.fr/provence/delegation/Accueil\_Delegation/Acces\_en\_Avion/;view
   airport (in
   french) <http://www.cnrs.fr/provence/delegation/Accueil_Delegation/Acces_en_Avion/;view%20airport%20(in%20french)>`__.
   When entering the campus, go to the main hall (large staircase),
   inside on the left you'll find on the same floor a door
   "Neurosciences Intégratives". Follow the next door in front of you
   (labelled "INCM"), and on the left (second door) you'll find the room
   "Salle Jean Requin" where we meet.

Who is attending
~~~~~~~~~~~~~~~~

Please
`https://facets.kip.uni-heidelberg.de/internal/jss/AttendMeeting?meetingID=28
register your
attendance <https://facets.kip.uni-heidelberg.de/internal/jss/AttendMeeting?meetingID=28%20register%20your%20attendance>`__.

-  monday lunch 16 people (everybody except Anders Lansner)
-  monday dinner 15 people (everybody except Anders Lansner and Andrew
   Davison)
-  tuesday lunch 16 people (everybody except Andrew Davison)

facilities
~~~~~~~~~~

we will have

-  a beamer
-  no internet connection (ask if you need one)
-  lunch and coffee breaks!
-  *( the video conferencing system was not needed anymore)*

more info
~~~~~~~~~

-  see the report of M9-3 at
   `https://www.kip.uni-heidelberg.de/repos/FACETSCOMMON/WP9T2/07-10\_M9-3/ <https://www.kip.uni-heidelberg.de/repos/FACETSCOMMON/WP9T2/07-10_M9-3/>`__
-  date poll
   `https://facets.kip.uni-heidelberg.de/private/jss/DatePoll?sId=7 <https://facets.kip.uni-heidelberg.de/private/jss/DatePoll?sId=7>`__
-  discussion list
   `https://facets.kip.uni-heidelberg.de/forum/viewtopic.php?t=147 <https://facets.kip.uni-heidelberg.de/forum/viewtopic.php?t=147>`__
-  this is a deliverable
   `https://facets.kip.uni-heidelberg.de/private/jss/servlet/de.bkmk.facets.Deliverables?m=showDeliverable&bk\_deliverableID=86
   M9-3 <https://facets.kip.uni-heidelberg.de/private/jss/servlet/de.bkmk.facets.Deliverables?m=showDeliverable&bk_deliverableID=86%20M9-3>`__
-  To ease the choice of a date for the workshop on the V1 hypercolumn
   model in October/November this year, a
   `https://facets.kip.uni-heidelberg.de/private/jss/DatePoll?sId=7 date
   poll <https://facets.kip.uni-heidelberg.de/private/jss/DatePoll?sId=7%20date%20poll>`__
   was created on the FACETS internal web page for all the people (tell
   Bjoern if somebody is missing) who should be interested in going.
-  Ryan Air is flying now to Marseille :
   `http://www.bookryanair.com/skylights/cgi-bin/skylights.cgi <http://www.bookryanair.com/skylights/cgi-bin/skylights.cgi>`__



.. |(!)| image:: https://invibe.net/moin_static196/moniker/img/idea.png
