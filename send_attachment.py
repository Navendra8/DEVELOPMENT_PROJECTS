
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase 
from getpass import getpass
from email import encoders

from_email = "simrangrover5@gmail.com"
to_email = "simrangrover5@gmail.com"
password = getpass("password : ")

message = MIMEMultipart("alternative")
message["Subject"] = "Mail through Python script"
message["To"] = to_email
message["From"] = from_email

html = """

<p style='color:red;font-style:italoc;font-family:sans serif;font-size:30px'>This is decorative email send</p>
<img src = 'https://www.success.com/wp-content/uploads/legacy/sites/default/files/10_16.jpg'>
"""

m = MIMEText(html,"html")
filename = "C://internship//frontend.pptx"
f = filename.split("//")[-1]
attachment = open(filename,'rb')
p = MIMEBase("application","octet-stream")
p.set_payload((attachment).read()) 
encoders.encode_base64(p)
p.add_header('Content-Disposition', f"attachment; filename= {f}")

message.attach(m)
message.attach(p)

context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com",465,context=context) as server:
    server.login(from_email,password)
    server.sendmail(from_email,to_email,message.as_string())
    
