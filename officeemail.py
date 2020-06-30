#!/usr/bin/env python3
# example of using office365 from Python
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
import getpass

# ask for invisible password entry
password = getpass.getpass("password: ")

fromaddr = "km2@soton.ac.uk"
toaddr = "km@ecs.soton.ac.uk"
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Test Mail"
body = "Test mail from python using office365"
msg.attach(MIMEText(body, 'plain'))
server = smtplib.SMTP('smtp.office365.com', 587)
server.ehlo()
server.starttls()
server.login(fromaddr, password)
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()
