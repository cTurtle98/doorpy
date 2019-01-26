#!/bin/bash


#doorpy by Ciaran Farley
#https://github.com/cTurtle98/doorpy

if [[ "$(tty)" == "/dev/tty1" ]]
 then
  cd $HOME/doorpy
  git pull
  python3 door.py &

  [[ -z $DISPLAY && $XDG_VTNR -eq 1 ]] && startx -- -nocursor
fi
