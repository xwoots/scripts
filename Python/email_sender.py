import os
from email.message import EmailMessage
import ssl
import smtplib
from dotenv import load_dotenv

load_dotenv()

sender_address = 'aws.mateuwc@gmail.com'
email_password = os.environ.get('emailPassword')
receiver_address = 'aws.mcoulibaly@gmail.com'

subject = 'Email from Python'
body = """
Bonjour,

Cet email vous est envoyé depuis un script Python.

Cordialement,
Le script Python
"""

em = EmailMessage()
em['From'] = sender_address
em['To'] = receiver_address
em['Subject'] = subject

em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(sender_address, email_password)
    smtp.sendmail(sender_address, receiver_address, em.as_string())
