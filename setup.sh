#!/bin/bash
#Ciaran Farley
# doorpy setup script
# commands to modify a fresh install of raspbian Lite for use with doorpy

sep () {
  printf '#'%.0s {1..98} ; echo
}

sep
sep
echo "WARNING THIS SCRIPT CHANGES SYSTEM FILES TO ONLY HAVE MY CONFIGURATIONS"
echo
echo "IF YOU HAME MODIFIED YOUR SYSTEM FILES PLEASE MAKE A BACKUP FIRST BEFORE RUNNING THIS FILE SO YOU CAN COPY YOUR CHANGES BACK INTO YOUR FLES AFTER THIS SCRIPT IS COMPLETE"
echo
echo "HIT CTRL+C TO QUIT OR ENTER TO CONTINUE"
read

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
sudo cp configs/openbox-config /etc/xdg/openbox/autostart

sep

echo "adding startup script to .bash_profile"
cp $HOME/doorpy/configs/startup.sh $HOME/.bash_profile

sep

echo "MONITOR SETTINGS CHANGE"

sudo cp $HOME/doorpy/configs/bootconfig /boot/config.txt

sep

echo "CHANGE MOTD"

sudo cp $HOME/doorpy/configs/motd /etc/motd

sep

echo "SETUP COMPLETE PLEASE REBOOT"
