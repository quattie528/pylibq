### MODULES ###
#from datetime import date as d
#from datetime import time as t
from datetime import date as dy # ein Alphabet ist gefehr
from datetime import time as tm # ein Alphabet ist gefehr
from datetime import datetime as dt
from datetime import timedelta as dl

"""
#2022-01-17
def heute(typ=True): # True:string, False:Date|Time
	x = dy.today()
	if typ == True:
		return x.strftime('%Y-%m-%d')
	elif typ == False:
		return x
	assert typ in [True,False]

def heuted():
	return dy.today()

def jetzt(typ=True):
	x = dt.now()
#	print( typ ) #d
	if typ == True:
		return x.strftime('%Y-%m-%d %H:%M:%S')
	elif typ == False:
		return x
	assert typ in [True,False]

def jetzt2(typ=True):
	x = dt.now()
	if typ == True:
		return x.strftime('%Y-%m-%d_%H%M%S')
	elif typ == False:
		return x
	assert typ in [True,False]

def jetztt():
	return dt.now()
"""

def imheute():
	x = dy.today()
	x = x.year * 100 + x.month
	return x

### MINUTE zu STRING ###
def min2strt(x):
	y = dt(1,1,1,0,0) + dl(minutes=x)
	y = str(y)[-8:-3]
#	print( y )
	return y

def vortagen(x):
	if isinstance(x, int):
		y = dy.today()
#		print( x ) #d
		x = y - dl(days=x)
#		print( x ) #d
	return x
