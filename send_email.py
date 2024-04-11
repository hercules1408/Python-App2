import smtplib, ssl
import os


def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = "sa22222s@gmail.com"
    password = "222222222"

    receiver = "san222222s@gmail.com"
    context = ssl.create_default_context()

    message = """
    Hi how are you 
    """

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)

    print('hello')