### MODUL ###
import os
import tempfile
import yaml

### ERKLÄRUNG ###
labomi    = ''
mychrome  = ''
myfirefox = ''

### TEMPFILE ###
labomi = ''
if os.name == 'posix':
	labomi = '/tmp/labomi/'
elif os.name == 'nt':
	labomi = tempfile.gettempdir() + '/labomi/'
	labomi = labomi.replace('\\','/')
os.makedirs(labomi,exist_ok=True)

### LOG ###
import logging
logging.basicConfig(
	level=logging.DEBUG,
	format='%(asctime)s - %(levelname)s - %(message)s',
#	filename=labomi+'a.txt'
)

### BROWSER ###
geh = True
browserdata = labomi + 'browser.yml'
if os.path.exists(browserdata):
#	print( browserdata ) #d
	with open(browserdata) as fh:
		dic = yaml.load(fh,Loader=yaml.FullLoader)
		mychrome  = dic.get('chrome','')
		myfirefox = dic.get('firefox','')
		geh = False
	if not os.path.exists(mychrome):  geh = True
	if not os.path.exists(myfirefox): geh = True
#
if os.name == 'posix':
	geh = False
	mychrome  = ''
	myfirefox = ''
if geh == True:
	pfad1 = 'C:/Program Files/'
	pfad2 = 'C:/Program Files (x86)'
	dic = {}

	for pfad in [pfad1,pfad2]:
		db = os.walk(pfad)
		res = []
		for tp in db:
			eigen = tp[0] + '/'
			dateien = tp[2]
			for x in dateien:
				y = eigen+x
				if y.endswith('chrome.exe'):
					y = y.replace('\\','/')
					dic['chrome'] = y
					mychrome = y
				elif y.endswith('firefox.exe'):
					y = y.replace('\\','/')
					dic['firefox'] = y
					myfirefox = y
	#
	with open(browserdata,'w') as fh:
		yaml.dump(dic,fh)
	del dic
	del pfad1
	del pfad2

del geh
del browserdata
