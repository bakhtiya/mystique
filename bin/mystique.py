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

# imports
import sys, os
from pycurl import Curl
from cStringIO import StringIO
from copy import copy
from random import randint as rnd
from time import sleep

# globals
defaultTimeout = 5 # seconds for timeout (default)
connectTimeout = 5 # seconds for timeout (connection timeout)
userAgents =	[
					"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.57 Safari/537.36"
				]
defaultHeaders =	[
						"Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
						"Accept-Language: en-US,en;q=0.8"
					]

# functions
def getUserAgent():
	'''Grab and return a random user agent from the global user agents list.'''
	return userAgents[rnd(0, rnd(0,len(userAgents) - 1))]

def post(url, data="", headers=[]):
        '''Given a URL, send a post request with post data and headers. Return the response.'''
        b = StringIO()
        c = Curl()
        c.setopt(c.URL, url)
        c.setopt(c.POST, True)
        c.setopt(c.POSTFIELDS, data)
        c.setopt(c.FOLLOWLOCATION, True)
        c.setopt(c.WRITEFUNCTION, b.write)
        c.setopt(c.VERBOSE, True)
        c.setopt(c.CONNECTTIMEOUT, connectTimeout)
        c.setopt(c.TIMEOUT, defaultTimeout)
        c.setopt(c.USERAGENT, getUserAgent())
        c.setopt(c.HTTPHEADER, defaultHeaders + headers)
        c.perform()
        r = copy(b.getvalue())
        b.close()
        return r

def get(url, headers=[]):
        '''Given a URL and headers send a HTTP GET request. Return the response.'''
        b = StringIO()
        c = Curl()
        c.setopt(c.URL, url)
        c.setopt(c.FOLLOWLOCATION, True)
        c.setopt(c.WRITEFUNCTION, b.write)
        c.setopt(c.CONNECTTIMEOUT, connectTimeout)
        c.setopt(c.TIMEOUT, defaultTimeout)
        c.setopt(c.USERAGENT, getUserAgent())
        c.setopt(c.HTTPHEADER, defaultHeaders + headers)
        c.perform()
        r = copy(b.getvalue())
        b.close()
        return r

# main handler
if __name__ == "__main__":

	# show us what we are sending the webserver on a basic request
	#print get("addictivemobility.com/headers.php")

	# make the bitsoup login initial call
	get("https://www.bitsoup.me/login.php")

	# sleep to avoid being caught as a bot
	# one cannot simply ask for login page, type his username and password in 0.0001 seconds :p
	sleep(5)

	# make the login request
	print post("https://www.bitsoup.me/takelogin.php")
