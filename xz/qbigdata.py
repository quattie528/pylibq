from .xzbase import *
#import cStringIO
import io

def csv2lns(datei):
	import csv
	import codecs
	import chardet

	tmp = labomi + '000.000.csv'
	koda = 'utf-8'
	with open(datei, 'r',encoding='utf-8') as fh:
		while 1:
			x = fh.readline()
#			tmp = io.StringIO(x)
			with open(tmp, 'w',encoding='utf-8') as gh:
				gh.write(x)
			lis = xz.csv2tbl(tmp)
			if lis == []: break
			yield lis[0]
#			spamreader = csv.reader(x)
#			tmp = []
#			for reihe in spamreader:
#				tmp.append(reihe)
#			yield tmp
#			continue
#		
#		tmp = chardet.detect(x)
#		if tmp['encoding'] == 'SHIFT_JIS':
#			koda = 'sjis'
#		elif tmp['encoding'] == 'ISO-8859-1': # opn.py
#			koda = 'latin1'
#		else:
#			koda = 'utf-8'
#		#
#		with codecs.open(datei,encoding=koda) as csvfile:
#			spamreader = csv.reader(csvfile)
#			for i, reihe in enumerate(spamreader):
#				if reihe == []:
#					res.append(reihe)
#					continue
#				if not reihe[0] == '': # 2018-05-27
#					if reihe[0][0] == '\ufeff': #== BOM
#						reihe[0] = reihe[0].replace('\ufeff','')# DEL
#				res.append(reihe)
#	#	xz.tbl2txt(res,ausgabe)
#		return res
