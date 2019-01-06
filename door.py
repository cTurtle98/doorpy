"""
pydoor python program

this program uses python flask to host the sign on my door
"""

from flask import Flask, render_template,

app = Flask(__name__, template_folder='html/templates/')



if __name__ == '__main__' :
    app.run(host='::', port=80)
