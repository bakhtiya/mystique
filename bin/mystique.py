#!/usr/bin/python

# Primary Executable
# This file will be run directly.

# By: Cyrus Bakhtiyari
# Email: me@cyrusbakhtiyari.com
# Site: cyrusbakhtiyari.com

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

	# make the login request (assume successful login - cookies are written to cookiefile - defined in configuration)
        console("sending login request to bitsoup")
        post("https://www.bitsoup.me/takelogin.php", data="username=" + username + "&password=" + password)
        console("login request sent")

        # sleep again, this time less as authentication has aleady been done
        console("sleeping for 2 seconds")
        sleep(2)

        # clear the annoying announcements 10 times
        for x in range(10):
                console("sending clear announcements request to bitsoup")
                get("https://www.bitsoup.me/clear_announcement.php")
                console("clear announcements request sent")

                console("sleeping for 1 second")
                sleep(1)
