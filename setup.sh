#!/bin/bash

#doorpy by Ciaran Farley
#https://github.com/cTurtle98/doorpy
# script to setup doorpy on a fresh install of raspbian lite

sep () {
  printf '#'%.0s {1..98} ; echo
}

sep

echo "changing locale and keyboard to US"
locale=en_US.UTF-8
layout=us
sudo raspi-config nonint do_change_locale $locale
sudo raspi-config nonint do_configure_keyboard $layout

sep

echo "enabling ssh"
sudo raspi-config nonint do_ssh 0

sep

echo "enable autologin cli"
sudo raspi-config nonint do_boot_behaviour B2

sep

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
sudo cp -b resources/openbox-config /etc/xdg/openbox/autostart

sep

echo "adding startup script to .bash_profile"
cp -b $HOME/doorpy/resources/startup.sh $HOME/.bash_profile

sep

echo "MONITOR SETTINGS CHANGE"

sudo cp -b $HOME/doorpy/resources/bootconfig /boot/config.txt

sep

echo "CHANGE MOTD"

sudo cp -b $HOME/doorpy/resources/motd /etc/motd

sep

echo "SETUP COMPLETE PLEASE REBOOT"
