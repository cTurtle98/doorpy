#!/bin/bash
#Ciaran Farley
# doorpy setup script
# commands to modify a fresh install of raspbian Lite for use with doorpy

echo "UPDATING DEFAULT INSTALLED PACKAGES"
sudo apt-get update
sudo apt-get -y upgrade

printf '#'%.0s {1..98} ; echo

echo "INSTALLING MINIMUM GUI FOR MESSAGE BOARD"
sudo apt-get install -y --no-install-recommends xserver-xorg x11-xserver-utils xinit openbox

printf '#'%.0s {1..98} ; echo

echo "INSTALLING CHROMIUM FOR MESSAGE BOARD"
sudo apt-get install -y --no-install-recommends chromium-browser

printf '#'%.0s {1..98} ; echo

echo "INSTALLING PYTHON DEPENDENCIES"
sudo apt-get install -y python3 python-pip
pip install Flask

printf '#'%.0s {1..98} ; echo

echo "CHANGING OPENBOX CONFIG FOR X11 SETTINGS WE NEED"
cat configs/openbox-config | sudo tee /etc/xdg/openbox/autostart > /dev/null

printf '#'%.0s {1..98} ; echo

echo "adding startup script to .bash_profile"
cat $HOME/doorpy/configs/startup.sh > $HOME/.bash_profile

printf '#'%.0s {1..98} ; echo

echo "SETUP COMPLETE PLEASE REBOOT"
