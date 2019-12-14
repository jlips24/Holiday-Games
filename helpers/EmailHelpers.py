import smtplib
import os
from string import Template
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv

load_dotenv()


def read_template(filename):
    with open(filename, 'r', encoding='utf-8') as template_file:
        template_file_content = template_file.read()
    return Template(template_file_content)

def send_emails(people):
    s = smtplib.SMTP(host=os.getenv("EMAIL_HOST"), port=int(os.getenv("EMAIL_PORT")))
    s.starttls()
    s.login(os.getenv("EMAIL_USER"), os.getenv("EMAIL_PASSWORD"))

    for person in people:
        message_template = read_template('templates/SecretSantaEmail.txt')
        
        msg = MIMEMultipart()
        # add in the actual person name to the message template
        reciprient = person[0]
        match_name = people[person[2]][0]
        message = message_template.substitute(RECIPRIENT_NAME=reciprient, MATCH_NAME=match_name)

        # setup the parameters of the message
        msg['From'] = os.getenv("EMAIL_USER")
        msg['To'] = person[1]
        msg['Subject']="Your Secret Santa match is ready"

        # add in the message body
        msg.attach(MIMEText(message, 'plain'))

        # send the message via the server set up earlier.
        s.send_message(msg)
        
        del msg