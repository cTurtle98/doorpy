#!/bin/bash
#Ciaran Farley
# doorpy setup script
# commands to modify a fresh install of raspbian Lite for use with doorpy

sudo apt-get update
sudo apt-get -y upgrade

sudo apt-get install -y --no-install-recommends xserver-xorg x11-xserver-utils xinit openbox

sudo apt-get install -y --no-install-recommends chromium-browser

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

echo '''
[[ -z $DISPLAY && $XDG_VTNR -eq 1 ]] && startx -- -nocursor
''' >> $HOME/.bash_profile

echo '''
python3 doorpy/door.py &
''' >> $HOME/.bash_profile
