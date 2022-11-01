#!/usr/bin/python

### MODULES ###
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import xz
import xt
import os
from datsun import *

### VARIABLES ###
debug = True

##########
### IO ###
##########
def txt2pd(txt):
	fh = open(txt, 'r')
	idx = fh.readline().split("\t")[0]
	chk = fh.readline().split("\t")[0]
	fh.close()
	#
#	df = pd.read_csv(txt,sep="\t")
	df = pd.read_csv(txt,sep="\t",index_col=idx)
	return df

def pd2txt(df,ausgabe):
	df.to_csv(ausgabe,sep="\t")
	ausgabe = ausgabe.replace('.tsv','.bin')
	xz.obj2bin(df,ausgabe)

def dffig2mono(fig,ausgabe='a.png'):
	import xi
	tmp = 'b.png'
	if ausgabe == 'b.png':
		tmp = 'a.png'
	fig.savefig(tmp)
	fig = xi.negate(tmp)
	fig.save(ausgabe)
	xz.__tell_output(ausgabe)

###################
### PIVOT TABLE ###
###################
def xsumme(df,dic):
	assert isinstance(df, pd.core.frame.DataFrame)
	assert isinstance(dic, dict)
	return df.groupby(dic).sum()

def ysumme(df,dic):
	assert isinstance(df, pd.core.frame.DataFrame)
	assert isinstance(dic, dict)
	return df.groupby(dic,axis=1).sum()

def xysumme(df,xdic,ydic):
	assert isinstance(df, pd.core.frame.DataFrame)
	assert isinstance(xdic, dict)
	assert isinstance(ydic, dict)
	return df.groupby(xdic).sum().groupby(ydic,axis=1).sum()

def summe(df):
	assert isinstance(df, pd.core.frame.DataFrame)
	return df.sum().sum()

################
### DIAGRAMM ###
################
def diagramm(df,ex='a.png',gattung='line'):
	p = df.plot(
		kind=gattung,
		figsize=(19.2,10.8),
		title='GEROP'
#		secondary_y = True,
	)
	return p

def line(df,ex='a.png'):
	p = diagramm(df,ex,'line')
	fig = p.get_figure()
	plt.close()
	pd2png(fig)

def bar(df,ex='a.png'):
	p = diagramm(df,ex,'bar')
	fig = p.get_figure()
	plt.close()
	pd2png(fig)

def barh(df,ex='a.png'):
	p = diagramm(df,ex,'barh')
	fig = p.get_figure()
	plt.close()
	pd2png(fig)

def area(df,ex='a.png'):
	p = diagramm(df,ex,'area')
	fig = p.get_figure()
	plt.close()
	pd2png(fig)

def bars(df,ex='a.png'):
	p = df.plot(
		kind='bar',
		figsize=(19.2,10.8),
		stacked=True,
#		secondary_y = True,
	)
	fig = p.get_figure()
	plt.close()
	pd2png(fig)

#

##########################
### PANDS zu DICT-DICT ###
##########################
def pds2ddic(pds,key1,key2,wert):
	ddic = xz.dictdict()
	for idx,tup in pds.iterrows():
		dic = dict(tup)
		r1 = dic[key1]
		r2 = dic[key2]
		w  = dic[wert]
		if not r1 in ddic:
			ddic[r1] = {}
		ddic[r1][r2] = w
	return ddic

def pds2ldic(pds,keys):
	ldic = xz.listdict()
	for idx,tup in pds.iterrows():
		dic = {}
		for k,w in dict(tup).items():
			typ = str(type(w))
			if typ == "<class 'int'>":
				dic[k] = int(w)
			if typ == "<class 'float'>":
				dic[k] = float(w)
			else:
				dic[k] = str(w)
		ldic.append(dic)
	return ldic

#

###############
### AUSGABE ###
###############
def pds2tsv(df,tsv):
	df.to_csv(tsv,sep="\t",index=False)

def pds2bin(df,bin):
	df.to_pickle(bin)

def pds2ldic(df):
	return df.to_dict(orient='records')

def dtiseries(ini,fin,frq='D'):
	tage = pd.date_range(
		start=ini,
		end=fin,
		freq=frq,
		name='tag'
	)
	tage = pd.DataFrame(range(len(tage)),index=tage)
	tage.columns=['X']
	tage.X = 0
	return tage


#

#########################
### PANDAS zu TABELLE ###
#########################
def pd2tbl(df):
	xs = list(df.columns)
	ys = df.index
	res = df.values.tolist()
	for i,lis in enumerate(res):
		lis.insert(0,ys[i])
	xs.insert(0,0)
	res.insert(0,xs)
	return res

#

###########################################
### INTMONAT PANDAS zu INTMONAT TABELLE ###
###########################################
def ndf2ntbl(df,tblmode=True):
	xs = list(df.columns)
	ys = df.values.tolist()[0]
	dic = { xs[i]:ys[i] for i in range(len(xs)) }
	res = {}
	for im,w in dic.items():
		j = xt.n2y(im)
		m = xt.n2m(im)
		if not j in res: res[j] = {}
		res[j][m] = w
	
	tblmode = True
	if tblmode == True:
		tbl = []
		jahren = list( res.keys() )
		jahren.sort()
		for j in jahren:
			lis = [j]
			for m in range(12):
				m += 1
				lis.append( res[j].get(m,0) )
			tbl.append(lis)
		monaten = [ m for m in range(13) ]
		tbl.insert(0,monaten)
		res = tbl

	return res

#

####################
### WIDE zu TIDY ###
####################
#https://www.jstatsoft.org/article/view/v059i10
#D:/OneDrive/comp/tips/Hadley_Wickham_(2014)_#Tidy_Data#.pdf
def wide2tidy(wide,opt={}):
	tidy = wide.melt(**opt)
	return tidy

def test4wide2tidy():
	wide = [
		["Tokyo",5.8,5.7,5.6],
		["Osaka",6.8,6.7,6.6],
		["Nagoya",5.1,5.1,5.0],
	]
	lis = ['Location'] + pd.date_range('2020-01-01',periods=3).tolist()
	wide = pd.DataFrame(wide,columns=lis)
	dic = {
		'id_vars':'Location',
		'var_name':'Date',
		'value_name':'Temperation',
	}
	#
	print( wide )
	print( '%'*40 ) #d
	tidy = wide2tidy(wide,dic)
	print( tidy )

#

##### DIREKT ###############
if __name__=='__main__':
	test4wide2tidy()
#	df = txt2pd('c.tsv')
#	df.info()
#	dic = xz.txt2dic('c.txt')
#	d = ysumme(df,dic)
#	print( d )
#	line(df)

#base is from df1zs.py
