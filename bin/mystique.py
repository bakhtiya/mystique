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

# modify path
sys.path.append("lib")

# specific imports
from time import sleep
from console import console
from url import *

# main handler
if __name__ == "__main__":

	# show us what we are sending the webserver on a basic request
	#print get("addictivemobility.com/headers.php")

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
        post("https://www.bitsoup.me/takelogin.php", data="username=test&password=test")
        console("login request sent")
