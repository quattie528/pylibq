#!/usr/bin/python

### MODULES ###
#import datetime
#import os
import pprint
#
import pickle
import pandas as pd
import sqlalchemy as sa
#
from datsun import *
import xz
#import kbench
#
#1:battery,2:pip,3:mygen,4:myopus

### VARIABLES ###
debug = True
debug = False

"""
CRUD-PRINZIP

+-------+--------+--------+---------+
|       | SQL    | HTML   | DDS     |
+-------+--------+--------+---------+
|CREATE : INSERT | POST   | write   |
|READ   : SELECT | GET    | read    |
|UPDATE : UPDATE | PUT    | write   |
|DELETE : DELETE | DELETE | dispose |
+-------+--------+--------+---------+
#
INFO    : READ { scalar, meta }
DEDUP   : UPDATE AND DELETE { dedup }
DUMP    : READ
EXECUTE : SQL

-------------------------------------------------
[DEU Sprachen]
Spalten
Felder [DEU] == field [ENG]
"""

### KLASS als SQLALCHEMY MEDIUM #######################################
class SAM():
	model = ''
	dbengine = ''

	def __init__(m,model,dbengine):
		m.model = model
		m.dbengine = dbengine

#

	##############
	### SCALAR ###
	##############
	def count(m,spalte='id'):
		x = sa.select([sa.sql.func.count(m.model.c[spalte])])
		res = m.dbengine.execute(x)
		res = res.scalar()
		return res

	def max(m,spalte='id'):
		x = sa.select([sa.sql.func.max(m.model.c[spalte])])
#		x = sa.select([m.model]).order_by(sa.desc(spalte)).limit(1)
		res = m.dbengine.execute(x)
		res = res.scalar()
		return res

	def min(m,spalte='id'):
		x = sa.select([sa.sql.func.min(m.model.c[spalte])])
#		x = sa.select([m.model]).order_by(sa.desc(spalte)).limit(1)
		res = m.dbengine.execute(x)
		res = res.scalar()
		return res

#	def last(m,spalte='id'):
#		x = sa.select([m.model.c[spalte]])
#		res = m.dbengine.execute(x)
#		res = res[0]
#		res = res.scalar()
#		return res

	############
	### META ###
	############
	def cols(m):
		return list( m.model.c.keys() )

	##############
	### CREATE ###
	##############
	def dic2db(m,dic,key=None): # CREATE + UPDATE
		dic2sa2db(m.model,m.dbengine,dic,key)

	def ldic2db(m,ldic,key=None): # CREATE + UPDATE
		ldic2sa2db(m.model,m.dbengine,ldic,key)

	############
	### READ ###
	############
	def getldic(m,spalten=[],where={}):
		if isinstance(spalten, str): spalten = [spalten]
		#
		if spalten == []:
			stmt = sa.select([m.model])
		else:
			stmt = [ m.model.c[sp] for sp in spalten ]
			stmt = sa.select(stmt)
		#
		if not where == {}:
			for k,w in where.items():
				stmt = stmt.where(m.model.c[k]==w)
		res = m.dbengine.execute(stmt)
		res = [ dict(x) for x in res ]
		return res

	def getlist(m,spalte=[],where={}):
		res = m.getldic(spalte,where)
		res = [ x[spalte] for x in res ]
		return res

	def uniq(m,spalte):
		# apply to any column to get unique values
		stmt = sa.select([m.model.c[spalte]])
		stmt = stmt.distinct(m.model.c[spalte])
		res = m.dbengine.execute(stmt)
		res = [ x[0] for x in res ]
		res = [ x for x in res if x != None ]
		res = [ x for x in res if x != '' ]
		res.sort()
		return res

	def selcol(m,columns):
		stmt = [ m.model.c[col] for col in columns ]
		stmt = sa.select(stmt)
		res = m.dbengine.execute(stmt)
		res = [ dict(x) for x in res ]
		return res

	def select(m,conddic={}):
		stmt = sa.select([m.model])
		for k,w in conddic.items():
			stmt = stmt.where(m.model.c[k]==w)
		res = m.dbengine.execute(stmt)
		res = [ dict(x) for x in res ]
		return res

	def selectlike(m,conddic={}):
		stmt = sa.select([m.model])
		for k,w in conddic.items():
			stmt = stmt.where( m.model.c[k].like('%'+w+'%') )
		res = m.dbengine.execute(stmt)
		res = [ dict(x) for x in res ]
		return res

	##############
	### UPDATE ###
	##############
	def replace(m,des,aux,spalte):
		# apply to string column to replace

		### SQL ###
		c = m.model.c
		des2 = '%' + des + '%'
		sql = sa.select([c.id,c[spalte]]).where(c[spalte].like(des2))
		res = m.dbengine.execute(sql)
		res = [ dict(x) for x in res ]
		if res == []:
			print( 'Kein Sache zu bearbeiten...' )
			return True

		### HAUPT ###
		mdl = m.model
		for dic in res:
			id = dic['id']
			w1 = dic[spalte]
			w2 = w1.replace(des,aux)
			print( dic )
			#
			dic = { spalte:w2 }
			stmt = sa.update(mdl).where(mdl.c.id==id).values(**dic)
			m.dbengine.execute(stmt)

	##############
	### DELETE ###
	##############
	def delete(m,conddic):
		stmt = sa.delete(m.model)
		for k,w in conddic.items():
			stmt = stmt.where(m.model.c[k]==w)
		m.dbengine.execute(stmt)
		return True

	#############
	### DEDUP ###
	#############
	def dedup(m,refid,gegenstand):
		stmt = sa.select([ m.model.c[refid], m.model.c[gegenstand] ])
		db = m.dbengine.execute(stmt)
		db = [ dict(x) for x in db ]
		dupdic = {}
		for dic in db:
			wert = dic[gegenstand]
			id = dic[refid]
			if wert in dupdic:
				dupdic[wert].append(id)
			else:
				dupdic[wert] = [id]
		#
		keys = list( dupdic.keys() )
		for wert in keys:
			if len( dupdic[wert] ) == 1:
				dupdic.pop(wert)
		return dupdic

	############
	### DUMP ###
	############
	def tsv(m,ausgabe,**opt):

		### OPTIONEN ###
		sql = sa.select([m.model])
		if 'order' in opt:
			for spalte in opt['order']:
				sql = sql.order_by(spalte)

		### HAUPT ###
		ldic = m.dbengine.execute(sql)
		ldic = [ dict(dic) for dic in ldic ]
		vs = m.cols()
		xz.ldic2txt(ldic,ausgabe,vs)
		return ldic

	###############
	### EXECUTE ###
	###############
	def exe(m,stmt):
		res = m.dbengine.execute(stmt)
		if 'UPDATE' in stmt :
			return True
		else:
			res = [ dict(x) for x in res ]
		return res
		#↑2022-05-07
		"""
		try:
			res = [ dict(x) for x in res ]
		except sa.exc.ResourceClosedError:
			return True
		return res
		"""

