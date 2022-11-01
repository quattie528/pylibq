
def defdict(bestimmung):
	assert isinstance(bestimmung, dict)
	dic = {}
	for k,typ in bestimmung.items():
#		print( k,typ ) #d
		if typ == 'str':
			dic[k] = ''
		elif typ == 'int':
			dic[k] = 0
		elif typ == 'float':
			dic[k] = 0.0
	return dic
