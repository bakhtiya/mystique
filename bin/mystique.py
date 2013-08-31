#!/usr/bin/python

# BitSoup Interaction
# By: Cyrus Bakhtiyari

# Notes
# This script is essentially an interaction script with BitSoup. I will
# eventually modularize this out and use parts for other systems
# I want to develop.
# My current goal is to either write this system so that it will inform me when
# new awesome movies come out for download OR it will help me keep my ratio up
# by periodically refreshing the new added list of torrents and looking for the
# best torrents to seed to gain the best ratio :p MUHAHHAHHAHA

# general imports
import sys, os

# specific imports
from sys import exit, argv

# check relative path
if __name__ == "__main__":
        cmd = argv[0]
        if cmd != "./bin/mystique.py" and cmd != "bin/mystique.py":
                print "%s: must run from repo root directory (./bin/mystique.py)" % (cmd)
                exit(1)

# modify path
sys.path.append("lib")

# specific imports
from time import sleep
from console import console
from url import *

# main handler
if __name__ == "__main__":

        # verify username and password passed
        if len(argv) < 3:
                print "%s: failed to specify enough parameters (%s [username] [password])" % (cmd, cmd)
                exit(1)

        # grab username and password
        username = str(argv[1])
        password = str(argv[2])

	# show us what we are sending the webserver on a basic request
	#print get("cyrusbakhtiyari.com/headers.php")

	# make the bitsoup login initial call
        console("calling bitsoup login page")
        get("https://www.bitsoup.me/login.php")
        console("bitsoup login page called")

	# sleep to avoid being caught as a bot
	# one cannot simply ask for login page, type his username and password in 0.0001 seconds :p
        console("sleeping for 5 seconds")
	sleep(5)

	# make the login request
        console("sending login request to bitsoup")
        post("https://www.bitsoup.me/takelogin.php", data="username=" + username + "&password=" + password)
        console("login request sent")
