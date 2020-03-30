"""
doorpy - raspberry pi message board for your door
Copyright (C) 2020  Ciaran Farley (ciaran@cturtle98.com)

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

--------

editmessage.py
server path to handle message editing

"""

from flask import request, redirect
import json

from doorpy import app

from doorpy import messagesdict

@app.route('/editmessage', methods=['POST'])
def editmessage() :
    ''' takes post request with form values from /edit and saves them to the dict then pushes them to the json files'''
    
    messagename = request.form.get('messageName')
    
    if messagesdict.get(messagename) == None:
        messagesdict[request.form.get('messageName')] = {
            "template" : request.form.get('messageTemplate'),
            "messageType" : request.form.get('messageType'),
            "messageSubject" : request.form.get('messageSubject'),
            "messageStatus" : request.form.get('messageStatus')
        }
    else:
        if request.form.get('messageTemplate') != "":
            messagesdict[messagename]["template"] = request.form.get('messageTemplate')
    
        if request.form.get('messageType') != "":
            messagesdict[messagename]["messageType"] = request.form.get('messageType')
    
        if request.form.get('messageSubject') != "":
            messagesdict[messagename]["messageSubject"] = request.form.get('messageSubject')
    
        if request.form.get('messageStatus') != "":
            messagesdict[messagename]["messageStatus"] = request.form.get('messageStatus')
    
    
    with open('json/messages.json', 'w') as f:
        json.dump(messagesdict, f, indent=4)
    
    return redirect("/edit")
