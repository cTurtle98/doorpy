# doorpy
python flask based web server for message board mounted to my door

## customization

changes to make to make this your own

* #### message templates

use html/templates/calendar.html as a basis for editing and creating new message templates

* #### cards.json and messages.json

access /edit from another computer to register new cards and messages to your system

(if using docker make sure to have a volume link for these files or you will loose then betwen docker reboots)

* #### monitor resolution

in html/templates/base.html edit the css with the resolution of the monitor on your message board
```css
#main {
		height: 1366px;
		width: 768px;
		background-color: black;
		text-align: center;
```
