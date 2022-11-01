import xz

def code2pref():
	dic = xz.txt2dic('__/pref_jp.tsv')
	return dic

def pref2code():
	dic = xz.txt2dic('__/pref_jp.tsv')
	dic = { w:k for k,w in dic.items() }
	return dic
