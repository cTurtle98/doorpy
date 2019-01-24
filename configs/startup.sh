#!/bin/bash

cd $HOME/doorpy &&\
git pull &&\
python3 door.py &

[[ -z $DISPLAY && $XDG_VTNR -eq 1 ]] && startx -- -nocursor
