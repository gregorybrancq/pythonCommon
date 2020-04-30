#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from mail import sendMail

userMail = "gregory.brancq@free.fr"
sendMail(From=userMail, To=userMail,
         Subject="This is an important subject",
         Message="What ! you killed Bill !!!")
