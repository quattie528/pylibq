#!/usr/bin/python

### MODULES ###
import datetime
#from datetime import date as d
#from datetime import time as t
#from datetime import date as dy # ein Alphabet ist gefehr
#from datetime import time as tm # ein Alphabet ist gefehr
#from datetime import datetime as dt
#from datetime import timedelta as dl
#from datetime import timezone as tz

#

#####################
### DATE in EXCEL ###
#####################
def xldate_to_date(xldate):
	temp = datetime.date(1900, 1, 1)
	delta = datetime.timedelta(days=xldate-2)
	return temp+delta

def xldate_to_datetime(xldate):
	temp = datetime.datetime(1900, 1, 1)
	delta = datetime.timedelta(days=xldate-2)
	return temp+delta

############################
### ÄLTESTE oder NEUESTE ###
############################
def aelteste_und_neueste(lis):
	assert( isinstance(lis, list) )
	lis = [ s2d(x) for x in lis ]
#	print( lis ) #d
	lis.sort()
	return lis

def aelteste(lis): # = älteste
	x = aelteste_und_neueste(lis)[0]
	x = str(x)
	return x

def neueste(lis):
	x = aelteste_und_neueste(lis)[-1]
	x = str(x)
	return x

#

##################
### DATE RANGE ###
##################
def daterange(ini,fin):
	res = []
	for n in range( int( (fin - ini).days ) + 1):
		res.append( ini + datetime.timedelta(n) )
	res.sort()
	res = tuple(res)
	return res

##### DIREKT ###############
if __name__ == '__main__':
	mode = 1
	if mode == 1: # 2018-08-18
		lis = ['2017-08-05','2018-09-16','2015-08-17','2019-08-08']
		print( aelteste(lis) )
		print( neueste(lis) )
	import kbench
	kbench.jetzt()
