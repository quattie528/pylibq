#!/usr/bin/python

### MODULES ###
import datetime
import requests
import sys
import re
import time
import random
#import kbench
import platform
import shutil
#
import clipboard
import webbrowser
import pyautogui as pgui
#
import xz
import xu
#import dritt
from datsun import *
from qenv3 import *
try:
	from qenv1 import *
except ModuleNotFoundError:
	pass
#
""" DEFINITION ###
(1) url2cmd2html()
(2) url2ggc2html()
(3) url2ggc2clp()
(4) url2ggc2datei()

* ggc : Mozilla FireFox
* ggc : Google Chrome

Google Chrome als Voreinstellung oder Standardwert für Webbrowser
"""

#__pycache__/kweb_2020-03-29.py
#pgui.FAILSAFE = True
pgui.moveTo(100,100)
#
wb = webbrowser.get(mychrome+' %s')

### KONSTANT ###
wart_min = 3
wart_max = 20
wart_min = 10 # EDGAR @ 2018-08-09
wart_max = 30
WART4BRW = 3
#
try:
	NLPFAD = mydwld
except NameError:
	NLPFAD = labomi + 'dwld/'
	os.makedirs(NLPFAD,exist_ok=True)
#
WGETPFAD = labomi + 'wget/'
os.makedirs(WGETPFAD,exist_ok=True)

#

def wahlbrowser(brw='chrome'):
	if brw == 'chrome':
		brw = mychrome
	elif brw == 'firefox':
		brw = myfirefox
#	brw = wb.get(brw+' %s') # 2022-04-10
	brw = webbrowser.get(brw+' %s')
	return brw

#

def url2ggc(addr):
	wb.open(addr)

##############################
### URL to KOMMAND zu HTML ###
##############################
def url2cmd2html(addr,ausgabe=None):
	if ausgabe == None:
		if addr[-1] == '/':
			ausgabe = re.sub('.+/','',addr[:-1])
		else:
			ausgabe = re.sub('.+/','',addr)
		ausgabe = WGETPFAD + ausgabe
	#
	if os.path.exists(ausgabe):
		html = xz.txt2str(ausgabe)
	else:
		print( addr )
		html = requests.get(addr)
		html = html.text
		#
		html = html.replace('JavaScript','JJavaScript')
		html = html.replace('http', 'hhttp' )
		html = "<URL>" + addr + "\n\n" + html
		xz.str2txt(html,ausgabe)
	return html

def url2cmd2datei(addr,ausgabe=None):
	if ausgabe == None:
		ausgabe = re.sub('.+/','',addr)
		ausgabe = WGETPFAD + ausgabe
	#
	if os.path.exists(ausgabe):
		inhalt = xz.bin2obj(ausgabe)
#		print( 'Existieren!',ausgabe ) #d
	else:
		inhalt = requests.get(addr)
#		print( ausgabe ) #d
		xz.obj2bin(inhalt,ausgabe)
	return inhalt

#

###############################
### URL zu FIREFOX zu DATEI ###
###############################
def url2ggc2datei(url,ausgabe):

	### KONSTANT ###
	datei = re.sub('.+/','',url)
	datei = NLPFAD + datei
	teil = datei + '.part'
	if '/' in ausgabe:
		ausgabe2 = ausgabe
	else:
		ausgabe2 = NLPFAD + ausgabe
#	print( datei ) #d
#	print( ausgabe2 ) #d
	if os.path.exists(ausgabe2):
		x = 'Passiert %s...' % ausgabe
		print( x )
		return True
	if os.path.exists(datei):
		shutil.move(datei,ausgabe2)
		x = 'Bewegt %s...' % ausgabe
		print( x )
		return True
	#
	x = 'Nehmen %s...' % ausgabe
	wb.open(url)
#	wb.open_new_tab(url)
	#
	xu.sleep(2)
