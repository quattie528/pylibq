from datetime import date as dy # ein Alphabet ist gefehr
from datetime import time as tm # ein Alphabet ist gefehr
from datetime import datetime as dt
from datetime import timedelta as dl
from datetime import timezone as tz
import dateutil.parser

"""
2020-04-08 08:47:59
BENCHMARK on datetime.timezone and pytz
https://qiita.com/mattsu6/items/5511c5631e7a54550f7f
"""

#

###########################
### TIMEZONE CONVERSION ###
###########################
def tzconv(zt,des='JST',aux='UTC'):
	if aux == 'JST':
		x = zt.astimezone(tz(dl(hours=+9)))
	return x

def jst2utc(zt):
	x = zt.astimezone(tz.utc)
	return x

def utc2jst(zt):
#	x = zt.replace(tzinfo=dateutil.tz.tzlocal())
	x = zt.astimezone(tz.utc)
#	print( x.tzinfo ) #d
	x = x.astimezone(tz(dl(hours=+9)))
	return x

#

################
### ISO-8601 ###
################
#https://en.wikipedia.org/wiki/ISO_8601
#2021-12-30T00:00:00.000000Z
def d2iso8601(x):
	x = str(x) + 'T00:00:00.000000Z'
	return x

def p2iso8601(x):
	x = str(x)
	x = x.replace(' ','T')
	x = x + '.000000Z'
	return x
