#!/usr/bin/python

### MODULES ###
import os
from PIL import Image
import PIL.ImageOps

### KONSTANT ###
notice = True
binary = True

"""
http://hp.vector.co.jp/authors/VA032610/JPEGFormat/StructureOfJPEG.htm
SOI スタートマーカ (Start of Image) 　0xFFD8
EOI エンドマーカ 　(End of Image) 　　0xFFD9

DQT 量子化テーブル定義　　(Define Quantization Table) 0xFFDB
DHT ハフマンテーブル定義　(Define Huffman Table)　　　0xFFD4
-------------------------------------------------
[raster]
'rgb' 	SGI ImgLib Files
'gif' 	GIF 87a and 89a Files
'pbm' 	Portable Bitmap Files
'pgm' 	Portable Graymap Files
'ppm' 	Portable Pixmap Files
'tiff' 	TIFF Files
'rast' 	Sun Raster Files
'xbm' 	X Bitmap Files
'jpeg' 	JPEG data in JFIF or Exif formats
'bmp' 	BMP files
'png' 	Portable Network Graphics

[vector]
SVG
EPS
PDF
AI
"""

def imageformat(img):
	return imghdr.what(img)

def istbild(x):
	bilden = ['jpg','jpeg','png','bmp','gif','tif']
	for bild in bilden:
		ext = '.' + bild
		if x.lower().endswith(ext): return True
	return False

#

################
### EIN BILD ###
################
def bild2grosse(img,xaxis,yaxis):
	img = img.resize((xaxis,yaxis))
	return img

def bild2abscheid(img,axis):
	img = img.crop(axis)
	return img

def bild2halb(img):

	### KONSTANT ###
	xaxis = img.size[1]
	yaxis = img.size[0]
	xaxis0 = img.size[1]
	xaxis2 = img.size[1] // 2
	yaxis0 = img.size[0]
	yaxis2 = img.size[0] // 2
	#
	if xaxis < yaxis: #
		mode = 'landschaft'
		axis1 = (0,0,yaxis2,xaxis0) # OK
		axis2 = (yaxis2,0,yaxis0,xaxis0)
	else:
		mode = 'portrait'
		axis1 = (0,0,yaxis0,xaxis2) # OK
		axis2 = (0,xaxis2,yaxis0,xaxis0)

#	print( mode )
#	print( 1,axis1 )
#	print( 2,axis2 )
	img1 = img.crop(axis1)
	img2 = img.crop(axis2)
	return img1,img2

def bild2umkehren(img):
	#2017-01-06
	#http://stackoverflow.com/questions/2498875/how-to-invert-colors-of-image-with-pil-python-imaging
	umkehre = ''
	if img.mode == 'RGBA':
		r,g,b,a = img.split()
		rgb_img = img.merge('RGB', (r,g,b))
		umkehre = PIL.ImageOps.invert(rgb_img)
		r2,g2,b2 = umkehre.split()
#		final_transparent_img = img.merge('RGBA', (r2,g2,b2,a))
#		final_transparent_img.save('new_file.png')
	else:
		umkehre = PIL.ImageOps.invert(img)
#		umkehre.save('new_name.png')
	return umkehre

#

#########################
### GEGENTEILIGEFARBE ###
#########################
def gegenteiligeFarbe(s):
	"""
	反転色 : 1EB7BA -> E14845
	補色   : 1EB7BA -> BA211E
	"""
	debug = True
	debug = False
	assert s[0] == '#'
	assert len(s) == 7
	s2 = [ s[1:3], s[3:5], s[5:7] ]
	#
#	for i in range(3): print( s[i], int(s[i],16) )
	r = [ 255 - int(s2[i],16) for i in range(3) ]
	q = [ '%02x' % r[i] for i in range(3) ]
	if debug == True:
		print( '*'*40 )
		print( 'DIV :',s,'->',s2 )
		print( 'x16 :',s,'->',r )
		print( 's16 :',s,'->',q )
	res = ''.join(q)
	res = '#' + res
	res = res.upper()
	return res

#

######################
### BILDEN zu BILD ###
######################
def bilden2bild(bilden,ausgabe='a.png',xlen=4,ylen=3):
	print( len(bilden) )
	print( xlen * ylen )
	assert len(bilden) <= xlen * ylen

	res = Image.open(bilden[0])
	xori,yori = res.size
	res = Image.new('1',(xori*xlen,yori*ylen))

	xnow = 0
	ynow = 0
	for i,bild in enumerate(bilden):
		bild = Image.open(bild)
		res.paste(bild,(xnow,ynow))
		xnow += xori
		if xnow / xori == xlen :
			ynow += yori
			xnow = 0
	print( ausgabe )
	res.save(ausgabe)

def mbilden2bild(des,ex): bilden2bild(des,ex,4,3)
def qbilden2bild(des,ex): bilden2bild(des,ex,2,2)

#

######################
### BILD zu STRING ###
######################
def bild2str(datei,sprache='eng'):
	import pytesseract as ocr

	### same drive rule, on windows ##
	#https://github.com/madmaze/pytesseract/issues/50
	hier = os.getcwd()
	os.chdir('C:')

	cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract.exe'
	#cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract'
	cmd = 'C:/usr/Tesseract-OCR/tesseract.exe'
	cmd = 'C:/usr/Tesseract-OCR/tesseract'
	ocr.pytesseract.tesseract_cmd = cmd

	# Simple image to string
	img = Image.open(datei)
	#x = ocr.image_to_string(img,lang='fra')
	x = ocr.image_to_string(img,lang=sprache)
	return x

#


def negate(bilddatei,sicher=True):
	im = Image.open(bilddatei)
	im_invert = PIL.ImageOps.invert(im)
	if sicher == True:
		im_invert.save(bilddatei+'.png')
	return im_invert

#

##### DIREKT ###############
if __name__=='__main__':
	pass
