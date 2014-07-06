import smtplib
from email.MIMEText import MIMEText

fromaddr = 'mmerriweather@mccicorp.com'
toaddr = 'mmerriweather@mccicorp.com'
text = 'test message from Python'
username = 'mmerriweather@mccicorp.com'
password = 'Paru1154'
msg = MIMEMultipart()
msg ['From'] = fromaddr
msg ['To'] = toaddr
msg ['Subject'] = 'Test'
msg.attach(MIMEText(text))
server = smtplib.SMTP('smtp.office365.com:587')
server.ehlo()
server.starttls()
server.ehlo()
server.login(username, password)
server.sendmail(fromaddr, toaddr, msg.as_string())
server.quit()