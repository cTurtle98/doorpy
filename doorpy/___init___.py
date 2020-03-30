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

___init___.py
init file to setup flask enviroment and global variables

"""

from flask import Flask, render_template, request, redirect
import os
import subprocess
import sys

# setup dictionaries
configsdict = {}
cardsdict = {}
messagesdict = {}

# import json dictionary loader
from doorpy import load_json_to_dict

#load dictionaries
cardsdict, messagesdict = load_json_to_dict()
        
# setup the flask enviroment
app = Flask(__name__, template_folder='templates/')

import doorpy.door
import doorpy.edit

import doorpy.editcard
import doorpy.editmessage

"""
@app.route('/gitpush', methods=['POST'])
def gitpush() :
    
    print('PUSHING JSON FILES TO GITHUB')
    
    return abort(500)

"""
@app.route('/reload', methods=['POST'])
def reload() :
    
    subprocess.run("$HOME/doorpy/resources/reload.sh", shell=True)
    
    cardsdict, messagesdict = load_json_to_dict()
    
    return redirect('/edit')

@app.route('/config', methods=['GET'])
def config() :
    ''' config editor page '''
    return render_template(
        'pages/config.jinja2',
        configsdict = configsdict
    )

@app.route('/config', methods=['POST'])
def configpost():
    
    configsdict = {
    }
    
    return redirect('/config')

if __name__ == '__main__' :
    app.run(
        # WARNING FLASK IS IN DEBUG MODE DISABLE FOR PRODUCTION SERVER
        debug=True,
        host='::',
        port=8080
    )
return app
