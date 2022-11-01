#!/usr/bin/python

### MODULES ###
import datetime as dt
import re
import os
import pprint
#
#import attrdict
#
from datsun import *
import xt
#import kbench
#
#1:battery,2:pip,3:mygen,4:myopus

### VARIABLES ###
debug = True
debug = False

def cutime(datei):
	return os.path.getctime(datei)

def mutime(datei):
	return os.path.getmtime(datei)

def autime(datei):
	return os.path.getatime(datei)

def ctime(datei):
	x = cutime(datei)
	return xt.u2p(x)

def mtime(datei):
	x = mutime(datei)
	return xt.u2p(x)

def atime(datei):
	x = autime(datei)
	return xt.u2p(x)

def cdate(datei):
	x = cutime(datei)
	return xt.u2d(x)
def mdate(datei):
	x = mutime(datei)
	return xt.u2d(x)
def adate(datei):
	x = autime(datei)
	return xt.u2d(x)

##################
### LETZER TAG ###
##################
def letzt(ordner,cond=''):

	dateien = os.listdir(ordner)
	if not cond == '':
		dateien = [ d for d in dateien if cond in d ]
	dateien = [ d for d in dateien if re.search('\d',d) ]
	#
	dateien.sort()
	datei = dateien[-1]
	return datei

def letzt2(ordner,regex):

	dateien = os.listdir(ordner)
	res = []
	for datei in dateien:
		m = re.search(regex,datei)
		m = m.group(1)
		res.append([datei,m])
	#
	res = sorted(res,key=lambda d:d[1])
	datei = res[-1][0]
	return datei

def letztzeit(ordner):
	ds2 = os.listdir(ordner)
	ds2 = [ [x,ctime(ordner+x)]  for x in ds2  ]
	ds2 = sorted(ds2,key=lambda d:d[1])
	return ds2[-1][0]

####################
### SERIE zu EIN ###
####################
def serie2ein(ordner,gemein,tag=45,**opt):
	import re
	dateien = os.listdir(ordner)
#	pprint.pprint( dateien ) #d
#	exit() #d

	### VORBEREITUNG ###
	if isinstance(tag, str):
		tag = xt.s2z(tag)
	elif isinstance(tag, int):
		tag = dt.date.today() - dt.timedelta(days=tag)
	else:
		assert( isinstance(tag, str) )

	### OPTIONEN ###
	rev = opt.get('reverse',False)
	dname = opt.get('filename',False)

	### HAUPT ###
	res = []
	for datei in dateien:
		## Ausnahme ##
		if not gemein in datei: continue
		if datei == gemein: continue
#		print( datei ) #d
		#
		m = re.search('(\d{4}-\d{2}-\d{2})',datei)
		if m:
			m = m.group(1)
		else:
			continue
		m = xt.s2z(m)
		if m < tag: continue # TAG PRUFUNG 1
		#
		print( '- ' + datei )
		v = ordner + datei
		#
		tmp = []
#		print( datei ) #d
		try:
			fh = open(v, 'r',encoding='utf-8')
			fh.read()
#			fh.rewind()
			fh.close()
			fh = open(v, 'r',encoding='utf-8')
		except UnicodeDecodeError:
			fh = open(v, 'r',encoding='sjis')
		for w in fh:
#			if not w[0:3] == '201' : continue
			w = w.rstrip("\r\n")
			w = w.rstrip("\n")
			tmp.append(w)
		fh.close()
#		tmp.pop()
		if rev == True:
			tmp.reverse()
		if dname == True:
			tmp.insert(0,datei)
		#
		for x in tmp:
			if x in res: continue
#			n = x[0:10]
#			n = n.replace('/','-')
#			n = xt.s2z(n)
#			if n < tag: continue # TAG PRUFUNG 2
			res.append(x)

	### AUSGANG ###
	return res

#

#######################################################################
### BEWEGT AUS dir.py ###
#########################
def alle_dateien(pfad):
	db = os.walk(pfad)
	res = []
	for tp in db:
		eigen = tp[0] + '/'
		dateien = tp[2]
		for x in dateien:
			y = eigen+x
			y = y.replace('\\','/')
			if y[0:2] == './': y = y[2:]
			res.append(y)
	res = [ x.replace('//','/') for x in res ]
	return res

def alle_ordner(pfad):
	ds = alle_dateien(pfad)
	ds = [ re.sub('(.+/).+','\\1',x) for x in ds ]
	ds = uniq(ds)
	return ds

"""
#Comment out @ 2019-06-30
def alle_dateien_2(pfad):
	db = os.walk(pfad)
	db = [ d[0].replace('\\','/') + '/' for d in db ]
	db = [ d.replace('//','/') for d in db ]
	return db
"""

