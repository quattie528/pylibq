def p2f(x):
	x = x.replace('%','')
	if x == '-': return None
	x = float(x)
	x = x / 100
	return x
