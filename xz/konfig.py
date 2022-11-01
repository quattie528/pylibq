try:
	import attrdict
except ModuleNotFoundError:
	pass
import io
from qenv3 import *
from .xzbase import *

#class confdict(attrdict.AttrDict):
#	pass

class confddic(dict):
	pass

####################
### YAML zu CONF ###
####################
def yml2cnf(txt):
	with open(txt, 'r',encoding='utf-8') as f:
		x = f.read()
	x = x.replace("\t",'  ')
#	x = x.replace('<UR>',mywkpl)
	try:
		x = x.replace('<LOKAL>/',myloca)
	except NameError:
		x = x.replace('<LOKAL>/',labomi)
#	x = x.replace(mywkpl+'/',mywkpl)

	ion = io.StringIO(x)
	dic = yaml.load(ion,Loader=yaml.BaseLoader)
#	pprint.pprint( dic )
	dic = attrdict.AttrDict(dic)
#	dic = confdict(dic)
	return dic

def yml2conv(txt):
	cnf = xz.yml2cnf(txt)
	res = {}
	for k,w in cnf.items():
		if isinstance(w, str):
			res[w] = k
		elif isinstance(w, list):
			for w2 in w:
				res[w2] = k
	return res

def cnf2cnf(txt):
	lis = xz.txt2lis(txt)
	lis = [ x.split("=") for x in lis ]
	lis = [ x for x in lis if len(x) == 2 ]
	dic = { x[0]:x[1] for x in lis }
	return dic

#

#########################
### DICT-DICT zu CONF ###
#########################
def ddic2cnf(ddic):
	res = confddic()
	for k,dic in ddic.items():
		res[k] = confdict(dic)
	return res

def ldic2cnf(ldic,k,**opt):
	cnf = ldic2ddic(ldic,k)
#	cnf = ldic2ddic(ldic,k,opt)
	cnf = ddic2cnf(cnf)
	return cnf
