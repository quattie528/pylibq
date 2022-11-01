#!/usr/bin/python

### MODULES ###
#import datetime
#import os
#import pprint
#import copy
#
#import clipboard
#import attrdict
#
#from datsun import *
from qenv3 import *
import xz
import kbench
#
#1:battery,2:pip,3:mygen,4:myopus

### VARIABLES ###
kbench.KBDEBUG = True
DEBUG = True
DEBUG = False
#
KOPFZEILE = 190#mm
KOPFZEILE = KOPFZEILE / 4 * 3

#

###########
###  ###
###########
def tbl2tex(tbl,langezeile=[]):
	"""
	[tabulate.tabulate(tbl,headers=tbl[0],tablefmt='latex')]

	\\begin{tabular}{lll}
	\\hline
	a & b & c \\\\
	\\hline
	1 & 2 & 3 \\\\
	4 & 5 & 6 \\\\
	7 & 8 & 9 \\\\
	\\hline
	\\end{tabular}
	"""

	### HAUPT ###
	res = ''
	for lis in tbl:
		x = ' & '.join(lis)
		x = "\\hline \n%s  \\\\ \n" % x
		if res == '':
			x += "\\hline \n"
		res += x

	### KOPFZEILE und FUßZEILE ###
	if langezeile == []:
		vs = len(tbl[0])
		lange = KOPFZEILE // vs
		lange = int(lange)
		vs = [ 'm{%dmm}' % lange for i in range(vs) ]
	else:
		if sum(langezeile) > KOPFZEILE:
			x = "[ACHTUNG] Deine Kopfzeile ist %d <-> "
			x += "Standard Lange ist %d"
			x %= (sum(langezeile),KOPFZEILE)
			print( x )
		if len(langezeile) != len(tbl[0]):
			x = "[ACHTUNG] Deine Kopfzeile hast %d Spalten <-> "
			x += "Es gibt %d Spalten ins Tabelle"
			x %= (len(langezeile),len(tbl[0]))
			print( x )
		vs = [ 'm{%dmm}' % d for d in langezeile ]
	vs = '|'.join(vs)
	vs = '|%s|' % vs
	#
	kopf = "\\begin{tabular}{%s}\n" % vs
	res = kopf + res
	#
	res += "\\hline \n"
	res += "\\end{tabular} \n"

	return res

#

##### DIREKT ###############
if __name__=='__main__':
	tbl = xz.txt2tbl(labomi+'a.tsv')
	x = tbl2tex(tbl,[40,20,30,5,5,5,5])
	x = tbl2tex(tbl)
	xz.str2txt(x,'b.tex')
	kbench.enfin()
