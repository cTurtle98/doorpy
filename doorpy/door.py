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

door.py
flask code to render the page displayed on the door

"""

# import the flask enviroment
from doorpy import app

# import dictionaries
from doorpy import cardsdict
from doorpy import messagesdict

# library to render jinja templates to html
from flask import render_template

# library to get the args from the client
from flask import request

@app.route('/')
def index() :
    '''door page'''
    
    #retrieve cardnum from html form
    cardnum = request.args.get('card')
    
    #if you havent scanned a card yet display a page telling you to
    if cardnum == None:
        cardnum = "default"
    
    #process scanning a card and retrieving its message
    try:
        if cardsdict[cardnum]['active'] == 'A':
            cardsdict[cardnum]['active'] = 'B'
            return render_template(messagesdict[cardsdict[cardnum]['B']]['template'], **messagesdict[cardsdict[cardnum]['B']])    
        elif cardsdict[cardnum]['active'] == 'B':
            cardsdict[cardnum]['active'] = 'A'
            return render_template(messagesdict[cardsdict[cardnum]['A']]['template'], **messagesdict[cardsdict[cardnum]['A']])
    except:
        cardsdict[cardnum] = {"A":None, "B":None, "active":"A"}
        return render_template(messagesdict["cardnotfound"]["template"], **messagesdict["cardnotfound"])
    
