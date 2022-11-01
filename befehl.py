#!/usr/bin/python

### MODULES ###
#import datetime
#import os
#import pprint
import sys
#
#import clipboard
#import attrdict
from collections import OrderedDict
#
from datsun import *
from qenv3 import *
#import xz
#
#1:battery,2:pip,3:mygen,4:myopus

### VARIABLES ###
DEBUG = True
DEBUG = False

#

###########
###  ###
###########
class Befehl(OrderedDict):
	def __init__(m):
		pass

	def show(m):
		x = '*** GENUTZ ANWEISUNG ***'
		print( x )
		i = 0
		for k,w in m.items():
			i += 1
			print( '%d)' % i, k )

	def call(m,ein):
		if isinstance(ein, int):
			i = 0
			for k,fx in m.items():
				i += 1
				if i == ein:
					fx()
		elif isinstance(ein, str):
			m[ein]()

	def stdin(m,*ein):
		if ein == ():
			if len(sys.argv) == 1:
				m.show()
				ein = "\n*** Was ist deiner Wahl? ***"
				print( ein )
				print( '# Ctrl-C: KeyboardInterrupt' )
				print( '# Ctrl-Z: STDIN Enden' )
				ein = input()
				ein = int(ein)
				m.call(ein)
			else:
				ein = sys.argv[1]
				if ein == 'MARUO':
					return False
					m.show()
				else:
					try:
						m.call(ein)
					except KeyError:
						m.call(int(ein))
		else:
			for e in ein: # 2022-05-13
				m.call(e)

#

##### DIREKT ###############
if __name__=='__main__':
	abc()

#b[''] = lambda: ()
