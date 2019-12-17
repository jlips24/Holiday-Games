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

def send_emails(people, template, extra=None):
    print("Sending Messages")

    s = smtplib.SMTP(host=os.getenv("EMAIL_HOST"), port=int(os.getenv("EMAIL_PORT")))
    s.starttls()
    s.login(os.getenv("EMAIL_USER"), os.getenv("EMAIL_PASSWORD"))

    message_number = 1
    total_messages = len(people)
    for person in people:
        print(f"({round((message_number/total_messages)*100, 2)}%)Sending message to {person[0]} at {person[1]}: message {message_number} of {total_messages}")
        msg = MIMEMultipart()
        msg['From'] = "Open Source Christmas"
        msg['To'] = person[1]

        if (template == "SecretSanta"):
            message_template = read_template('templates/SecretSantaEmail.txt')
            # Add in the reciprient name and match name to the message template
            reciprient = person[0]
            match_name = people[person[2]][0]
            message = message_template.substitute(RECIPRIENT_NAME=reciprient, MATCH_NAME=match_name)
            # Setup the parameters of the message
            msg['Subject']="Your Secret Santa match is ready"

            # Add in the message body
            msg.attach(MIMEText(message, 'plain'))
        elif (template == "WhiteElephant"):
            message_template = read_template('templates/WhiteElephant.txt')
            # Add in the reciprient name and match name to the message template
            reciprient = person[0]
            turn = person[2]
            message = message_template.substitute(RECIPRIENT_NAME=reciprient, TURN_NUMBER=turn)
            # Setup the parameters of the message
            msg['Subject']="White Elephant info"
            # Add in the message body
            msg.attach(MIMEText(message, 'plain'))
        elif (template == "WhiteElephantMaster"):
            message_template = read_template('templates/WhiteElephantMaster.txt')
            # Add in the reciprient name and match name to the message template
            reciprient = person[0]
            message = message_template.substitute(RECIPRIENT_NAME=reciprient, PERSON_LIST=extra)
            # Setup the parameters of the message
            msg['Subject']="White Elephant info (master list)"
            # Add in the message body
            msg.attach(MIMEText(message, 'plain'))
        # Send the message
        try:
            s.send_message(msg)
        except smtplib.SMTPRecipientsRefused:
            print(f"The mail server had an error sending the notification to {msg['To']}")
        del msg

        message_number += 1
