#!/bin/bash
#Ciaran Farley
# doorpy setup script
# commands to modify a fresh install of raspbian Lite for use with doorpy

echo "UPDATING DEFAULT INSTALLED PACKAGES"
sudo apt-get update
sudo apt-get -y upgrade

echo -*20

echo "INSTALLING MINIMUM GUI FOR MESSAGE BOARD"
sudo apt-get install -y --no-install-recommends xserver-xorg x11-xserver-utils xinit openbox

echo -*20

echo "INSTALLING CHROMIUM FOR MESSAGE BOARD"
sudo apt-get install -y --no-install-recommends chromium-browser

echo -*20

echo "INSTALLING PYTHON DEPENDENCIES"
sudo apt-get install -y python3 python-pip
pip install Flask

echo -*20

echo "CHANGING OPENBOX CONFIG FOR X11 SETTINGS WE NEED"
cat configs/openbox-config > /etc/xdg/openbox/autostart

echo -*20

echo "adding startup script to .bash_profile"
echo '''
source $HOME/doorpy/configs/startup.sh
''' >> $HOME/.bash_profile
