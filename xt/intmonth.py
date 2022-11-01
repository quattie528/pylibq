#!/usr/bin/python

### MODULES ###
#from datetime import date as d
#from datetime import time as t
from datetime import date as dy # ein Alphabet ist gefehr
from datetime import time as tm # ein Alphabet ist gefehr
from datetime import datetime as dt
from datetime import timedelta as dl
import calendar
from .xtbase import is_n
#from .finplus import imvec # intmonth.py < finplus.py 
from datsun import *

#

###############################################
### N = INTMONTH = INTEGER MONTH = INTMONAT ###
###############################################
def n2d(m,ende=True):
	assert is_n(m)
	j = m // 100
	m = m % 100
	if ende == True:
		t = calendar.monthrange(j,m)[1]
	elif ende == False:
		t = 1
	return dy(j,m,t)

def n2me(im):
	assert is_n(im)
	return n2d(im,True)

def s2n(x):
	assert( isinstance(x, str) )
	if re.search('[a-zA-Z]',x): return x

	x = re.sub(' \d\d:\d\d:\d\d$','',x)
	x = re.sub('-\d\d$','',x)
	x = x.replace('-','')
	x = int(x)
	is_n(x)

	return x

def d2n(x):
	assert( isinstance(x, dy) )
	return x.year * 100 + x.month

#-------------------------------------------------

###########
### N+- ###
###########
def nplus(x):
	rev = False
	if not is_n(x):
		if is_n(200000+x):
			rev = True
			x = 200000 + x
		else:
			return x
	x += 1
	if x % 100 == 13:
		x += 88
	assert is_n(x)
	if rev == True:
		x = x - 200000
	return x

def nminus(x):
	rev = False
	if not is_n(x):
		if is_n(200000+x):
			rev = True
			x = 200000 + x
		else:
			return x
	x -= 1
	if x % 100 == 0:
		x -= 88
	assert is_n(x)
	if rev == True:
		x = x - 200000
	return x

#

##############
### VEKTOR ###
##############
#seh "finplus.py".qvec()
def nvec(ini,fin=0,interval=1):
	assert is_n(ini)
	if not fin == 0: assert is_n(fin)
	assert interval in [1,2,3,4,6]

	if fin == 0:
		fin = dy.today()
		fin = fin.year * 100 + fin.month
	initmonth = ini % 100
	while 1:
		initmonth += interval
#		print( initmonth ) #d
		if initmonth > 12:
			initmonth = initmonth - 12
			break
	#
	res = [ini]
	i = ini + 0
#	print( i ) #d
	while 1:
		i += interval
#		if i % 100 >= 13:
#			i -= interval
#			i -= 11
#			i += 100
		if i % 100 >= 13:
			i = i // 100
			i += 1
			i *= 100
			i += initmonth
		if i > fin:
			break
		res.append(i)
	return res

## Alias ##
imvec = nvec
intmonths = nvec

#

############################
### DICT-DICT zu TABELLE ###
############################

### INTMONTH VEKTOR ###
def nddic2imvec(nddic):
	ims = list( nddic.keys() )
	ims.sort()
	ini = ims[0]
	fin = ims[-1]
	ims = imvec(ini,fin)
	return ims

def nddic2vs(nddic):
	vs2 = []
	for im,dic in nddic.items():
		vs2 += list(dic.keys())
	vs2 = uniq(vs2)
	return vs2

### ERFULL ###
def nddic2erfull(nddic,vs=[]):
	"""
	nddic[im][val] = int or float
	"""

	### KEYS ###
	ims = nddic2imvec(nddic)
	if vs == []:
		vs2 = nddic2vs(nddic)
	else:
		vs2 = [ x for x in vs ]

	### REINDEX ###
	for im in ims:
		if not im in nddic:
			nddic[im] = {}
		#
		for kol in vs2:
			if kol in nddic[im]: continue
			nddic[im][kol] = ''

	### AUSGABE ###
	return nddic

### TABELLE ###
def nddic2ntbl(nddic,vs=[]):

	### KEYS ###
	nddic = nddic2erfull(nddic,vs)
	ims = nddic2imvec(nddic)
	if vs == []:
		vs2 = nddic2vs(nddic)
	else:
		vs2 = [ x for x in vs ]

	tbl = []
	for im in ims:
		x = '_%d' % im
		lis = [x]
		for kol in vs2:
			lis.append(nddic[im][kol])
		tbl.append(lis)
	vs2.insert(0,'/')
	tbl.insert(0,vs2)
	tbl.append(vs2)
	return tbl

