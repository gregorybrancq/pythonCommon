#!/usr/bin/env python
# -*- coding: utf-8 -*-

###############################################
###############################################
##                  COLOR                    ##
###############################################
###############################################

# Color definition
color = dict()
color['red'] = '\033[31m'
color['green'] = '\033[32m'
color['blue'] = '\033[34m'
color['magenta'] = '\033[35m'
color['cyan'] = '\033[36m'
color['reset'] = '\033[39m\033[49m\033[0m'
color['blink'] = '\033[5m'
color['bold'] = '\033[1m'
color_default = color['cyan']

color_info1 = color['cyan']
color_info2 = color['green']
color_cmd = color['magenta']
color_warn = color['blue']
color_error = color['red']
color_reset = color['reset']
