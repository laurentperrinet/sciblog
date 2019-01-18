.. title: some unix tips
.. slug: 2009-11-22-some-unix-tips
.. date: 2009-11-22 13:36:57
.. type: text
.. tags: sciblog


-  find / -nouser te donneras tous les fichiers dont le nom du
   propriétaire est inexistant de la table /etc/passwd

   .. TEASER_END

-  batch converting

   ::

       for draw in `find /path/to/wiki/data -name \*.draw`; do
           file=`dirname $draw`/`basename $draw .draw`
           if [ -e "${file}.gif" ]; then
               echo "Converting ${file}.gif to ${file}.png"
               convert "${file}.gif" "${file}.png"
           fi
       done

-  You may always pipe the output of commands through grep to find
   specific words, but it can also be used to find files that contain a
   text string:

   ::

       grep -lir "some text" *

   The -l switch outputs only the names of files in which the text
   occurs (instead of each line containing the text), the -i switch
   ignores the case, and the -r descends into subdirectories.

-  compression

   ::

       in : tar cvf nom.tar dir/*
       out : tar xvf nom
       liste : tar tvf nom

-  du -sk : occupation des fichiers sur un disque
-  a2ps archives/unix.txt -Prsi2 imprime joliement...
-  dos2unix fic1 fic2 transforme fic1 en fichier texte unix nomme fic2
-  Pour connaitre le taux d'occupation de l'UC d'une machine, utiliser
   la commande sar. Exemple : sar -u 1 5 donne la consommation UC
   pendant 1s et 5 fois de suite
