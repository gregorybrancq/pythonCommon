#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
from datetime import datetime
from .color import *


##############################################
##############################################
#                CLASS LOG                  ##
##############################################
##############################################

class LOGC(object): #TODO rename the class
    def __init__(self, file_name, prog_name, debug, gui=False):
        self.fileName = file_name
        self.progName = prog_name
        self.debug = debug
        self.gui = gui
        self.dtFormat = datetime.today().isoformat("_")

    def writeLog(self, msg):
        if self.debug:
            print(" DBG : " + str(msg))

        msg += "\n"
        try:
            f = open(self.fileName, 'a+')
            f.write(msg)
            f.close()
        except (IOError, OSError):
            pass

    def dbg(self, msg):
        mes = " [ debug ] " + self.dtFormat + " == " + msg
        if self.debug:
            print(" DBG : " + self.progName + str(mes))

    def info(self, item, msg):
        mes = item + " [ info  ] " + self.dtFormat + " == " + msg
        self.writeLog(mes)

    def warn(self, item, msg):
        mes = item + " [warning] " + self.dtFormat + " == " + msg
        self.writeLog(mes)

    def error(self, item, msg):
        mes = item + " [ error ] " + self.dtFormat + " == " + msg
        self.writeLog(mes)
        print("  ERROR " + self.progName + " :   Code " + str(item) + "\n" + str(msg) + "\n")

    def exit(self, item, msg):
        self.debug = False
        if self.gui:
            mes = "ERROR " + self.progName + " :   Exit code " + str(item) + "\n" + str(msg) + "\n"
            # MessageDialog(type_='error', title="ERROR " + self.progName + " code " + str(item), message=msg).run()
        else:
            mes = "  ERROR " + self.progName + " :   Exit code " + str(item) + "\n" + color_error + str(
                msg) + color_reset + "\n"
        self.writeLog(mes)
        sys.exit(color_error + mes + color_reset)
