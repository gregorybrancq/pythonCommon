#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Network functions
"""
import socket
import subprocess


def checkAddress(address):
    """
    Check if address pings

    :param address: IP v4 (string)
    :return: True if address is accessible, else False
    """
    cmd = ["ping", "-w", "1", str(address)]
    proc = subprocess.Popen(cmd)
    proc.wait()
    if proc.returncode == 0:
        return True
    return False


def getIp():
    # print([(s.connect(('8.8.8.8', 53)), s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET,
    # socket.SOCK_DGRAM)]][0][1]) ips = subprocess.check_output(['hostname', '--all-ip-addresses'])
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # try:
    # doesn't even have to be reachable
    s.connect(('10.255.255.255', 1))
    ip = s.getsockname()[0]
    # except:
    # ip = '127.0.0.1'
    # finally:
    s.close()
    return ip
