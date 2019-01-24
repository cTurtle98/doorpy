#!/bin/bash
#Ciaran Farley
# doorpy setup script
# commands to modify a fresh install of raspbian Lite for use with doorpy

sep () {
  printf '#'%.0s {1..98} ; echo
}

echo "UPDATING DEFAULT INSTALLED PACKAGES"
sudo apt-get update
sudo apt-get -y upgrade

sep

echo "INSTALLING MINIMUM GUI FOR MESSAGE BOARD"
sudo apt-get install -y --no-install-recommends xserver-xorg x11-xserver-utils xinit openbox


sep

echo "INSTALLING CHROMIUM FOR MESSAGE BOARD"
sudo apt-get install -y --no-install-recommends chromium-browser

sep

echo "INSTALLING PYTHON DEPENDENCIES"
sudo apt-get install -y python3 python3-pip
pip3 install Flask

sep

echo "CHANGING OPENBOX CONFIG FOR X11 SETTINGS WE NEED"
cat configs/openbox-config | sudo tee /etc/xdg/openbox/autostart > /dev/null

sep

echo "adding startup script to .bash_profile"
cat $HOME/doorpy/configs/startup.sh > $HOME/.bash_profile

sep

echo "MONITOR SETTINGS CHANGE"

cat $HOME/doorpy/configs/bootconfig | sudo tee /boot/config.txt > /dev/null

sep

echo "CHANGE MOTD"

cat $HOME/doorpy/configs/motd | sudo tee /etc/motd > /dev/null

sep

echo "SETUP COMPLETE PLEASE REBOOT"
