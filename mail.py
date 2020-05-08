#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def sendMail(from_user, to_user, subject, message, filename=None, cc_user=None, bcc_user=None):
    # Create a multipart message and set headers
    if filename :
        msg = MIMEMultipart('mixed')
    else :
        msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = from_user
    msg['To'] = to_user
    msg['Cc'] = cc_user
    msg['Bcc'] = bcc_user

    # Add body to email
    msg.attach(MIMEText(message, 'plain'))

    # Add file to email
    if filename is not None:
        # Open file in binary mode
        with open(filename, "rb") as attachment:
            # Add file as application/octet-stream
            # Email client can usually download this automatically as attachment
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())

        # Encode file in ASCII characters to send by email
        encoders.encode_base64(part)

        # Add header as key/value pair to attachment part
        part.add_header(
            "Content-Disposition",
            f"attachment; filename= {filename}",
        )

        # Add attachment to message
        msg.attach(part)

    # Convert message to string
    text = msg.as_string()

    # Send the message via our own SMTP server, but don't include the envelope header.
    s = smtplib.SMTP('localhost')
    s.sendmail(from_user, to_user, text)
    s.quit()
