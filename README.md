# doorpy

raspberry pi message board for your door

**only raspbian on a raspberry pi supported**

## Copyright (C) 2020  Ciaran Farley (ciaran@cturtle98.com)

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License along
with this program; if not, write to the Free Software Foundation, Inc.,
51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

## Features

sets up pi with just enough gui for chromium in fullscreen kiosk mode

runs a web server built with python flask for gerating the messages

scan any card on any HID device type card reader to register it into your cards list

on another computer visit `<pi-IP>:8080/edit` to use my editor for the cards and messages

customize messages and add more message templates for more html than you want in the json

## setup

#### 1) Raspbian

Download raspbian Lite and burn it to the SD card for pi you are using
https://www.raspberrypi.org/downloads/raspbian/

#### 2) First boot

boot up the pi and login with 
```
user: pi
pass: raspberry
```

do the first time setup by running 
```bash
sudo raspi-config
```

**Localization Options:** select your region and keyboard

**Change User Password** change the password on your pi because everyone knows the defaults and you dont want to be hacked

**Network Options** setup your wifi if you have it

**Boot Options** select "Desktop / cli" and enable "Console Autologin" (we will see why later)

**Interfacing Options** if you will want remote access enable ssh

#### 3) install git

run
```bash
sudo apt-get install -y git
```

#### 4) clone this github repo into your home folder

```bash
cd ~
git clone https://github.com/cTurtle98/doorpy.git
```

#### 5) run setup script

```bash
~/doorpy/setup.sh
```
if this is a fresh pi you can ignore the warning message and hit ENTER

#### 6) Reboot

reboot your pi and take note of its IP address printed in the startup text scroll

#### 7) customization

use another computer on your network to visit the following web addresses

<pi-ip> is the ip address you noted from the startup text scroll

`<pi-ip>:8080/edit` editor for cards and messages

(future feature)
`<pi-ip>:8080/config` editor for configs.json

