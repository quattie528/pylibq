#!/usr/bin/python

### MODULES ###
#import datetime
#import os
#import pprint
#import urllib.parse
import time
#
import webbrowser as wb
import pyautogui as pgui
#
#import clipboard
#import attrdict
#
from datsun import *
#from qenv1 import *
from qenv3 import *
import xz
import xu
import kweb
import kbench
#
#1:battery,2:pip,3:mygen,4:myopus

### VARIABLES ###
kbench.KBDEBUG = True
DEBUG = True
DEBUG = False
#
KNF1 = xz.kml2ldic('__/sns.memo')
KNF1 = xz.ldic2ddic(KNF1,'sym')
#
ENTWURF = '__/sns_draft.memo'
SNSDB = xz.kml2ldic(ENTWURF)
SNSVS = xz.getkmlheader(ENTWURF)
URPFAD = 'D:/var/cache/bilden/instagram/'

#

###########
###  ###
###########
def data2sns9(data):

	### KONSTANT ###
	maus2click = ['maus2foto','maus2text','maus2post']

	### VORBEREITUNG ###
	for sym,dic in KNF1.items():
		for ziel in maus2click:
			lis = dic[ziel]
			lis = lis.split('||')
			lis = [ x.split('/') for x in lis ]
			for paar in lis:
				paar[0] = int(paar[0])
				paar[1] = int(paar[1])
			lis = [ tuple(x) for x in lis ]
			dic[ziel] = lis

	### HAUPT ###
	for dic in data:
		getun = dic['getun']
		foto = dic['foto']
		text = dic['text']
		pfad4foto = URPFAD + foto
		pfad4foto = pfad4foto.replace("/",'\\')
		if getun == 'X': continue
		for sym,param in KNF1.items():
			site = param['lien']
			kweb.url2ggc(site)
			xu.sleep(5)
			#
			for paar in param['maus2foto']:
				xu.click( paar[0], paar[1] )
			xu.paste(pfad4foto)
			pgui.press('enter')
			time.sleep(1)
			#
			for paar in param['maus2text']:
				xu.click( paar[0], paar[1] )
			xu.paste(text)
			time.sleep(1)
			#
			for paar in param['maus2post']:
				xu.click( paar[0], paar[1] )
			time.sleep(1)
			#
			pgui.hotkey('ctrl','w')
			#
		dic['getun'] = 'X'
	
	### AUSGABE ###
	xz.ldic2kml(data,labomi+'x.memo',SNSVS)
	xz.ldic2kml(data,SNSDB,SNSVS)
	return True

#	kweb.url2ggc('yahoo.com')
#	wb.open(url)
#	xu.max2left()
#	pgui.press('')
#	xu.click(7,7)
#	xu.fewbutton(7,'')
#	x = clipboard.paste()
#	clipboard.copy(x)

#

##### DIREKT ###############
if __name__=='__main__':
	data = xz.kml2ldic(ENTWURF)
	data2sns9(data)
	kbench.enfin()
