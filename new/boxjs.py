import os
import subprocess

node='/usr/bin/node '
boxjs='/root/javascr/box-js/run.js '
decoder='/root/javascr/box-js/decoder.c '

def decode(s_name):
	try:
		proc = subprocess.Popen([decoder, s_name, s_name.replace("jse","js")],stdout=subprocess.PIPE)
		(out, err) = proc.communicate()
		return s_name.replace("jse","js")
	except: 
		raise NameError(err)

def boxjs(name):
	if name.endswith("jse"):
		file=decode(name)
	#