#

### NON-KLASS als SQLALCHEMY MEDIUM ###################################

#

def mod2dbengine(mod):
	if isinstance(mod, sa.engine.base.Engine):
		return mod
	else:
		dbh = mod.dbengine
		return dbh

#

#######################################
### DICT zu SQL ALCHEMY zu DATABASE ###
#######################################
def dic2sa2db(model,dbh,dic,key=None):

	dbh = mod2dbengine(dbh)

	try:
		idty = dic[key]
	except KeyError:
		idty = None
		rp = None

	if not idty == None:
		stmt = sa.select([ model.c[key] ])
		stmt = stmt.where( model.c[key]==idty )
		rp = dbh.execute(stmt)
		rp = rp.scalar()

	if rp == None:
		print( '* UNSEIN, daher EINLEGEN >>%s<<' % (idty) )
		stmt = model.insert().values(**dic)
	else:
		print( '* SEIN, daher BEARBEITEN >>%s<<' % (idty) )
#		if idty == 'id': dic.pop(idty)
		stmt = sa.update(model)
		stmt = stmt.where(model.c[key]==idty)
		stmt = stmt.values(**dic)
	rp = dbh.execute(stmt)
	return rp

#

############################################
### LIST-DICT zu SQL ALCHEMY zu DATABASE ###
############################################
def ldic2sa2db(model,dbh,ldic,key=None):

	### KONSTANT ###
	if key == None:
		sein = []
	else:
		stmt = sa.select([ model.c[key] ])
		sein = dbh.execute(stmt)
		sein = [ x[0] for x in sein ]
	dbh = mod2dbengine(dbh)

	### HAUPT ###
	tmp = []
	with dbh.connect() as conn:
		with conn.begin() as trans:
			for i,dic in enumerate(ldic):
				if key == None:
					stmt = model.insert().values(**dic)
				else:
					ref = dic[key]
					if ref in sein:
						stmt = sa.update(model)
						stmt = stmt.where(model.c[key]==ref)
						stmt = stmt.values(**dic)
					else:
						stmt = model.insert().values(**dic)
				conn.execute(stmt)
			res = trans.commit()
#			print( '* ERFOLG der COMMIT:',res ) #d
	return True

#

##### DIREKT ###############
if __name__=='__main__':
	pass
