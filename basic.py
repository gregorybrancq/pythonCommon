#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import random
import sys
from os.path import expanduser

from color import *


##############################################
# Basic functions
##############################################

# Exit when receiving an exception
def sysKeybInt():
    remove_lock_file()
    sys.exit(color_error + "\n### Received Ctrl-C exception\n#### Quit properly" + color_reset)


# User login
def getUserLogin():
    try:
        user = os.environ['USER']
    except KeyError:
        # if launch via crontab, there is no USER variable
        user = "greg"
        # print('%sCannot get the login user\n' % color_error)
    if user == "root":
        # tip to launch script with root user
        user = "greg"
    return user


def getHomeDir():
    return expanduser("~%s" % getUserLogin())


def getConfigDir():
    return os.path.join(getHomeDir(), 'Config')


def getToolsDir():
    return os.path.join(getConfigDir(), 'tools')


def getEnvDir():
    return os.path.join(getConfigDir(), 'env')


def getBinDir():
    env = getEnvDir()
    return os.path.join(getEnvDir(), "bin")


def getCommonDir():
    return os.path.join(getEnvDir(), "pythonCommon")


def getLogDir():
    return os.path.join(getEnvDir(), "log")


# Get the human size of a file
def humanSize(num):
    for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if num < 1024.0:
            return "%3.1f%s" % (num, x)
        num /= 1024.0


# Verify lock file
def verify_lock_file(lock_file):
    timeout = 0
    # Verify that the lock file doesn't exist
    while os.path.isfile(lock_file):
        if timeout > 200:
            remove_lock_file(lock_file)
            break
        else:
            import time
            time.sleep(1)
            timeout += 1


# Create lock file
def create_lock_file(lock_file):
    # Verify that the lock file doesn't exist
    verify_lock_file(lock_file)
    # Create it.
    os.system('touch ' + lock_file)


# Delete lock file
def remove_lock_file(lock_file):
    os.remove(lock_file)


# Random number
def getRandomSeed():
    return random.randint(1, 65536)


# Create a integer range
def parseRange(range_str):
    result = list()
    try:
        if range_str != "":
            list0 = range_str.split(",")
            for list1 in list0:
                list2 = list1.split("-")
                if len(list2) == 2:  # range found
                    for i in range(int(list2[0]), int(list2[1]) + 1):
                        result.append(i)
                else:
                    result.append(int(list2[0]))
    except:
        print(" There is a problem with your parsed options")

    return (result)


# Determine if the file is executable.
def test_file_exe(file):
    """Determine if the file is executable."""
    if not os.path.exists(file):
        return 0
    stat = os.path.stat
    stat_info = os.stat(file)
    mode = stat.S_IMODE(stat_info[stat.ST_MODE])
    if (stat.S_IXUSR & mode) or (stat.S_IXGRP & mode) or (stat.S_IXOTH & mode):
        return True
    return False


# Remove a directory
def remove_dir_file(path):
    list_files = os.listdir(path)
    for file in list_files:
        try:
            os.remove(os.path.join(path, file))
        except OSError:
            pass


# Move files in another directory
def move_files(old_path, new_path):
    list_files = os.listdir(old_path)
    for file in list_files:
        os.rename(os.path.join(old_path, file), os.path.join(new_path, file))
