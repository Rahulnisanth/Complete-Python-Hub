# BASIC EMAIL SENDER API USING PYTHON

# importing the required modules for email API :
import smtplib
from email.message import EmailMessage
# importing the string & pathlib for passing the contents in a html file :
from pathlib import Path
from string import Template

# capturing the contents in the targeted template...
html = Template(Path('index.html').read_text())

# email procedures :
email = EmailMessage()
email['from'] = 'Rahul Nisanth'
email['to'] = 'xx--receiver--xx@gmail.com'
email['subject'] = 'You have won a 1,000,000 dollars...'

# setting the email content as similar as the content in the html template...
email.set_content(html.substitute({'name':'TinTin', 'prize':'1,000,000'}))

# ensuring the smtp protocols :
with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('xx--sender--xx@gmail.com', 'xx--password--xx')
    smtp.send_message(email)