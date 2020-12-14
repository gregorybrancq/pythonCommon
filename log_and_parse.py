#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Common functions used for each file
"""
import logging
import os
from logging.handlers import RotatingFileHandler
from optparse import OptionParser

from basic import getLogDir


def parsingLine():
    parser = OptionParser()
    parser.add_option(
        "-d",
        "--debug",
        action="store_true",
        dest="debug",
        default=False,
        help="Display all debug information"
    )
    parser.add_option(
        "--dry-run",
        action="store_true",
        dest="dryRun",
        default=False,
        help="Don't execute the processus"
    )
    return parser.parse_args()


def createLog(log_name, parsed_args):
    if not os.path.isdir(getLogDir()):
        os.mkdir(getLogDir())
    # create logger
    logger = logging.getLogger(log_name)
    logger.setLevel(logging.DEBUG)
    # create file handler which logs even debug messages
    # fh = logging.FileHandler(os.path.join('log', '%s.log' % log_name))
    fh = RotatingFileHandler(os.path.join(getLogDir(), '%s.log' % log_name), mode='a', maxBytes=5 * 1024 * 1024,
                             backupCount=2, delay=False)
    fh.setLevel(logging.DEBUG)
    # create console handler with a higher log level
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    # create formatter and add it to the handlers
    formatter = logging.Formatter('%(asctime)s - %(levelname)-7s - %(name)s - %(message)s')
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)
    # add the handlers to the logger
    logger.addHandler(fh)
    if parsed_args.debug:
        logger.addHandler(ch)
    return logger

# command application
# logger.debug('debug message')
# logger.info('info message')
# logger.warning('warn message')
# logger.error('error message')
# logger.critical('critical message')
