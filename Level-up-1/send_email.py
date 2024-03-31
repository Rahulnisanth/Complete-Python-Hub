import smtplib # importing the smtplib module for sending email as server

SENDER_EMAIL = 'xxxxxx@gmail.com'
SENDER_PASSWORD = '1234567abc'

def send_email(receiver, subject, body):
    message = f'Subject : {subject} \n\n {body}' # Enhancing the contents in one variable
    with smtplib.SMTP('smtp.microsoft365.com', 587) as server:
        server.starttls() # Starting the transport layer security
        server.login(SENDER_EMAIL, SENDER_PASSWORD) # Signing in as the sender
        server.sendmail(SENDER_EMAIL, receiver, message) # Sending email to receiver


