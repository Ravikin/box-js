# SPIS FUNKCJI:
# run_analysis() 	- podaje do box-js wskazany plik (pierwszy argument) oraz flagi (kazdy nastepny argument) do analizy
# send_output()		- po analizie printuje pliki urls.json oraz active_urls.json
# find_res()		- szuka tylko folderu wynikowego - NIE UZYWANA
# check_state()		- sprawdza czy nie potrzeba helpa (sprawdza argumenty)
# HELP()		- wypisuje wiadomosc pomocy
# make_env()		- przygotowuje sobie srodowisko pracy
# main()		- main to main :)

import sys, os, os.path, time, io
import glob
import json

#--- Zbior flag dla box-js uzywanych w trakcie analizy
class F:
	download="--download"
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

#--- [OLD] v1 Glowna funkcja programu
def run_analysis():
	ARGS=len(sys.argv) 					# Zaczytuje ilosc argumentow jako liczbe
	command = 'node /root/javascr/box-js/run.js ' 
	for arg in sys.argv[1:]:  				# petla dodaje do stringa command wszystkie argumenty
		command+=arg + ' '				# to dodajemy go do konca stringa z komenda
		print arg						# DEBUG
	print command  							# DEBUG
	os.system(command)					 # uruchamia run.js z dodanymi argumentami
	
#--- [NEW] v2 Glowna funkcja programu
def analysis(name, *flags):
	command = 'node /root/javascr/box-js/run.js ' + name + ' ' 
	for flag in flags:  					# petla dodaje do stringa command wszystkie argumenty
		command+=flag + ' '				# to dodajemy go do konca stringa z komenda
		print flag						# DEBUG
	print command  							# DEBUG
	os.system(command)					 # uruchamia run.js z dodanymi argumentami



#--- Funkcja czyta i wysyla plik wynikowy z URLami na stdout
def send_output(name):
	RES_DIR=glob.glob(name+'.results') 			# jezeli folder istnial to zapisuje jego lokalizacje
	RES_DIR=''.join(RES_DIR)
	print RES_DIR						# DEBUG
	if os.path.exists(RES_DIR):				# sprawdza czy folder wynikowy istnieje !!! MUSI BYC TYLKO JEDEN FOLDER WYNIKOWY
		FILES=os.walk(RES_DIR)				# od tak tylko sprawdza pliki w folerze wynikowym
		URLS=RES_DIR[0]+'/'+'urls.json'			# wskazuje na plik urls.json
		AURLS=RES_DIR[0]+'/'+'active_urls.json'		# wskazuje na plik active_urls.json
		if os.path.exists(str(URLS)):			# jezeli plik urls.json istnieje
			with open(str(URLS)) as f:			# to go otwiera
				data = json.load(f)		# laduje jako json
				print json.dumps(data, indent=4, separators=(',',':'))	# wypisuje z wcieciem i przecinkiem miedzy rekordami
		if os.path.exists(str(AURLS)):			# jezeli plik active_urls.json istnieje
			with open(str(AURLS)) as fi:			# to go otwiera
				data2 = json.load(fi)		# laduje jako json
				print json.dumps(data2, indent=4, separators=(',',':')) 	# wypisuje z wcieciem i przecinkiem miedzy rekordami
	else:							# jezeli folder wynikowy nie istnial
		raise NameError("Brak folderu wynikowego")	# to zwraca exception

#--- Find results - znajduje folder z wynikami i poki co tyle...
def find_res(name):
	CWD=os.getcwd()
	RES=glob.glob(name+'.results')
	print RES						# DEBUG
	RES_PATH=cwd + '/' + RES
	print os.getcwd()					# DEBUG
	os.chdir(RES_PATH)
	print os.getcwd()					# DEBUG

#--- Zwykly help
def check_state():
	for args in sys.argv:					# jezeli wsrod podanych argumentow jest ktorys z ifa to wywoluje HELP() i konczy
		if args=='-h':
			HELP()
			sys.exit()
		elif args=='--help':
			HELP()
			sys.exit()
		elif args=='/?':
			HELP()
			sys.exit()
		elif args=='-?':
			HELP()
			sys.exit()
		elif args=='-A':
		

def HELP():
	print "TO JEST HELP"
	os.system("node /root/javascr/box-js/run.js -h")

#--- Przygotowanie srodowiska pracy, utowrzenie folderow etc.
#def make_env():

#--- CLEANUP
def cleanup():
	time.sleep(1)

#---MAIN---#
def main():
	check_state()
	
	run_analysis()

	send_output()

##### KONIEC DEFINICJI FUNKCJI #####

#--- RAW ---#
try:
	main()
except KeyboardInterrupt:
	print "Przerwanie dzialania!"
finally:
	cleanup()
	sys.exit()
