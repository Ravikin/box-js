import subprocess
import json
import os

# GLOBALS
node="/usr/bin/node"
boxjs="/root/javascr/box-js/run.js"
decoder="/root/javascr/box-js/decoder"

# -- SLOWNIK FLAG
class F:
	d="--download"
	t10="--timeout=10"
	t20="--timeout=20"
	t30="--timeout=30"	
	t120="--timeout=120"
	t360="--timeout=360"
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


def __anal(input):
	substring = "timed out"
	n = 0
	global node, boxjs
	with open("jsanal.tmp","w") as f:
		f=input.read()
	s_file=getcwd()+"/jsanal.tmp"
	for timeout in [F.t10,F.t30,F.t60,F.t120,F.t360]:					# Proboj analizowac plik dla wskazanych timeoutow jezeli w out pojawi sie 'timed out'	
		if substring in out:								# Jezeli analiza zakonczyla sie timeoutem to powtorz
			flags=' '.join([timeout, F.nfe, F.d])					# Flagi z jakimi ma zostac uruchomiona analiza
			proc = subprocess.Popen([node, boxjs, s_file, flags], stdout=subprocess.PIPE]	# Analizujemy
			(out, err) = proc.communicate()						# Przypisujemy wyjscie z analizy do zmienych out oraz err
			with open('debug.log','w') as f:					# DEBUG
				f.write("OUTPUT:\r\n"out+err)	
			print "TIMEDOUT"							# DEBUG
			n += 1
			continue								# time out sie pojawil wiec wracamy do for'a
		else:
			print "WYNIK POZYTYWNY"							# DEBUG
			break									# timeoutu nie ma wiec lecim dalej 
	if substring in out:									# W przypadku gdy petla [:46]for zakonczyla sie z wynikiem negatywnym (tzn gdy doszlo do timeoutu) to wypisujemy ta informacje
		print "Analiza nieudana - time out"						# DEBUG
		raise NameError("TIMED OUT")
	os.remove(s_file)									# Sprzątamy

def __send_output():
	

def __danal(input):


