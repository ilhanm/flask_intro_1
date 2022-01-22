#
#File created to test and see Flask url paths
#

from distutils.log import debug
from flask import Flask

app=Flask(__name__)

@app.route("/")
def index():
    return f"Welcome to index page"

@app.route("/users/<name>")
def hello_world(name):
    return f"Hello {name}"

@app.route("/users/<name>/<int:id>")
def hello_world2(name,id):
    return f"Hello {name}, your id is {id}"

@app.route("/users/<name>/<midname>")
def hello_world3(name,midname):
    return f"Hello {name}, your mid name is {midname}"

@app.route("/info/<path:name>")
def hello_world4(name):
    return f"Hello {name}"

app.run(debug=1)