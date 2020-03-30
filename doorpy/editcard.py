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

editcard.py
serverside handler for card editing

"""

from flask import request, redirect

#import flask enviroment
from doorpy import app

from doorpy import cardsdict

@app.route('/editcard', methods=['POST'])
def editcard() :
    ''' takes post request with form values from /edit and saves them to the dict then pushes them to the json files'''
    
    cardnum = request.form.get('cardnum')
    
    if cardsdict.get(cardnum) == None:
        cardsdict[request.form.get('cardnum')] = {
          "nickname" : request.form.get('nickname'),
          "A" :  request.form.get('message_a'),
          "B" :  request.form.get('message_b'),
            "active" : "A"
        }
    else:
        if request.form.get('nickname') != "":
            cardsdict[cardnum]["nickname"] = request.form.get('nickname')
        
        if request.form.get('message_a') != "":
            cardsdict[cardnum]["A"] = request.form.get('message_a')
    
        if request.form.get('message_b') != "":
            cardsdict[cardnum]["B"] = request.form.get('message_b')
    
        cardsdict[cardnum]["active"] = "B"
    
    with open('json/cards.json', 'w') as f:
        json.dump(cardsdict, f, indent=4)
    
    return redirect("/edit")
