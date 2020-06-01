import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

fromadd = 'sender_email'
toadd = 'reciever_emailaddress'

msg = MIMEMultipart()
msg['FROM'] = fromadd
msg['TO'] = toadd
msg['SUBJECT'] ='TEST SUBJECT'
body = 'TEST Body'
msg.attach(MIMEText(body,'plain'))
filename='your file name with extension'
attachment = open(r'fiull file_path','rb')
p = MIMEBase('application', "pdf", Name=filename)
p.set_payload((attachment).read())
encoders.encode_base64(p)
p.add_header('Content-Disposition','attachment; filename= %s' % filename)
msg.attach(p)
s=smtplib.SMTP('smtp.gmail.com', 587)
s.ehlo()
s.starttls()
s.login(fromadd,'your password')
text=msg.as_string()
s.sendmail(fromadd,toadd,text)
s.quit()
print("Email sent!")

