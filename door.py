"""
Ciaran Farley
pydoor python program

this program uses python flask to host the sign on my door
"""

from flask import Flask, render_template, request, abort
import json

#enable personal debug messages
DEBUG = True

## THIS BLOCK OF CODE IS BAD AND NEEDS TO BE GONE
try:
    with open("cards.json") as f:
        cardsdict = json.load(f)
except:
    #MINIMAL DICTS FOR TESTING
    cardsdict = {
        #card number 12345
        "12345" : {
            #primary message
            "A" : "home",
            #secondary message
            "B" : "away",
            #was last seen message primary or secondary
            "active" : "A"
        }
    }
## END BAD CODE BLOCK

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
        return render_template(messagesdict["default"]["template"], **messagesdict["default"])
    
    #process scanning a card and retrieving its message
    try:
        if cardsdict[cardnum]['active'] == 'A':
            cardsdict[cardnum]['active'] = 'B'
            return render_template(messagesdict[cardsdict[cardnum]['B']]['template'], **messagesdict[cardsdict[cardnum]['B']])    
        elif cardsdict[cardnum]['active'] == 'B':
            cardsdict[cardnum]['active'] = 'A'
            return render_template(cardsdict[cardnum]['A'],)
    except:
        return render_template(messagesdict["cardnotfound"]["template"], **messagesdict["cardnotfound"])
    
@app.route('/edit')
def edit() :
    ''' this is a route for registering new cards and messages, must be accessed remotely'''

    return abort(404)

if __name__ == '__main__' :
    # WARNING FLASK IS IN DEBUG MODE DISABLE FOR PRODUCTION SERVER
    app.run(debug=True, host='::', port=80)
