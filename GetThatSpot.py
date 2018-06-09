import requests
import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


host = "meetup.com"
api_key = ""

urlname = ""
event_id = ""

rsvp_limit = 16


def send_email():

    msg = MIMEMultipart()
    message = "There's an opens spot right now!"

    password = ""
    msg['From'] = ""
    msg['To'] = ""
    msg['Subject'] = "RSVP spot open"

    msg.attach(MIMEText(message, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com: 587')

    server.starttls()
    server.login(msg['From'], password)
    server.sendmail(msg['From'], msg['To'], msg.as_string())
    server.quit()
    

def get_event_details():
    response = requests.get('https://api.%s/%s?key=%s' % (host, urlname, api_key))
    if response.status_code != 200:
        return response.raise_for_status()
    return response.json()


def get_rsvp_count():
    return get_event_details()['next_event']['yes_rsvp_count']


def is_open_spot():
    return get_rsvp_count() < rsvp_limit


def notify():
    if is_open_spot():
        send_email()


notify()
