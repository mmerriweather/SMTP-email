import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

fromaddr = 'mmerriweather@mccicorp.com'
toaddr = 'mmerriweather@mccicorp.com'
# text = 'test message from Python'
username = 'mmerriweather@mccicorp.com'
password = 'Paru1154'

msg = MIMEMultipart('alternative')
msg ['From'] = fromaddr
msg ['To'] = toaddr
msg ['Subject'] = 'Test'
# optionally, you could point these to some other files on your computer
html_file = "email.html"
plain_file = "plain.txt"

# set the plain text and html parts
plain = ""
html = ""

with open(html_file,"r") as f_html:
	html = f_html.read()
f_html.closed

with open(plain_file,"r") as f_plain:
	plain = f_plain.read()
f_plain.closed

msg.attach(MIMEText(plain, 'plain'))
msg.attach(MIMEText(html, 'html'))


server = smtplib.SMTP('smtp.office365.com:587')
server.ehlo()
server.starttls()
server.ehlo()
server.login(username, password)
server.sendmail(fromaddr, toaddr, msg.as_string())
server.quit()
print 'email sent'