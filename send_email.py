import smtplib, ssl


def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = "sanjayredmi1s@gmail.com"
    password = "Sanj@y1408"

    receiver = "sanjayredmi1s@gmail.com"
    context = ssl.create_default_context()

    message = """
    Hi how are you 
    """

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)

    print('hello')