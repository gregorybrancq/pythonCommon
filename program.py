#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
 Class for program :
    - manage if it is running or not
    - enable or disable it for one day
    - launch it only once a day
"""
import logging
import os
import sys
from datetime import date, datetime, timedelta


class Program:
    """
    Different functions to manage a program
    """

    def __init__(self, prog_name, config_file=None, root_log=None):
        if root_log:
            log_name = '.'.join([root_log, __name__])
        else:
            log_name = '.'.join([prog_name, __name__])
        self.logCP = logging.getLogger(log_name)
        self.prog_name = prog_name
        self.config_file = config_file
        self._enable_program = bool()  # Program can be launched
        self._justRemoveFile = False  # To know if the file has just been deleted
        self.running_file = os.path.join("/tmp", self.prog_name + ".running")
        self.disable_file = os.path.join("/tmp", self.prog_name + ".disable")

    #
    # Running part
    #
    def isRunning(self):
        """
        Specify if the program is running

        :return: True if running, False if not.
        """
        if not (os.path.isfile(self.running_file)):
            self.logCP.debug("Running file is not present")
            return False
        self.logCP.debug("Running file is present : %s" % self.running_file)
        return True

    def startRunning(self):
        """
        Start the program, running file is created
        """
        self.logCP.debug("Create running file %s" % self.running_file)
        open(self.running_file, "w")

    def stopRunning(self):
        """
        Stop the program, running file is deleted
        """
        if os.path.isfile(self.running_file):
            self.logCP.debug("Delete running file %s" % self.running_file)
            os.remove(self.running_file)

    #
    # Enable/disable part
    #
    def _setEnable(self):
        self._enable_program = True

    def _setDisable(self):
        self._enable_program = False

    def _isEnable(self):
        if self._enable_program:
            self.logCP.debug("Enable file is not present")
            return True
        self.logCP.debug("Enable file is present")
        return False

    def _checkFileDate(self):
        """
        Check if disable file is created more than one day

        :return: True if more than one day, False if not
        """
        fd = open(self.disable_file, 'r')
        date_file_str = fd.read().rstrip('\n')
        fd.close()
        try:
            date_file = datetime.strptime(date_file_str, "%Y-%m-%d %H:%M:%S.%f")
        except ValueError:
            return True
        current_date = datetime.now()
        if date_file + timedelta(days=1) < current_date:
            return True
        return False

    # Check if disable_file exists more than one day
    def _checkDisableFile(self):
        """
        Check if disable file exists more than one day
        """
        if not os.path.isfile(self.disable_file):
            self._setEnable()
        else:
            # check if more than one day
            if self._checkFileDate():
                self.progEnable()
            else:
                self._setDisable()

    def isEnable(self):
        """
        Check if the program can be launched

        :return: True if it can be launched, False if not.
        """
        self._checkDisableFile()
        return self._isEnable()

    def progEnable(self):
        """
        Allow to launch the program by deleting the disable file
        """
        self._setEnable()
        if os.path.isfile(self.disable_file):
            os.remove(self.disable_file)
            self._justRemoveFile = True

    def progDisable(self):
        """
        Avoid the program running by creating the disable file
        """
        self._setDisable()
        fd = open(self.disable_file, 'w')
        fd.write(str(datetime.now()))
        fd.close()

    def getInfo(self):
        """
        Return the status

        :return: if program can be launched or not.
        """
        if self.isEnable():
            return "The program could be launched."
        else:
            return "The program is currently disabled."

    #
    # Config part
    #

    # If the file has just been deleted
    def isJustRemoveFile(self):
        return self._justRemoveFile

    def isLaunchedLastDays(self, days=1):
        """
        Is the program launched today ?

        :return: True if it runs today, False if not or at the first run
        """
        if not os.path.isfile(self.config_file):
            self.logCP.debug("The program has never been launched.")
            return False
        else:
            # Get the date in config file
            fd = open(self.config_file, 'r')
            date_file_str = fd.read().rstrip('\n')
            fd.close()
            try:
                config_date = datetime.strptime(date_file_str, "%Y-%m-%d")
            except ValueError:
                self.logCP.error("Can't get the date in config file (%s)" % self.config_file)
                return False

            # Get current date
            today_date = date.today()
            today_datetime = datetime(
                year=today_date.year,
                month=today_date.month,
                day=today_date.day,
            )

            # Compare date to current date
            self.logCP.debug("today_datetime = %s, config_date = %s" % (str(today_datetime), str(config_date)))
            if config_date + timedelta(days=7) > today_datetime:
                self.logCP.info("Already launched during the last %s days" % days)
                return True
            else:
                self.logCP.info("Not launched during the last %s days" % days)
                return False

    def runToday(self):
        """
        Update the date to indicate that program was running today.
        """
        if os.path.isfile(self.config_file):
            os.remove(self.config_file)
        try:
            fd = open(self.config_file, 'w')
        except IOError:
            self.logCP.error("Can't create the config file %s" % self.config_file)
            self.stopRunning()
            sys.exit(1)
        today_str = date.today().isoformat()
        self.logCP.debug("Create config file (%s) with date = %s" % (self.config_file, today_str))
        fd.write(today_str)
        fd.close()
        #os.chown(self.config_file, 1000, 1000)
