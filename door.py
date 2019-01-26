"""
doorpy by Ciaran Farley
https://github.com/cTurtle98/doorpy

program to host a web server with python flask
web server is for a message board system for a bedroom door

"""

from flask import Flask, render_template, request, redirect
import json
import os
import subprocess

# setup dictionaries
configsdict = {}
cardsdict = {}
messagesdict = {}

def load_json_to_dict():\
    # load configs json into dictionary for runtime use
    try:
        f = open("configs.json")
        configsdict = json.load(f)
        f.close
    except:
        print("ERROR! Could not load configs dictionary!")
    # load cards json into dictionary for runtime use
    try:
        f = open("json/cards.json")
        cardsdict = json.load(f)
        f.close
    except:
        print("ERROR! Could not load cards dictionary!")
    
    # load messages json into dictionary for runtime use
    try:
        f = open("json/messages.json")
        messagesdict = json.load(f)
        f.close()
    except:
        print("ERROR! Could not load messages dictionary!")
    
    return cardsdict, messagesdict

cardsdict, messagesdict = load_json_to_dict()
        
# setup the flask enviroment
app = Flask(__name__, template_folder='templates/')

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
        cardsdict[cardnum] = {"A":None, "B":None, "active":"A"}
        return render_template(messagesdict["cardnotfound"]["template"], **messagesdict["cardnotfound"])
    
@app.route('/edit', methods=['GET'])
def edit() :
    ''' remote edit page for messages and cards'''    
    
    return render_template(
        'pages/edit.j2',
        cardsdict=cardsdict,
        messagesdict=messagesdict,
        templateList=os.listdir('templates/').remove('pages'),
    )

@app.route('/editcard', methods=['POST'])
def editcard() :
    ''' takes post request with form values from /edit and saves them to the dict then pushes them to the json files'''
    
    cardsdict[request.form.get('cardnum')] = {
        "nickname" : request.form.get('nickname'),
        "A" :  request.form.get('message_a'),
        "B" :  request.form.get('message_b'),
        "active" : "A"
    }
    
    with open('json/cards.json', 'w') as f:
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
    
    with open('json/messages.json', 'w') as f:
        json.dump(messagesdict, f, indent=4)
    
    return redirect("/edit")

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
        'pages/config.j2',
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
