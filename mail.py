#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Import smtplib for the actual sending function
import smtplib
# Import the email modules we'll need
from io import BytesIO
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
#from email import Charset
from email.generator import Generator


def sendMail(From, To, Subject, Cc=None, Message=None):

    # Default encoding mode set to Quoted Printable. Acts globally!
    #Charset.add_charset('utf-8', Charset.QP, Charset.QP, 'utf-8')
    # 'alternative’ MIME type – HTML and plain text bundled in one e-mail message
    msg = MIMEMultipart('alternative')
    msg['Subject'] = Header(Subject, 'utf-8')
    # Only descriptive part of recipient and sender shall be encoded, not the email address
    # msg['From'] = Header(From, 'utf-8')
    msg['From'] = From
    msg['To'] = To
    msg['Cc'] = Cc

    # Attach the parts with the given encodings.
    #htmlpart = MIMEText(MessageHtml, 'html', 'UTF-8')
    #msg.attach(htmlpart)
    textpart = MIMEText(Message, 'plain', 'UTF-8')
    msg.attach(textpart)

    # And here we have to instantiate a Generator object to convert the msg
    # object to a string (can't use msg.as_string, because that escapes
    # "From" lines).
    io = BytesIO()
    g = Generator(io, False)  # second argument means "should I mangle From?"
    g.flatten(msg)

    # Send the message via our own SMTP server, but don't include the
    # envelope header.
    s = smtplib.SMTP('localhost')
    s.sendmail(From, [To], io.getvalue())
    s.quit()


