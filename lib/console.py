# Console Library
# Various console specific functions

# general imports
import sys

# spefic imports
from datetime import datetime
from sys import stdout, exit

# functions
def console(line):
        '''Output text to the console with the appropriate formatting.'''

        # create a date-timestamp with a specified format
        date = datetime.now().strftime("%Y/%m/%d %H:%M:%S")

        # print the formatted message with timestamp to stdout
        print date + " " + str(line)

        # ensure stdout is flushed
        stdout.flush()
