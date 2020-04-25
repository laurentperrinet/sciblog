.. title: paramétrer l'e-mail à l'INT
.. slug: 2012-02-17-parametrer-le-mail-a-lINT
.. date: 2012-02-17 13:36:57
.. type: text
.. tags: int, sciblog


-  paramétrer un nouveau compte avec son adresse
   `lolo.toto@univ-amu.fr <mailto:lolo.toto@univ-amu.fr>`__


.. TEASER_END
.. warning::

  This post is certainly obsolete...


-  indiquer les parametres:

   #. serveur IMAP ``imap.univmed.fr``
   #. SSL (port 993)
   #. comme identifiant, l'identifiant univmed (de la forme ``toto.l``)
   #. serveur SMTP ``smtp.univmed.fr``

::

    SERVEUR ENTRANT (imap)

    Sélectionner IMAP et le nommer UNIV-AMU.

    Saisir votre adresse mail prenom.nom@univ-amu.fr.

    Votre login est du genre : nom.x ou nom (x est la première lettre de votre prénom)

    Saisir le : Prénom NOM

    L'adresse du serveur IMAP est : imap.univmed.fr

    Le port est 993 avec chiffrement SSL et l'authentification est par mot de passe.

    SERVEUR SORTANT (smtp)

    Sélectionner SMTP et le nommer UNIV-AMU.

    L'adresse du serveur IMAP est : smtp.univmed.fr

    Votre login est du genre : nom.x ou nom

    Le port est 465 avec chiffrement SSL et l'authentification est par mot de passe.
