#!/usr/bin/python

### MODULS ###
from .xtbase   import *
from .xtplus   import *
from .intmonth import * # n
from .finplus  import * # q
from .gengou   import *
from .weltzeit import *
from .augenblick import *
#
from .op4pctg import * # 2021-01-03
from .kkbase  import * # 2021-10-16

#

#############################
### ERKLÄRUNG IN ENGLISCH ###
#############################
"""
[ERKLÄRUNG]
Hier, ich nutze Englisch für Symbols als {d:date, t.time, y:year}

[ACHTUNG!!!]
Verwenden niemals meine eigenen externen Module

[NOTIZ @ 2020-03-08]
I excluded date operation related to financials
Especially quarter operation is very critical and special

[BESTIMMUNG]
obj
	timedelta
	tzinfo
	time
	date
		datetime

[ABBREVIATION]
s : string
i : integer
f : float
d : date
t : time
p : datetime
r : datetime with millisecond
z : any
-
u : unixtime
x : exceltime
-
y : year
m : month
d : day
h : hour
m : minute
s : second
-
a : weekday (Mon-Sun)
b : month in language (Jan-Dec)
- MY DEFINITION
q : quarter
n : month in 6 digits (ex. 198005, 201610)
e : date in 4 digits (ex. 0122, 1107, 0528)
k : delta
w : week
----------
g  : gengou (明治|大正|昭和|平成)
sc : string in dot -> 1980.05.28
sh : string in hyphen -> 1980-05-28
sl : string in slash -> 1980/05/28
sj : string in Japanese Gengou ->
sg : string in Japanese alphabetical Gengou -> S55.5.28
sf : string in full mode -> 1980-05-27 23:57:33
"""
