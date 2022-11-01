### MODULES ###
#!/usr/bin/python

### MODULES ###
import os
import re
import sys
import pprint
import shutil
#
#import clipboard
#import attrdict
#
from datsun import *
from qenv3 import *
import xf
import xz
import kbench
from PIL import Image
from PIL import ImageDraw
#
#1:battery,2:pip,3:mygen,4:myopus

#A5 : 2330 x 3307 (by Canon DR-C225W)
GrosA4 = (2330,3307)
GrosA5 = (3307,4676)
#Bilden = xz.txt2lis('__/swipe2.list')
"""
[1]
Canon Name Rule Example
20170629213522_002.png

HIER SEHEN
D:/onedrive/comp/canon.txt

[2]
Unterlage für schreiben
D:/OneDrive/comp/conf3/mein/unterlageA4.pptx

[]
Ich kaufte das Sony Maschine an 2019-02-07 bei Amazon
"""

######################
### MERGE 2 IMAGE  ###
######################
def img2img(in1,in2,ex,nach='v'):
	i1 = Image.open(in1)
	if in2 == '':
		i2 = Image.new('1',(i1.size[0],i1.size[1]))
	else:
		i2 = Image.open(in2)

	#pos = (0,0,i1.size[0],i1.size[1])

	if nach == 'h':
		i3 = Image.new('1',(i1.size[0]*2,i1.size[1]))
	elif nach == 'v':
		i3 = Image.new('1',(i1.size[0],i1.size[1]*2))
	#
	i3.paste(i1,(0,0))
	#
	if nach == 'h':
		i3.paste(i2,(i1.size[0],0))
		i4 = ImageDraw.Draw(i3)
		i4.line((i1.size[0],0,i1.size[0],i1.size[1]),fill=0)
	elif nach == 'v':
		i3.paste(i2,(0,i1.size[1]))
		i4 = ImageDraw.Draw(i3)
		i4.line((0,i1.size[1],i1.size[0],i1.size[1]),fill=0)
	#
	i3.save(ex)
#	xz.__tell_output(ex)
	return i3

def img2imgH(in1,in2,ex): return img2img(in1,in2,ex,'h')
def img2imgV(in1,in2,ex): return img2img(in1,in2,ex,'v')

#

########################
### PDF for SONYBOOK ###
########################
def sonybook(pfad,ausgabe='D:/var/backup/y.pdf'):
	wurzel1 = 'D:/var/1/'
	wurzel2 = 'D:/var/2/'
	menge = (1653,1165)
	menge = (1165,1653)
	xf.retree(wurzel1)
	xf.retree(wurzel2)

	### HAUPT 1 ###
	lis = []
	feilen = os.listdir(pfad)
	feilen.sort()
	xz.notice = False
	#
	for i,x in enumerate(feilen):
		if not x[-4:] == '.png': continue
		x = pfad+x
		img = Image.open(x)
		img = img.resize(menge)
		ex = '%04d.png' % i
		ex = wurzel1 + ex
		img.save(ex)
		lis.append(ex)

	### HAUPT 2 ###
	res = []
	if len(lis) % 2 == 1:
		lis.append('')
	while 1:
		img1 = lis.pop(0)
		img2 = lis.pop(0)
		ex = img1.replace(wurzel1,wurzel2)
		img2imgH(img1,img2,ex)
		#
		res.append(ex)
		if lis == []: break

	### HAUPT 3 ###
	from fpdf import FPDF
	pdf = FPDF(orientation='L',unit='mm',format='A4')
	#
	for bild in res:
		pdf.add_page()
		pdf.image(bild,0,0,294,210)
		"""
		x,y = position coordinate
		w,h = weight and height
		"""

	### AUSGABE ###
	pdf.output(ausgabe, "F")
	xz.notice = True
#	xz.__tell_output(ausgabe)
	#
	xf.rmrf(wurzel1)
	xf.rmrf(wurzel2)

#

