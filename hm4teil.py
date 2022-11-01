#!/usr/bin/python

### MODULES ###
import datetime
#import os
#import pprint
import re
#
#import clipboard
#
#from datsun import *
#from qenv1 import *
#from qenv3 import *
#import befehl
#import regi
#import xb
import xt
#import xz
import kbench
#
#1:battery,2:pip,3:mygen,4:myopus

### VARIABLES ###
kbench.KBDEBUG = True
DEBUG = True
DEBUG = False

#

######################
### STRINT zu ZEIT ###
######################
def str2zeit(x):
	m1 = re.match('(\d{2})(\d{2}) (\d{2})(\d{2})',x)
	m2 = re.match('(\d{2}) (\d{2})(\d{2})',x)
	m3 = re.match('(\d{2})(\d{2})',x)
	tag = datetime.date.today()
	j = tag.year
	m = tag.month
	t = tag.day
	if m1:
		m  = int( m1.group(1) )
		t  = int( m1.group(2) )
		hh = int( m1.group(3) )
		mm = int( m1.group(4) )
		tag = datetime.date(j,m,t)
		w = xt.d2a(tag,'JPN')
		res = '%02d月%02d日(%s) %02d:%02d' % (m,t,w,hh,mm)
	elif m2:
		t  = int( m2.group(1) )
		hh = int( m2.group(2) )
		mm = int( m2.group(3) )
		tag = datetime.date(j,m,t)
		w = xt.d2a(tag,'JPN')
		res = '%02d日(%s) %02d:%02d' % (t,w,hh,mm)
	elif m3:
		hh = int( m3.group(1) )
		mm = int( m3.group(2) )
		res = '%02d:%02d' % (hh,mm)
	return res

#

##### DIREKT ###############
if __name__=='__main__':
	kbench.enfin()
