.. title: rotating a video using ffmpeg
.. slug: 2012-04-30-rotating-a-video-using-ffmpeg
.. date: 2012-04-30 13:36:57
.. type: text
.. tags: sciblog

Easy transformations of videos:

-  turn to the right

   ::

       ffmpeg  -i  2012-04-29\ 19.31.32.mov  -vf "transpose=1" -sameq -y 2012-04-29\ 19.31.32_right.mov



.. TEASER_END


-  turn to the left

   ::

       ffmpeg -i  2012-04-29\ 19.31.32.mov  -vf "transpose=3" -sameq 2012-04-29\ 19.31.32_left.mov

-  upside down

   ::

       ffmpeg -i  2012-04-29\ 19.31.32.mov  -vf "transpose=2" -sameq 2012-04-29\ 19.31.32_left.mov

-  made some scripts:

   ::

       $ vim ~/bin/video_rotate.sh
       $ chmod +x ~/bin/video_rotate.sh

       $ cat  ~/bin/video_rotate.sh
       #! /usr/bin/env bash
       ORIGINAL_IFS=$IFS
       IFS=$'\n'
       ffmpeg  -i $1 -v 0  -vf "transpose=$2"  -qscale 0 -y tmp.mov && mv tmp.mov $1
       IFS=$ORIGINAL_IFS

       $ video_rotate.sh 2012-04-29_19.31.32.mov 1
