import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders
import os
gmail_user = input("enter mail id:") #enter your gmail username
gmail_pwd = input("enter passcode:") #enter your passwd
to =[x for x in input("enter mail id").split(',')]#enter to whom you want to send
subject = input("enter the subject:")
text = input("enter the text you want to send:")
attach=input("enter file's path:")
#give your attachment name
msg = MIMEMultipart()
msg['From'] = gmail_user
msg['To'] = ", ".join(to)
msg['Subject'] = subject
msg.attach(MIMEText(text))
part = MIMEBase('application', 'octet-stream')
part.set_payload(open(attach, 'rb').read())
encoders.encode_base64(part)
part.add_header('Content-Disposition','attachment; filename="%s"' % os.path.basename(attach))
msg.attach(part)
mailServer = smtplib.SMTP("smtp.gmail.com",587)
mailServer.starttls()
mailServer.login(gmail_user, gmail_pwd)
mailServer.sendmail(gmail_user, to, msg.as_string())
mailServer.close() 
