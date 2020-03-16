#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
 Class that allows to enable or disable a program for one day
 If the disable file is present, the program will not be launched
"""

import os
from datetime import datetime, timedelta


class ProgEnDis:
    def __init__(self, disableFile):
        self._enable = bool()
        self.disableFile = disableFile  # Disable file name with path
        self._checkDisableFile()

    def __str__(self):
        res = str()
        res += "# enable = " + str(self._enable) + "\n"
        res += "# disableFile = " + str(self.disableFile) + "\n"
        return res

    # Enable it
    def _setEnable(self):
        self._enable = True

    # Disable it
    def _setDisable(self):
        self._enable = False

    # if this program can be launched
    def _isEnable(self):
        if self._enable:
            return True
        return False

    # Check file date creation is
    #  return True  if > 1 day
    #  return False if < 1 day
    def _checkFileDate(self):
        fd = open(self.disableFile, 'r')
        dateFileStr = fd.read().rstrip('\n')
        try :
            dateFileDT = datetime.strptime(dateFileStr, "%Y-%m-%d %H:%M:%S.%f")
        except ValueError :
            return True
        currentDT = datetime.now()
        if dateFileDT + timedelta(days=1) < currentDT:
            return True
        return False

    # Check if disableFile exists more than one day
    def _checkDisableFile(self):
        if not os.path.isfile(self.disableFile):
            self._setEnable()
        else:
            # check if more than one day
            if self._checkFileDate():
                self._setEnable()
            else:
                self._setDisable()

    # Enable procedure
    # delete (if existing) the disableFile
    def setEnable(self):
        if os.path.isfile(self.disableFile):
            os.remove(self.disableFile)
        self._isEnable()

    # Disable procedure
    # create the disableFile
    def setDisable(self):
        fd = open(self.disableFile, 'w')
        fd.write(str(datetime.now()))
        fd.close()
        self._setDisable()

    # Check if the disableFile exist
    # return true if it exists, false if it doesn't exist
    def isEnable(self):
        self._checkDisableFile()
        return self._isEnable()
