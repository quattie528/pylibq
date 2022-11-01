#!/usr/bin/python

### MODULES ###
#import datetime
import os
#import pprint
#
#import clipboard
import cv2
from pyzbar import pyzbar
#
from datsun import *
from qenv1 import *
from qenv3 import *
import befehl
#import regi
#import xb
#import xt
#import xz
import kbench
#
import pytesseract # tesseract is obsolete
from PIL import Image
from PIL import ImageGrab
TESSERACT_PATH = 'C:/Program Files/Tesseract-OCR'
TESSDATA_PATH  = 'C:/Program Files/Tesseract-OCR/tessdata'
os.environ["PATH"] += os.pathsep + TESSERACT_PATH
os.environ["TESSDATA_PREFIX"] = TESSDATA_PATH

### VARIABLES ###
kbench.KBDEBUG = True
logging.disable(logging.DEBUG)
#

#

#########################
### BARCODE zu STRING ###
#########################
def bar2str(bild):
	#2022-10-02
	#https://towardsdatascience.com/building-a-barcode-qr-code-reader-using-python-360e22dfb6e5
	img_bgr = cv2.imread(bild, cv2.IMREAD_COLOR)
	wert = pyzbar.decode(img_bgr)
	if wert == []: return None
	x = wert[0].data
	x = x.decode('ascii')
	return x

########################
### QRCODE zu STRING ###
########################
def qr2str(bild):
	#2022-10-02
	#https://qiita.com/PoodleMaster/items/0afbce4be7e442e75be6
	qrd = cv2.QRCodeDetector()
	img_bgr = cv2.imread(bild, cv2.IMREAD_COLOR)
	wert = qrd.detectAndDecodeMulti(img_bgr)
	retval          = wert[0]
	decoded_info	= wert[1]
	points          = wert[2]
	straight_qrcode = wert[3]
	if decoded_info == []: return ''
	return decoded_info[0]

#

######################
### BILD zu STRING ###
######################
def bild2str(bild):
	img = Image.open(bild)
	x = pytesseract.image_to_string(img,lang='eng')
	if x == '': return None
	return x

def clip2bild2str():
	img = ImageGrab.grabclipboard()
	pfad = labomi + 'x.png'
	img.save(pfad)
	x = bild2str(pfad)
	return x

def clip2qr2str():
	img = ImageGrab.grabclipboard()
	pfad = labomi + 'x.png'
	img.save(pfad)
	x = qr2str(pfad)
	return x

def clip2bar2str():
	img = ImageGrab.grabclipboard()
	pfad = labomi + 'x.png'
	img.save(pfad)
	x = bar2str(pfad)
	return x

#

##### DIREKT ###############
if __name__=='__main__':
	bild = '__/xv_probe_qr.png'
	x = qr2str(bild)
	print( x )
	#
	bild = '__/xv_probe_bar.png'
	x = bar2str(bild)
	print( x )
	#
	x = bild2str(bild)
	print( x )
	#
	x = clip2bild2str()
	print( x )
	kbench.enfin()

