#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import datetime
from mail import sendMail

userMail = "gregory.brancq@free.fr"

sendMail(from_user=userMail, to_user=userMail, subject="Mail test " + str(datetime.now()),
         message="Bouh, t'as eu peur ?")
sendMail(from_user=userMail, to_user=userMail, subject="Mail with attachment " + str(datetime.now()),
         message="File in attachment, ça marche ?", filename="../nemoScripts/Test/4_2.pdf")
