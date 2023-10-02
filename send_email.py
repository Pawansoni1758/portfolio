import smtplib, ssl
import os


def send_email(message):
    host = "smtp.gmail.com"
    port = 465
    username = "pawan2004soni@gmail.com"
    password = os.getenv("PASSWORD")

    # password = os.getenv("pas_word")
    receiver = "pawan2004soni@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context)as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)