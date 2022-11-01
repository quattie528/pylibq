import datetime

def us2kk4d(x):
#	x = dt.strptime(x, '%Y-%m-%d')
#	x = dt.strptime(x, '%dD %H:%M:%S')
#	x = datetime.datetime.strptime(x, '%/%/%Y%m%d')
	try:
		x = datetime.datetime.strptime(x, '%m/%d/%Y')
		return x
	except ValueError:
		return x

def us2kk4q(x):
	w = x.split('-')
	y = w[1] + w[0]
	return y

#

###################
### ZEITBEREICH ###
###################
def zeitbereich(aus,nach=0):
	eigen = datetime.date.today()
	x = eigen + datetime.timedelta(days=aus)
	if nach == 0:
		y = eigen
	else:
		y = eigen + datetime.timedelta(days=nach)
	return (x,y)
