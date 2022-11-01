#!/usr/bin/python

### MODULES ###
#import datetime
#import os
#import pprint
#
#import clipboard
#import attrdict
#import flask
import tabulate
#
from datsun import *
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

####################
### POST zu DICT ###
####################
def post2dic(form):
#	xz.dic2txt(form,labomi+'x.tsv')
	if str(form) == '': return {}
	if form == {}: return {}
	dic = {}
	for k,w in form.items():
		if str(w) == '': continue
		dic[k] = str(w)
	return dic

#

#######################
### TABELLE zu HTML ###
#######################
def tbl2html(tbl,**opt):
	res = ''
#	tbl[3][3] = xz.bless(tbl[3][3])
	html = tabulate.tabulate(tbl, tablefmt='html')

	if opt.get('kopfer') == True:
		html = html.split("\n")
		tmp = []
		th = False
		for x in html:
			if th == True:
				pass
			elif '<td>' in x:
				x = x.replace('td>','th>')
				th = True
			tmp.append(x)
		html = "\n".join(tmp)

	if opt.get('nurinhalt') == True:
		for tag in ['<table>','<tbody>','</table>','</tbody>']:
			html = html.replace(tag,'')
	return html

#

########################
### LISTE zu OPTIONS ###
########################
def lis2opt(lis,gewahlt):
	res = ''
	for x in lis:
		w = '<option value="%s" selected>%s</option>' % (x,x)
		if x != gewahlt:
			w = w.replace(' selected','')
		res += w
	return res

#

##### DIREKT ###############
if __name__=='__main__':
	tbl = xz.txt2tbl(labomi+'x.tsv')
	x = tbl2html(tbl,kopfer=True)
	print( x )
	kbench.enfin()
