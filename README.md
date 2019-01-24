# doorpy
python flask based web server for message board mounted to my door

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
```sudo raspi-config```

**Localization Options:** select your region and keyboard

**Change User Password** change the password on your pi because everyone knows the defaults and you dont want to be hacked

**Network Options** setup your wifi if you have it

**Boot Options** select "Desktop / cli" and enable "Console Autologin" (we will see why later)

**Interfacing Options** if you will want remote access enable ssh

#### 3) install git

run
```
sudo apt-get install -y git
```

#### 4) clone this github repo into your home folder

```git clone https://github.com/cTurtle98/doorpy.git```

#### 5) run setup script

```bash
./doorpy/setup.sh
```

#### 6) Reboot

reboot your pi and you should be good to go

## customization

changes to make to make this your own

#### message templates

use html/templates/calendar.html as a basis for editing and creating new message templates

#### cards.json and messages.json

access /edit from another computer to register new cards and messages to your system

(if using docker make sure to have a volume link for these files or you will loose then betwen docker reboots)

#### monitor resolution

in html/templates/base.html edit the css with the resolution of the monitor on your message board
```css
#main {
		height: 1366px;
		width: 768px;
		background-color: black;
		text-align: center;
```
