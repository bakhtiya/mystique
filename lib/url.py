# URL Library
# Various URL specific functions.

# general imports
import sys

# modify path
sys.path.append("lib")

# specific imports
from config import *
from pycurl import Curl
from copy import copy
from cStringIO import StringIO

def post(url, data="", headers=[]):
        '''Given a URL, send a post request with post data and headers. Return the response.'''
        b = StringIO()
        c = Curl()
        c.setopt(c.URL, url)
        c.setopt(c.POST, True)
        c.setopt(c.POSTFIELDS, data)
        c.setopt(c.FOLLOWLOCATION, True)
        c.setopt(c.WRITEFUNCTION, b.write)
        c.setopt(c.COOKIEJAR, cookiePath)
        c.setopt(c.COOKIEFILE, cookiePath)
        c.setopt(c.VERBOSE, verbose)
        c.setopt(c.CONNECTTIMEOUT, connectTimeout)
        c.setopt(c.TIMEOUT, defaultTimeout)
        c.setopt(c.USERAGENT, userAgent)
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
        c.setopt(c.COOKIEJAR, cookiePath)
        c.setopt(c.COOKIEFILE, cookiePath)
        c.setopt(c.VERBOSE, verbose)
        c.setopt(c.CONNECTTIMEOUT, connectTimeout)
        c.setopt(c.TIMEOUT, defaultTimeout)
        c.setopt(c.USERAGENT, userAgent)
        c.setopt(c.HTTPHEADER, defaultHeaders + headers)
        c.perform()
        r = copy(b.getvalue())
        b.close()
        return r