def gesamtgrose(pfad,strict=True):
	res = alle_dateien(pfad)
	sum = 0
	for x in res:
		if strict == True:
			sum += os.path.getsize(x)
		else:
			try:
				sum += os.path.getsize(x)
			except PermissionError:
				pass
			except FileNotFoundError:
				pass
	return sum

def get_count(pfad):
	return len( alle_dateien(pfad) )

#

#############
### RM RF ###
#############
# ULTRA ACHTUNG !
def rmrf(pfad): #
	dateien = os.listdir(pfad)
	for datei in dateien:
		datei = pfad + datei
		os.remove(datei)
	os.rmdir(pfad)

#############
### MKDIR ###
#############
def mkdir2(pfad):
	if not pfad[-1] == '/':
		pfad = re.match('(.+/).+',pfad)
		pfad = pfad.group(1)
	pfad = pfad[0:-1]
	if os.path.exists(pfad):
		return True
	pfad = pfad.split('/')
	#
	res = ''
	for x in pfad:
		res = res + x + '/'
		if os.path.exists(res):
			continue
		else:
			os.mkdir(res)
	try:
		print( res )
	except UnicodeEncodeError:
		print( '[etwas]' )
	return res

#

#############
### RMDIR ###
#############
def rmdir2(pfad):
	pfade = alle_dateien(pfad)
	pfade.reverse()
	res = []
	for w in pfade:
		if alle_dateien(w) == 0:
			os.rmdir(w)
			res.append(w)
		else:
			continue
	#
	for w in res:
		try:
			print( 'Deleted this : %s' % w )
		except UnicodeEncodeError:
			print( '[etwas]' )
		return res

#

##############
### RMTREE ###
##############
def retree(pfad):
	import shutil
	#
	if os.path.exists(pfad):
		shutil.rmtree(pfad)
	while 1:
		try:
			os.mkdir(pfad)
			break
		except PermissionError:
			continue

#-------------------------------------------------

def findfat(pfad):
	res = []
	w = byte(pfad)
	#
	res.append([w,pfad])
	#
	while 1:
		dic = {}
		dateien = os.listdir(pfad)
		flg = False
		for x in dateien:
			x = pfad+x
			if os.path.isdir(x):
				flg = True
				x += '/'
				w = byte(x)
				dic[w] = x
		if flg == True:
			g = max(dic.keys())
			pfad = dic[g]
			res.append([g,pfad])
		elif flg == False:
			break
	try:
		import xz
		xz.show(res)
	except ImportError:
		for x in res:
			x[0] = commify(x[0])
			print( ' || '.join(x) )

#

#############################
### ÄLTER RANG in DATEIEN ###
#############################
def aelter(pfad,rang=20):
	ds = alle_dateien(pfad)
	zt = 0
	ds = [ [d,xt.u2p(mtime(d))] for d in ds ]
	ds = sorted(ds,key=lambda d:d[1])
	ds.reverse()
	#
	res = []
	n = 1
	for paar in ds:
		zt = paar[1]
		zt = str(zt)
		datei = paar[0]
		if datei[-4:] == '.pyc': continue
		tmp = [n,zt,datei]
		res.append(tmp)
		n += 1
		if n == rang + 1: break
	pprint.pprint( res )

#

#########################
### ÄLTEST in DATEIEN ###
#########################
def aeltest(dateien):
	res = []
	for d in dateien:
		zt = mtime(d)
		res.append([d,zt])
	res = sorted(res,key=lambda d:d[1])
#	pprint.pprint( res ) #
	x = res[-1][0]
#	print( x ) #d
	return x

#

####################
### DATEI zu TAG ###
####################
def datei2tag(datei,regex='(\d{8})'):
	m = re.search(regex,datei)
	tag = m.group(1)
	tag = '-'.join( [ tag[0:4], tag[4:6], tag[6:8] ] )
	tag = xt.s2d(tag)
	return tag

#

#####################
### ABSOLUTE PFAD ###
#####################
def abspfad(x):
#	print( x ) #d
	q = os.path.dirname( x )
#	print( q ) #d
	q = q.replace('\\','/')
	q = q.replace('//','/')
	q += '/'
	return q

#

##### DIREKT ###############
if __name__=='__main__':
	pass

#0000071508_10K_2015Q1a

"""
### MEMO @ 2018-12-23 ###
ONE DAY I HAVE TO DO "xf.py" + "xo.py"
These 2 files are similar but messed

### MEMO @ 2018-12-24 ###
ONE DAY I HAVE TO DO "xf.py" + "xo.py" + "dir.py"
These 2 files are similar but messed

### MEMO @ 2020-03-XX ###
get_all_files() -> alle_dateien()
get_all_size() -> gesamtgrose()
"""
#C:\Users\kakagami\AppData\Local\Temp