#####################################
### FUJI XEROX SIZE to CANON SIZE ###
#####################################
def xerox2canonsize(ordner):
	png = "D:/var/backup/biopolitik.png"
	name = '20170629213522_002.png'
	name = 'D:/var/spool/%d.png'
	cnt = 0

	for x in os.listdir(ordner):
		flg = False
		for ext in Bilden:
			if '.pdf' in x:
				break
			elif '.' + ext in x:
				flg = True
				break
		if flg == False: continue
		#
		img = Image.open(ordner+x)
		if img.size == (()):
			img.resize(GrosA4)
		elif img.size == (()):
			img.resize(GrosA5)
		#
		cnt += 1
		ex = name % cnt
		try:
			img.save(ex)
			sys.stdout.write("\tAusgabe als %s\n" % ex)
		except OSError:
			continue

#

######################################
### UMBENENNEN FUJI-XEROX zu CANON ###
######################################
def umbenennen_fx2canon(pfad):
	"""
3307,4676 # Canon
3310,4680 # FX

<Canon>20170629213600_009.png
<FX>20171003123754-0001.tif

20170629213600_009.png
20171003123754-0001.tif
	"""

	### HAUPT ###
	for x in os.listdir(pfad):

		## Tor ##
		if x == 'desktop.ini': continue # 2018-02-13
		if x == 'Desktop.ini': continue # 2018-02-13

		## Umbenennen ##
		y = x.replace('-0','_')
#		print( "%s -> %s" % (x,y) ) #d
		os.rename(pfad+x, pfad+y)

		## Größenänderung ##
		y = pfad+y
		i = Image.open(y)
		i = i.resize((3307,4676))
		ext = y[-4:]
#		print( ext ) #d
		if ext == '.tif':
			z = y.replace('.tif','.png')
		elif ext == '.jpg':
			z = y.replace('.jpg','.png')
		else:
			continue
#		z = y.replace('.png','.jpg')
#		z = y.replace('.tif','.jpg')
		"""
		I decided not to change my policy to use png
		Because jpg will degrade its quaility per every time of saving
		While png keeps its quality
		And I can put something like tag in the file names
		"""
		print( "%s -> %s" % (x,z) ) #d
		i.save(z)
		z = z.replace(pfad,'')
		#
		print("\tAusgabe als %s \n" % z)
#		sys.stdout.write("\tAusgabe als %s \n" % z)

#

def del_tif(pfad):
	dateien = os.listdir(pfad)
	geh = False
	for d in dateien:
		if d[-4:] == '.tif':
			os.remove(pfad+d)
			print( '* DEL',pfad )
			geh = True
	if geh == False:
		print( '* Kein TIF in die Ordner' )

#

################################
### DEDUPLICATION für ICARUS ###
################################
def dedup4md5():

	### MODUL ###
	import xk

	### KONSTANT ###
	pfad = IcarusPfad
	ds = xf.alle_dateien(pfad)
	res = []

	### HAUPT ###
	for d in ds:
		geh = False
		for ext in Bilden:
			if ext in d:
				geh = True
				break
		if geh == False: continue
		#
		k = xk.f2md5(d)
		res.append([d,k])

	### AUSGABE ###
	xz.tbl2txt(res,labomi+'x.tsv')

#

##### DIREKT ###############
if __name__=='__main__':
	mode = 2
	if mode == 1:
		x = 'D:/var/backup/x.jpg'
		y = 'D:/var/backup/y.jpg'
		z = 'D:/var/backup/z.jpg'
		w = img2imgH(x,y,z)
		print( w )
	elif mode == 2:
		memo2pdf9()
	elif mode == 3:
		xerox2canonsize('D:/var/spool/')

	### BIOPOLITIK PNGs to SONY-PDF ###
	elif mode == 4:
		pfad = 'D:/Dropbox/icarus/biopolitik/'
		ex = 'D:/var/backup/b.pdf'
		sonybook(pfad,ex)
	elif mode == 5:
		pfad = 'D:/var/img/'
#		pfad = 'D:/var/spool/'
#		pfad = 'C:/Users/kakagami/Downloads/wertlos/'
		umbenennen_fx2canon(pfad)
		del_tif(pfad)
	elif mode == 6:
		dedup4md5()

#D:\var\img\

"""
[CONCLUSION on 2019-01-21]
CubePDF is the solution to convert PNGs to PDF
I have decided to use this

This is a good solution too, but this has a limit of 20 pages
https://png2pdf.com/ja/
"""