### TABELLE PLUS ###
def nddic2ntblplus(nddic,vs=[]):

	### KEYS ###
	nddic = nddic2erfull(nddic,vs)
	ims = nddic2imvec(nddic)
	if vs == []:
		vs2 = nddic2vs(nddic)
	else:
		vs2 = [ x for x in vs ]

	### HAUPT ###
	for im in ims:
		n = [ w for w in nddic[im].values() ]
		while 1:
			try:
				n.remove('')
			except ValueError:
				break
		n = sum(n)
		n = round(n,2)
		nddic[im]['Σ'] = n
	#
	summe = nplus(ims[-1])
	nddic[summe] = {}
	vs2.insert(0,'Σ')
	for kol in vs2:
		n = 0
		for im in ims:
			if nddic[im][kol] == '': continue
			n += nddic[im][kol]
		n = round(n,2)
		nddic[summe][kol] = n

	tbl = nddic2ntbl(nddic,vs2)
	tbl[-2][0] = 'Σ'
	return tbl

"""
def nddic2jtblplus(nddic,vs=[]):

	### KEYS ###
	nddic = nddic2erfull(nddic,vs)
	ims = nddic2imvec(nddic)
	im2j = { im:im//100 for im in ims }
	if vs == []:
		vs2 = nddic2vs(nddic)
	else:
		vs2 = [ x for x in vs ]

	### HAUPT ###
	res = { j:{} for j in im2j.values() }
	for j in res.keys():
		for k in vs2:
			res[j][k] = 0
	#
	for im in ims:
		j = im2j[im]
		for k in vs:
			res[j][k] += nddic[im][k]

	### HAUPT (kopiert aus nddic2jtblplus() ###
	jahren = list(res.keys())
	jahren.sort()
	#
	for j in jahren:
		n = [ w for w in res[j].values() ]
		while 1:
			try:
				n.remove('')
			except ValueError:
				break
		n = sum(n)
		n = round(n,2)
		res[j]['Σ'] = n
	#
	summe = nplus(ims[-1])
	res[summe] = {}
	vs2.insert(0,'Σ')
	for kol in vs2:
		n = 0
		for j in ims:
			if res[j][kol] == '': continue
			n += res[j][kol]
		n = round(n,2)
		res[summe][kol] = n

	tbl = nddic2ntbl(nddic,vs2)
	tbl[-2][0] = 'Σ'
	return tbl
Use pands for this type of calculation
"""

#

##################
### GESCHICHTE ###
##################

### MOVED from xd.py ###
"""
[Comment out @ 2018-10-28]
### INT MONTH ###
class intmonth(int):
	def __myfunc__(n):
		if n % 100 <= 12:
			return True
		else:
			return False

	def __new__(cls,n):
		if cls.__myfunc__(n) == False:
			raise ValueError('not intmonth')
		return super().__new__(cls,n)

	def __iadd__(my,n):
		n = my + n
		if n % 100 > 12:
			n = n + 88
		return intmonth(n)

	def __isub__(my,n):
		n = my - n
		if n % 100 > 12:
			n = n - 88
		elif n % 100 <= 0:
			n = n - 88
		return intmonth(n)
"""

M2STABLE = {}

#

############
### SEIN ###
############
def is_n(m):
	try:
		assert( isinstance(m, int) )
		assert m in range(190001,210000)
		assert m % 100 in range(1,12+1)
	except AssertionError:
		return False
	return True

def is_q(w):
	try:
		assert( isinstance(w, str) )
		assert len(w) == 6
		j = int(w[0:4])
		q = int(w[-1])
		assert j in range(1900,2100)
		assert q in range(1,5)
	except AssertionError:
		return False
	return True

def is_me(x): # Monatsende
	if isinstance(x, str):
		x = s2z(x)
	assert( isinstance(x, dy) )
	y = calendar.monthrange(x.year,x.month)[1]
	y = dy(x.year,x.month,y)
#	print( x ) #d
#	print( y ) #d
	if x == y:
		return True
	else:
		return False
