#!/bin/bash

#doorpy by Ciaran Farley
#https://github.com/cTurtle98/doorpy

cd $HOME/doorpy

if [[ "$(tty)" == "/dev/tty1" ]]
 then
  git pull
  python3 door.py &

  [[ -z $DISPLAY && $XDG_VTNR -eq 1 ]] && startx -- -nocursor
fi
