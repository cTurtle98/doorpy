"""
pydoor python program

this program uses python flask to host the sign on my door
"""

from flask import Flask, render_template, request
import json
from os import listdir
from os.path import isfile, join
class SignOnDoor:
    """
    python has some weird things goin on with scope.
    I created a class to force the use of SignOnDoor.mostRecentCard
    rather than some index() local variable that gets created in-place
    """

    #enable personal debug messages
    DEBUG = True

    app = Flask(__name__, template_folder='html/templates/')
    mostRecentCard = {}  # tracks which card was most recently handed to the Raspi Sign
    extraMode = False # trakcs if template should be augmented with ModeB, or standard ModeA (+/- calendar)
    cardsdict = {}
    try:
        # load card pages from cards.json
        f = open("cards.json")
        cardsdict = json.load(f)
        print("DEBUG: cardsdict contents: ", cardsdict)
    except:
        print("an error has occurred!")
    @app.route('/')
    def index():
        #TODO: Unset this string assignment. This was just for testing without the card reader
        #TODO: ensure form data is aquired correctly
        cardnum = "card1" # request.args.get("card") # request card number from Raspi Sign
        
        if SignOnDoor.DEBUG:
            print("DEBUG: cardnum = ", cardnum)
            print("DEBUG: cardnum type = ", type(cardnum))
            print("DEBUG: app type = ", type(SignOnDoor.app))
        try:  # surround with try-except to handle card-not-found errors
        # if there was no mostRecentCard (server has just started), display a prompt to swipe first one!
            if(SignOnDoor.mostRecentCard == {}):  # <--- This here is why there is a class, now
                SignOnDoor.mostRecentCard = SignOnDoor.cardsdict[cardnum] # assign first setting
                return render_template('pleasescan.html')
            # if card has been swiped 2x in a row, toggle the extra mode
            if SignOnDoor.cardsdict[cardnum] == SignOnDoor.mostRecentCard:
                SignOnDoor.extraMode = not SignOnDoor.extraMode
            else: # if its a different card, then reset to False
                SignOnDoor.extraMode = False
            # use the template associated with this card,
            # pass in its dictionary of properties 
            # (keys are used as Jinja2 variable names, and the values are of course values)
            # add withCalendar keyword argument
            print("DEBUG: Rendering card with properties: ", SignOnDoor.cardsdict[cardnum])
            return render_template(SignOnDoor.cardsdict[cardnum]["template"], **SignOnDoor.cardsdict[cardnum], withCalendar=SignOnDoor.extraMode)
            # passing in parameters this way allows for unlimited length lists of parameters (or until RAM caps out, anyway)        
    
        except KeyError: # handle invalid card values by showing error
            return render_template('basicmessage.html', title="Invalid Card", status="Card is Invalid")
        
    @app.route('/edit')
    def edit() :
        mypath = "html/templates/"
        files = [f for f in listdir(mypath) if isfile(join(mypath, f))]
        files.remove("base.html")
        files.remove('template.html')
        
        if DEBUG:
            print(files)
            
        return str(files)

if __name__ == '__main__' :
    # WARNING FLASK IS IN DEBUG MODE DISABLE FOR PRODUCTION SERVER
    SignOnDoor.app.run(debug=True, host='::', port=2580)
