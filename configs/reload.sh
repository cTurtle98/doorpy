#!/bin/bash

#Ciaran Farley
#doorpy
#https://github.com/cTurtle98/doorpy

#kill flask, git pull, start flask

kill $(ps a | grep "python3 door.py" | head -1 | cut -f 3 -d " ")

cd $HOME/doorpy
git pull
python3 door.py &
