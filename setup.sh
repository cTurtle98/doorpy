#!/bin/bash
#Ciaran Farley
# doorpy setup script
# commands to modify a fresh install of raspbian Lite for use with doorpy

echo "UPDATING DEFAULT INSTALLED PACKAGES"
sudo apt-get update
sudo apt-get -y upgrade

echo "INSTALLING MINIMUM GUI FOR MESSAGE BOARD"
sudo apt-get install -y --no-install-recommends xserver-xorg x11-xserver-utils xinit openbox

echo "INSTALLING CHROMIUM FOR MESSAGE BOARD"
sudo apt-get install -y --no-install-recommends chromium-browser

echo "CHANGING OPENBOX CONFIG FOR X11 SETTINGS WE NEED"
echo '''
# Disable any form of screen saver / screen blanking / power management
xset s off
xset s noblank
xset -dpms

# Allow quitting the X server with CTRL-ATL-Backspace
setxkbmap -option terminate:ctrl_alt_bksp

# Start Chromium in kiosk mode
sed -i 's/"exited_cleanly":false/"exited_cleanly":true/' ~/.config/chromium/'Local State'
sed -i 's/"exited_cleanly":false/"exited_cleanly":true/; s/"exit_type":"[^"]\+"/"exit_type":"Normal"/' ~/.config/chromium/Default/Preferences
chromium-browser --disable-infobars --kiosk 'http://localhost:8080'
''' > /etc/xdg/openbox/autostart

echo "ENABLING AUTOMATIC GUI MODE"
echo '''
[[ -z $DISPLAY && $XDG_VTNR -eq 1 ]] && startx -- -nocursor
''' >> $HOME/.bash_profile

echo "ENABLING AUTOMATIC PYTHON SERVER START"
echo '''
git pull doorpy &&\
python3 doorpy/door.py &
''' >> $HOME/.bash_profile
