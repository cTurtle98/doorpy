#!/bin/bash
#Ciaran Farley
# doorpy setup script
# commands to modify a fresh install of raspbian for use with doorpy

sudo apt remove --purge -y \
bluej \
geany \
greenfoot \
mathematica \
minecraft-pi \
libreoffice* \
vnc \
lxde \
lxpanel \
lxappearance \
lxde-common \
lxde-core \
lxde-icon-theme \
lxinput \
lxinput \
lxkeymap \
lxmenu-data \
lxappearance-obconf \
lxpanel-data \
lxrandr \
lxsession \
lxtask \
lxterminal 

sudo apt autoremove --purge
