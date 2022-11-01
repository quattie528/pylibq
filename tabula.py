#!/usr/bin/python

### MODULES ###
#import datetime
#import os
#import pprint
#
#import clipboard
#import attrdict
import colorama
#
from datsun import *
from qenv3 import *
#import xz
import kbench
#
#1:battery,2:pip,3:mygen,4:myopus

### VARIABLES ###
kbench.KBDEBUG = True
DEBUG = True
DEBUG = False

colorama.init()

#

###########
###  ###
###########
def farbenV(tbl,farbe,pos):
	for lis in tbl:
		x = lis[pos]
		x = str(x)
		x = farbe + x + colorama.Fore.RESET
		lis[pos] = x
	return tbl

def farbenH(tbl,farbe,pos):
	lis = tbl[pos]
	lis = [ str(x) for x in lis ]
	lis = [ farbe + x + colorama.Fore.RESET for x in lis ]
	tbl[pos] = lis
	return tbl

def farbenP(tbl,farbe,x,y):
	tbl[x][y] = str(tbl[x][y])
	tbl[x][y] = farbe + tbl[x][y] + colorama.Fore.RESET
	return tbl

#

##### DIREKT ###############
if __name__=='__main__':
	farbenV()
	kbench.enfin()