#	pgui.click(x=1000, y=500)
#	pgui.keyDown('ctrl')
#	pgui.press('w')
#	pgui.keyUp('ctrl')
	#
	key = 0
	i = 0
	kein = 0
	for zt in range(30):
		i += 1
		if os.path.exists(teil):
			if not key == 1:
				print( "\nSLEEP / Teil Existert : ", end='')
			print('%d, '%i, end='')
			key = 1
			xu.sleep(1)
			continue
		#
		try:
			os.path.getsize(datei)
		except FileNotFoundError:
			kein += 1
			if kein == 5:
				print( "\n- PASS / %s : " % datei , end='')
				break
			xu.sleep(1)
		#
		if os.path.getsize(datei) == 0:
			if not key == 2:
				print( "\nSLEEP 2 / Get Size : ", end='')
			print('%d, '%i, end='')
			xu.sleep(1)
		else:
			break
	#
	if os.path.getsize(datei) == 0:
		os.remove(datei)
		return False

	### AUSGABE ###
	xu.sleep(2)
	xu.click(797,16)
#	xu.click(3,12)
#	pgui.hotkey('ctrl','w') #2022-07-03
	#
#	print( datei ) #d
#	print( ausgabe ) #d
	shutil.move(datei,ausgabe2)
	return True
#	exit() #d

#

#############################
### URL zu FIREFOX zu TXT ###
#############################
def url2ggc2txt(url,ausgabe):
#	print( 'Recommend wget2.uws' )
#	exit()

	### ZIEL ###
	ausgabe2 = ausgabe.replace('/','\\')
	clipboard.copy(ausgabe2)

	### KONSTANT ###
	print( url ) #d
	wb.open(url)
	m = random.randrange(wart_min,wart_max)
	xu.sleep(m)
	#
	xpos4sicher = 2
	ypos4sicher = 2
	#1640,20
	#797,16  # leftside
	#
	xu.click(xpos4sicher,ypos4sicher) # Golden Position
#	exit() #d
	pgui.hotkey('ctrl','s')
	print( "\tCtrl-S, ", end="" ) #d
	xu.sleep(3)
	#
	pgui.hotkey('ctrl','v')
	print( 'Ctrl-V, ', end="" ) #d
#	xu.sleep(3)
	xu.sleep(1) # 2018-12-12
	#
	pgui.press('enter')
	print( 'Enter, ', end="" ) #d
#	xu.sleep(1)
	xu.sleep(0.5) # 2018-12-12

	### AUSGABE ###
	xu.click(xpos4sicher,ypos4sicher) # Golden Position
	print( 'Click, ', end="" ) #d
	pgui.hotkey('ctrl','w')
	print( 'Ctrl-W', end="" ) #d
	print( '' ) #d

#

###################################
### URL zu FIREFOX zu CLIPBOARD ###
###################################
def url2ggc2clip(url,x=0,y=0,brw='chrome'):
	brw = 'firefox'
	brw = 'chrome'
	if brw == 'chrome':
		wb = wahlbrowser(brw)

	wb.open(url)
#	wb.open_new_tab(url)
	xu.sleep(WART4BRW)

	if brw == 'firefox':
		if x == 0: x == 155
		if y == 0: y == 50
		xu.click(x,y)
	elif brw == 'chrome':
		if x == 0: x == 65
		if y == 0: y == 40
		xu.click(x,y)
#	pgui.hotkey('alt','space') # DON'T DO THIS !!! @ 2020-04-18
#	pgui.press('x')            # DON'T DO THIS !!! @ 2020-04-18
	for k in 'accw':
		time.sleep(0.3)
		pgui.hotkey('ctrl',k)
	#
	wert = clipboard.paste()
	return wert


def url2ggc2src2clip(url,brw='chrome'):
#	brw = 'firefox'
	if brw == 'chrome': wb = wahlbrowser(brw)
	#
	wb.open(url)
	xu.sleep(WART4BRW)
	#
	pgui.hotkey('ctrl','u')
	time.sleep(WART4BRW/2)
	pgui.hotkey('ctrl','a')
	pgui.hotkey('ctrl','c')
	pgui.hotkey('ctrl','w')
	#
	wert = clipboard.paste()
	return wert


##### DIREKT ###############
if __name__=='__main__':
	pass
