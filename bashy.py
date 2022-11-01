#!/usr/bin/python

### MODULES ###
#import datetime
#import os
#import pprint
import sys
#
#import clipboard
#import attrdict
#
#from datsun import *
#from qenv3 import *
#import xz
import kbench
#
#1:battery,2:pip,3:mygen,4:myopus

### VARIABLES ###
kbench.KBDEBUG = True
DEBUG = True
DEBUG = False

#

#####################
### STDIN zu LIST ###
#####################
def stdin2lis():
	lis = sys.stdin.read()
	lis = lis.split("\n")
	while 1:
		try:
			lis.remove('')
		except ValueError:
			break
	return lis

#

##### DIREKT ###############
if __name__=='__main__':
	abc()
	kbench.enfin()
