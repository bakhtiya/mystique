# Config(uration) Library
# Various configuration file specific functions

# general imports
import sys

# spefic imports
from json import loads as json2obj
from copy import copy

# globals
configPath = "conf/mystique.json"

# open file
configFile = open(configPath)

# load json
config = copy(json2obj(configFile.read()))

# required parameters
defaultTimeout = int(config.get("default_timeout", 5))
connectTimeout = int(config.get("connect_timeout", 5))
userAgent = str(config.get("user_agent", "Mozilla/5.0 (compatible; MSIE 10.6; Windows NT 6.1; Trident/5.0; InfoPath.2; SLCC1; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET CLR 2.0.50727) 3gpp-gba UNTRUSTED/1.0")) # IE 10.6 UA
defaultHeaders = config.get("default_headers", [])
verbose = bool(config.get("verbose", False))

# format parameters (json treats everything as unicode, when it starts at a str (wierd eh?))
for index in range(len(defaultHeaders)):
	defaultHeaders[index] = str(defaultHeaders[index])

# close file
configFile.close()