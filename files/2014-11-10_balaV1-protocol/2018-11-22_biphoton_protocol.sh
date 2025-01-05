#!/usr/bin/env bash
NAME=2018-11-22_biphoton
cd ../files/2014-11-10_balaV1-protocol
rm -fr `echo $NAME`_protocol.zip `echo $NAME`
echo 'start generating files'
ipython3 `echo $NAME`_protocol.py
echo 'done generating files'
zip `echo $NAME`_protocol.zip `echo $NAME`_protocol.* `echo $NAME`_protocol.sh `echo $NAME`/* `echo $NAME`/**/*
rm -fr `echo $NAME`
cd ../..
