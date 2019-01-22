"""
pydoor python program

this program uses python flask to host the sign on my door
"""

from flask import Flask, render_template, request
import json

try:
    with open("cards.json") as f:
        cardsdict = json.load(f)
except:
    cardsdict = []

app = Flask(__name__, template_folder='html/templates/')

@app.route('/')
def index() :
    cardnum = request.args.get('card')
    if cardnum == "None":
        return render_template('pleasescan.html',)
    
    elif cardsdict[cardnum]['active'] == 'A':
        cardsdict[cardnum]['active'] = 'B'
        return render_template(cardsdict[cardnum]['B'],)
    
    elif cardsdict[cardnum][active] == 'B':
        cardsdict[cardnum][active] = 'A'
        return render_template(cardsdict[cardnum]['A'],)
    
    else:
        return render_template('cardnotfound.html',)
    

if __name__ == '__main__' :
    app.run(host='::', port=80)
