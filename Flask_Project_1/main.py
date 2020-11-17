from flask import Flask,render_template,request,make_response
import pymysql as sql
import smtplib,ssl
from email.mime.multipart  import MIMEMultipart
from email.mime.text import MIMEText
import os
from flask import redirect
import requests


app = Flask(__name__)


@app.route("/")
def main():
  
    return render_template("firstpage.html")

@app.route("/login/")
def login():
   
    return render_template("login.html")

@app.route("/signup/")
def signup():
  
    return render_template ("signup.html")

@app.route("/fun2/")
def fun():
    
    return render_template ("fun2.html")

@app.route("/firstpage/")
def first_page():
   
    return render_template ("firstpage.html")

@app.route("/about_us/")
def aboutus():
   
    return render_template ("about_us.html")

@app.route("/cart/")
def cart():
   
    return render_template ("cart.html")

@app.route("/logout/")
def logout():
    
    resp = make_response(render_template("firstpage.html"))
    resp.delete_cookie("email")
    resp.delete_cookie("islogin")
    return resp


@app.route("/afterlogin/",methods=['POST','GET'])
def afterlogin():
    if request.method == "POST":
        email=request.form.get("email")
        password=request.form.get("password")
        try:
            db=sql.connect(host="localhost",port=3306,user="root",password="",database="myweb")
            cursor= db.cursor()
            cmd=f"select * from myweb where email='{email}'"
            cursor.execute(cmd)
            data=cursor.fetchone()
            if data:
                if data[3]==password:
                    resp=make_response(render_template("afterlogin.html"))
                    resp.set_cookie("email",email)
                    resp.set_cookie("islogin","true")
                    return resp
                else:
                    error = "Password Doesn't match...."
                    return render_template ("login.html",error=error)
                
            else:
                error="Invalid user"
                return render_template ("login.html",error=error)
        
        except Exception as e:
            return f"{e}"
    else:
        return render_template("login.html")




@app.route("/message/",methods=['GET','POST'])
def message():
    if request.method == "POST":
        email= request.form.get ("email1")
        message = request .form.get ("message1")
        db =sql.connect(host="localhost",port =3306,user ="root",password="",database="myweb")
        cursor=db.cursor()
        cmd=f"insert into myweb_message values('{email}','{message}')"
        cursor.execute(cmd)
        db.commit()
        return render_template ("firstpage.html")
    else:
        return render_template ("firstpage.html")

@app.route ("/aftersignup/",methods=['GET','POST'])
def aftersignup():
    if request.method == "POST":
        firstname=request.form.get("firstname")
        lastname=request.form.get("lastname")
        email= request.form.get("email")
        password=request.form.get("password")
        address=request.form.get("address")
        address2=request.form.get("address2")
        city=request.form.get("city")
        state=request.form.get("state")
        pincode=request.form.get("pincode")
        try:
            db =sql.connect(host="localhost",port =3306,user ="root",password="",database="myweb")
            cursor=db.cursor()
            cmd=f"select * from myweb where email = '{email}'"
            cursor.execute(cmd)
            data=cursor.fetchone()
            if data:
                error= "Email already exist ..."
                return render_template("signup.html",error=error)
            else:
                s=0
                l=0
                u=0
                n=0
                if len(password) >=8:
                    for i in password:
                        if i.isupper():
                            u+=1
                        if i.islower():
                            l+=1
                        if i.isnumeric():
                            n+=1

                        if i in ["@","#","£","*","&",".","+","^","$","!"]:
                            s+=1

                    else:
                        if s>=1 and l>=1 and u>=1 and n>1:
                            from_email = "navendra8@gmail.com"
                            to_email = email
                            p = "Dipu8991"
                            message = MIMEMultipart("alternative")
                            message["Subject"] = "Mail for your account activation"
                            message["To"] = to_email
                            message["From"] = from_email

                            html = """
                                <h1 style='color:red'>Your activation link is as follows</h1>
                                <a href="http://localhost:1234/afterlogin/">CLient on this link<a>
                                """
                            msg = MIMEText(html,"html")
                            message.attach(msg)
                            context = ssl.create_default_context()
                            with smtplib.SMTP_SSL("smtp.gmail.com",465,context=context) as server:
                                server.login(from_email,p)
                                server.sendmail(from_email,to_email,message.as_string())
                                cmd=f"insert into myweb values('{firstname}','{lastname}','{email}','{password}','{address}','{address2}','{city}','{state}','{pincode}')"
                                cursor.execute(cmd)
                                db.commit()
                                error="Login to continue......."
                                return render_template("login.html",error=error)

                            return render_template ("login.html")
                        else:
                            error =" Password does not meet the requirement "
                            return render_template("signup.html",error=error)
                else:
                    error="Password must be minimum 8 character long"
                    return render_template("signup.html",error=error)
        except Exception as e:
            return f"{e}"

    else:
        return render_template("signup.html")



@app.route("/pollution_meter/",methods=['GET','POST'])
def pollution_meter():
    if request.method == "GET":
        return render_template("pollution_meter.html")
    elif request.method == "POST":
        city= request.form.get("city")
        api_key="b6b641a4bf2a0ae493c2d452d0eb5eff1ca32ed9"
        url=f"https://api.waqi.info/feed/{city}/?token={api_key}"
        data=requests.get(url)
        if data.status_code==200:
            data=data.json()
            d = u"\N{DEGREE SIGN}"
            Name=data['data']['city']['name']
            temprature=round(data['data']['iaqi']['t']['v'],2)
            airpollution=round(data['data']['iaqi']['pm25']['v'],2)
            humidity=round(data['data']['iaqi']['h']['v'],2)
            localtime=data['data']['time']['s'][-8:]
            date=data['data']['time']['s'][0:10]
            timezone=data['data']['time']['tz']
            weather= {
                "Location":Name,
                "LastUpdated Date":date,
                "LastUpdated Time":localtime,
                "TimeZone":timezone,
                "Temperature":temprature,
                "AQI":airpollution,
                "Humidity":humidity,
                }
            return render_template("pollution_meter.html",data=weather)
            
    @app.route("/pollution_meter/",methods=['GET','POST'])
    def carbon_footprint():
        if request.method=="GET":
            return render_template ("Pollution_meter.html")
        elif request.method == "POST":
            fuel= request.form.get("fuel")
            liters=request.form.get("liters")
            url = "https://carbonfootprint1.p.rapidapi.com/FuelToCO2e"

            querystring = {"type":{fuel},"litres":liters}

            headers = {
                'x-rapidapi-host': "carbonfootprint1.p.rapidapi.com",
                'x-rapidapi-key': "5eeb1e148amsh67824ebcafb1348p1d1c15jsncfb7a2cbf97f"
                }


            
            if response.status_code == 200:
                data1=response.json()
                output=data1['carbonEquivalent']
                final={
                    "KgEmmission" : output
                }
        return render_template ("pollution_meter.html",data=output)

        






app.run(host="localhost",port=1234,debug=True)