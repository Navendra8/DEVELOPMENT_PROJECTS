from flask import Flask
app =Flask (__name__)
@app.route("/")
def index():
    return "Hello World Enter to my world"


@app.route("/home/")
def home():
    return "<h1 style = 'color:red'>Welcome to my python</h1>"

@app.route("/home/myhome")
def myhome():
    return """<h1>WELCOME TO MY WORLD OF PYTHON</h1>
              <p style = 'color:green'>Anshul</p>
    """

@app.route("/home/<name>")
def welcome(name):
    return f"<h1 style ='color:coral; font-style:italic'>Welcome {name} to flask</h1>"


@app.route("/home/<name>/<int:marks>")
def marks(name,marks):
    return f"<h1 style ='color:coral; font-style:italic'>Welcome {name}  and marks {marks} to flask</h1>"





app.run(host="localhost",port=1234,debug=True)