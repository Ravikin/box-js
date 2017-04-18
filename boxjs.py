# Wrapper for box js
import os

#--- Zbior flag dla box-js uzywanych w trakcie analizy
class F:
	d="--download"
	t20="--timeout=20"
	t30="--timeout=30"
	t120="--timeout=120"
	nfe="--no-file-exists"
	ncr="--no-catch-rewrite"
	nccr="--no-cc_on-rewrite"
	ncs="--no-concat-simplify"
	ne="--no-echo"
	ner="--no-eval-rewrite"
	nr="--no-rewrite"
	nse="--no-shell-error"
	ntr="--no-typeof-rewrite"
	xp="--windows-xp"
	exp="--experimental-neq"


def anal(name, mode):
	node='node' 				# sciezka do nodejs
	boxjs='run.js'				# sciezka do box-js
	if mode == '-h':
		HELP()
		sys.exit()
	elif mode == '-U':				# U - Uniwersalny
		analysis(name,F.t30,F.nfe)
	elif mode == '-D':				# D - Download
		analysis(name,F.t30,F.nfe,F.d)
	elif mode == '-oD':				# oD - Only Download
		analysis(name,F.d)
	elif mode == '-LD':				# LD - Long Download
		flags=' '.join([F.t120,F.d])		# Laczymy flagi dla boxa w jeden string
		print flags				# DEBUG
		command=' '.join([node, boxjs, name, flags])	# Laczymy cala komenda w jeden string dzielony spacjami
		print command				# DEBUG
		#run(command)				# odpalamy analize


def run(command):
	os.system(command)	


#def HELP():
