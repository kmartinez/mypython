#!/usr/bin/env python3
# example of using office365 from Python
import smtplib
from email.message import EmailMessage
import getpass

# ask for invisible password entry
password = getpass.getpass("password: ")

fromaddr = "km2@soton.ac.uk"
toaddr = "km@ecs.soton.ac.uk"
msg = EmailMessage()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Test Mail"
body = "email from python using office365"
msg.set_content(body)
server = smtplib.SMTP('smtp.office365.com', 587)
server.ehlo()
server.starttls()
server.login(fromaddr, password)
server.send_message(msg)
server.quit()
