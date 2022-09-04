from email.message import EmailMessage
from app2 import password
import ssl
import smtplib

email_sender = 'ashishsubedi18@gmail.com'
email_password = password

email_receiver = 'hafope4205@seinfaq.com'

subject = "Thank you for applying for this post"
body = """
We received your application,currently we are reviewing your cv and we will contact you asap
"""
em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['subject'] = subject
em.set_content(body)

context = ssl.create_default_context()
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())
