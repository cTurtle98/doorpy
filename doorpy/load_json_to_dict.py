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

load_json_to_dict.py
helper function to load in the dictionaries

"""

import json

#import dictionaries
from doorpy import cardsdict
from doorpy import messagesdict
from doorpy import configsdict

def load_json_to_dict():
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
    try:
      print("custom cards not found, attempting to load default-cards")
      f = open("json/default-cards.json")
      cardsdict = json.load(f)
      f.close
    except:
      print ("default cards not found please git pull to download them")
    
  # load messages json into dictionary for runtime use
  try:
    f = open("json/messages.json")
    messagesdict = json.load(f)
    f.close()
  except:
    try:
      print("custom messages not found, attempting to load default-messages")
      f = open("json/default-messages.json")
      cardsdict = json.load(f)
      f.close
    except:
      print ("default messages not found please git pull to download them")
    
  return cardsdict, messagesdict
