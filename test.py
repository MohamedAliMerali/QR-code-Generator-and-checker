# import smtplib

# sender = 'merali.med@gmail.com'
# receivers = ['mirfantom@gmail.com.com']

# message = """
# To: To Person <to@todomain.com>
# Subject: SMTP e-mail test

# This is a test e-mail message.
# """

# try:
#     smtpObj = smtplib.SMTP('localhost')
#     smtpObj.sendmail(sender, receivers, message)
# except:
#     print("Error: unable to send email")

with open("apppassword.txt", "r") as apppass:
    lines = apppass.readline()

import smtplib
import ssl
from email.message import EmailMessage

# Define email sender and receiver
email_sender = 'merali.med@gmail.com'
email_password = lines
email_receiver = 'mirfantom@gmail.com'

# Set the subject and body of the email
subject = 'The Purge has began!'
body = """
This is not a test. This is your emergency broadcast system announcing the commencement of the Annual Purge sanctioned by the U.S Government.
"""

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)

# Add SSL (layer of security)
context = ssl.create_default_context()

# Log in and send the email
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())
