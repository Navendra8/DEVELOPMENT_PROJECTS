from flask import Flask,render_template

app=Flask(__name__)

@app.route("/")
def index():
    return render_template ("abc.html")

@app.route("/home/<name>/<interest>")
def home(name,interest):
    return render_template("abc.html",n = name,int=interest)



@app.route("/home/<name1>/<name2>/<name3>/")
def your_name(name1,name2,name3):
    d = {
        "Father" : name1,
        "Mother" : name2,
       "Child" : name3
    }
    return render_template("abc.html",{'x':d})
app.run(host="localhost",port=1234,debug=True)