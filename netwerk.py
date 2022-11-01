import os
import socket

mittel2 = 'http://www-proxy-ams.nl.oracle.com:80'
os.environ['http_proxy'] = mittel2
os.environ['https_proxy'] = mittel2

def lien():
	hostname = 'google.com'
	x = socket.getaddrinfo(hostname,'www')
	s = socket.socket(*x[0][0:3])
	s.settimeout(1)
	try:
		s.connect(x[0][4])
		print ( hostname, 'is up!' )
		return True
	except socket.timeout:
		print ( hostname, 'is down!' )
		return False

def proxx():
	if not lien():
		mittel = 'http://www-proxy-ams.nl.oracle.com:80'
		os.environ['http_proxy'] = mittel
		os.environ['https_proxy'] = mittel
		assert lien() == True
		print( 'Proxy gesetzt!' )
	return True

proxx()

"""
mittel2 = 'www-proxy-ams.nl.oracle.com:80'
os.environ['http_proxy'] = 'adc-proxy.oracle.com:80'
os.environ['https_proxy'] = 'adc-proxy.oracle.com:80'

s.connect(x[0][4])
"""
