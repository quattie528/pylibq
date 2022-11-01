def merge2dic(dic1,dic2):
	kopfer =  list( dic1.keys() )
	kopfer += list( dic2.keys() )
	kopfer = uniq(kopfer)

	dic3 = {}
	for k in kopfer:
		w1 = dic1[k]
		w2 = dic2[k]
		if w1 == '' and w2 == '':
			dic3[k] = ''
		elif w1 == '' and not w2 == '':
			dic3[k] = w1
		elif not w1 == '' and w2 == '':
			dic3[k] = w2
		elif not w1 == '' and not w2 == '':
			dic3[k] = w1 + ' / ' + w2
			print( '* SICHERN : ' + dic3[k] )
	return dic3

#

##############################
### LIST-DICT zu LIST-DICT ###
##############################
def ldic2ldic(ldic,vsdic,strict=True):
	res = []
	for dic in ldic:
		tmp = {}
		for des,aux in vsdic.items():
			if strict == True:
				tmp[aux] = dic[des]
			elif strict == False:
				try:
					tmp[aux] = dic[des]
				except KeyError:
					pass
		res.append(tmp)
	return res

#

########################################
### LIST-DICT zu LISTE der EIGENWERT ###
########################################
def ldic2ewlis(ldic,kolonne):
	lis = { d[kolonne]:0 for d in ldic }
	lis = list( lis.keys() )
	lis.sort()
	return lis

#

#################################
### DIC zu KEY ins Bestimmung ###
#################################
def dic2kkey(dic):

	### HAUPT ###
	rev = {}
	for x in dic.keys():
		if not isinstance(x, str): continue
		y = '' + x
		geh = False

		# Unterstrich
		for wert in " ":
			if wert in x:
				y = y.replace(wert,'_')
		# Nil
		for wert in ":'()?": #
			if wert in x:
				y = y.replace(wert,'')
		# Strip
		y = y.rstrip()
		y = y.lstrip()
		
		if x == y: continue
		rev[x] = y

	### ERSETZEN ###
	for x,y in rev.items():
		w = dic[x]
		dic[y] = w
		dic.pop(x)
	
	### AUSGABE ###
	return dic

def ldic2kkey(ldic):
	for dic in ldic:
		dic = dic2kkey(dic)
	return ldic

#

##########################
### UNIQ for LIST-DICT ###
##########################
def uniq4ldic(ldic,key,wert_in_front=True):
	res = []
	if wert_in_front == True: ldic.reverse()
	for dic in ldic:
		if res == []:
			res.append(dic)
		else:
			x = dic[key]
			y = res[-1][key]
			if x == y: res.pop()
			res.append(dic)
	if wert_in_front == True: res.reverse()
	return res
