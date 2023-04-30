from flask import Flask,render_template,request
import pymysql as sql

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login/")
def login():
    return render_template ("login.html")

@app.route("/signup/")
def signup():
    return render_template("signup.html")

@app.route("/afterlogin/",methods=['POST','GET'])
def afterlogin():
    if request.method=='POST':
        email=request.form.get("email")
        password=request.form.get("password")

        try:
            db=sql.connect(host="localhost",port=3306,database="navendraproject",user="root",password="")
            cursor = db.cursor()
            cmd=f"select * from users where email='{email}'"
            cursor.execute(cmd)
            data =cursor.fetchone()
            
            if data:
                if data[1]  == password:
                    return render_template("abc.html")

            else:
                error = "password doesn't match"
                return render_template("login.html",error=error)

        except Exception as e:
            return f"{e}"
        
    else:
        return render_template ("login.html")


@app.route("/aftersignup/",methods=['GET','POST'])
def aftersignup():
    if request.method=="POST":
        email=request.form.get("email")
        password=request.form.get("passwd")
        gender=request.form.get("gender")
        try:
            db = sql.connect(host="localhost",port=3306,user="root",password="",database="navendraproject")
            cursor=db.cursor()
            cmd=f"select * from users where email = '{email}'"
            cursor.execute(cmd)
            data =cursor.fetchone()
            if data: #if email already present then true else false;
                error="Email already exists"
                return render_template ("signup.html",error = error)

            else:
                cmd = f"insert into users values ('{email}','{password}','{gender}')"
                cursor.execute(cmd)
                db.commit()
                error="Login to continue......"
                return render_template ("login.html",error = error)
        except Exception as e:
            return f"{e}"
            
    else:
        return render_template("signup.html")

app.run(host="localhost",port=1234,debug=True)