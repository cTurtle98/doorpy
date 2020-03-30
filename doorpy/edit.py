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

edit.py
page for editing the cards and messages

"""

import os

# import dictionaries
from doorpy import configsdict
from doorpy import cardsdict
from doorpy import messagesdict

# import flask enviroment
from doorpy import app

# import jinja renderer
from Flask import render_template

@app.route('/edit', methods=['GET'])
def edit() :
    ''' remote edit page for messages and cards'''    
    
    templateList = os.listdir('templates/')
    templateList.remove('pages')
    
    return render_template(
        'pages/edit.jinja2',
        cardsdict=cardsdict,
        messagesdict=messagesdict,
        templateList=templateList,
    )
