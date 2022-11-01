#!/usr/bin/python

### MODULES ###
#import datetime
#import os
#import pprint
import threading
#
#import clipboard
#
from datsun import *
from qenv3 import *
import befehl
import regi
#import xb
#import xt
#import xz
import kbench
#
#1:battery,2:pip,3:mygen,4:myopus

### VARIABLES ###
kbench.KBDEBUG = True
DEBUG = True
DEBUG = False

#

###########
###  ###
###########
def vorder1hinten9(vorder,hinten):
	if not isinstance(hinten, list): hinten = [hinten]
	fxs = []
	faden = []
	faden1 = threading.Thread(target=vorder,daemon=True)
	for fx in hinten:
		tmp = threading.Thread(target=fx,daemon=True)
		faden.append(tmp)

	faden1.start()
	for fx in faden: fx.start()
	#
	faden1.join()
	for fx in faden: fx.join()
	return True

def vorxls1hinten9(vorder,hinten):
	if not isinstance(hinten, list): hinten = [hinten]
	fxs = []
	faden = []
	faden1 = threading.Thread(target=vorder,daemon=True)
	for fx in hinten:
		tmp = threading.Thread(target=fx,daemon=True)
		faden.append(tmp)

	faden1.start()
	for fx in faden: fx.start()
	#
	faden1.join()
	for fx in faden: fx.join()
	return True

#

##### DIREKT ###############
if __name__=='__main__':
	kbench.enfin()
