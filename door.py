"""
Ciaran Farley
doorpy

this program uses python flask to host the sign on my door
"""

from flask import Flask, render_template, request, redirect
import json
import os
import subprocess

#enable personal debug messages
DEBUG = True

# load cards json into dictionary for runtime use
try:
    with open("cards.json") as f:
        cardsdict = json.load(f)
except:
    cardsdict = {}
    print("ERROR! Could not load cards dictionary!")

# load messages json into dictionary for runtime use
try:
    f = open("messages.json")
    messagesdict = json.load(f)
    f.close()
except:
    messagesdict = {}
    print("ERROR! Could not load messages dictionary!")

# setup the flask enviroment
app = Flask(__name__, template_folder='html/templates/')

@app.route('/')
def index() :
    '''this is the main route that the kiosk pi will be looking at'''
    
    #retrieve cardnum from html form
    cardnum = request.args.get('card')
    
    #if you havent scanned a card yet display a page telling you to
    if cardnum == None:
        cardnum = "default"
#        return render_template(messagesdict["default"]["template"], **messagesdict["default"])
    
    #process scanning a card and retrieving its message
    try:
        if cardsdict[cardnum]['active'] == 'A':
            cardsdict[cardnum]['active'] = 'B'
            return render_template(messagesdict[cardsdict[cardnum]['B']]['template'], **messagesdict[cardsdict[cardnum]['B']])    
        elif cardsdict[cardnum]['active'] == 'B':
            cardsdict[cardnum]['active'] = 'A'
            return render_template(messagesdict[cardsdict[cardnum]['A']]['template'], **messagesdict[cardsdict[cardnum]['A']])
    except:
        return render_template(messagesdict["cardnotfound"]["template"], **messagesdict["cardnotfound"])
    
@app.route('/edit', methods=['GET'])
def edit() :
    ''' remote edit page for messages and cards'''
    
    
    
    return render_template(
        'edit.html',
        cardsdict=cardsdict,
        messagesdict=messagesdict,
        templateList=os.listdir('html/templates/'),
    )

@app.route('/editcard', methods=['POST'])
def editcard() :
    ''' takes post request with form values from /edit and saves them to the dict then pushes them to the json files'''
    
    cardsdict[request.form.get('cardnum')] = {
        "A" :  request.form.get('message_a'),
        "B" :  request.form.get('message_b'),
        "active" : "A"
    }
    
    with open('cards.json', 'w') as f:
        json.dump(cardsdict, f, indent=4)
    
    return redirect("/edit")

@app.route('/editmessage', methods=['POST'])
def editmessage() :
    ''' takes post request with form values from /edit and saves them to the dict then pushes them to the json files'''
    
    messagesdict[request.form.get('messageName')] = {
        "template" : request.form.get('messageTemplate'),
        "messageType" : request.form.get('messageType'),
        "messageSubject" : request.form.get('messageSubject'),
        "messageStatus" : request.form.get('messageStatus')
    }
    
    with open('messages.json', 'w') as f:
        json.dump(messagesdict, f, indent=4)
    
    return redirect("/edit")

"""
@app.route('/gitpush', methods=['POST'])
def gitpush() :
    
    print('PUSHING JSON FILES TO GITHUB')
    
    return abort(500)

@app.route('/reload', methods=['POST'])
def reload() :
    
    subprocess.run("$HOME/doorpy/configs/reload.sh", shell=True)
    
    return redirect('/edit')
"""

if __name__ == '__main__' :
    app.run(
        # WARNING FLASK IS IN DEBUG MODE DISABLE FOR PRODUCTION SERVER
        debug=True,
        host='::',
        port=8080
    )
