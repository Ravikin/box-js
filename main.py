# SPIS FUNKCJI:
# run_analysis() 	- podaje do box-js wskazany plik (pierwszy argument) oraz flagi (kazdy nastepny argument) do analizy
# send_output()		- po analizie printuje pliki urls.json oraz active_urls.json
# find_res()		- szuka tylko folderu wynikowego - NIE UZYWANA
# check_state()		- sprawdza czy nie potrzeba helpa (sprawdza argumenty)
# HELP()		- wypisuje wiadomosc pomocy
# make_env()		- przygotowuje sobie srodowisko pracy
# main()		- main to main :)

import sys
import os
import os.path
import time
import glob
import contextlib
import io

#--- Glowna funkcja programu
def run_analysis():
	ARGS=len(sys.argv) 					# Zaczytuje ilosc argumentow jako liczbe
	command = 'node /root/javascr/box-js/run.js ' 
	for i in range(ARGS):  					# petla dodaje do stringa command wszystkie argumenty
		if i>0:						# jezeli numer argumentu wiekszy od 1 (czyli od nazwy uruchamianego pliku)
			command+=sys.argv[i] + ' '		# to dodajemy go do konca stringa z komenda
			print sys.argv[i]				# DEBUG
	print command  							# DEBUG
	os.system(command)					 # uruchamia run.js z dodanymi argumentami

#--- Funkcja czyta i wysyla plik wynikowy z URLami na stdout
def send_output():
	if os.path.exists(glob.glob(sys.argv[1]+'*.results')):	# sprawdza czy folder wynikowy istnieje !!! MUSI BYC TYLKO JEDEN FOLDER WYNIKOWY
		RES_DIR=glob.glob(sys.argv[1]+'*.results') 	# jezeli folder istnial to zapisuje jego lokalizacje
		FILES=os.walk(RES_DIR)				# od tak tylko sprawdza pliki w folerze wynikowym
		URLS=RES_DIR+'/'+'urls.json'			# wskazuje na plik urls.json
		AURLS=RES_DIR+'/'+'active_urls.json'		# wskazuje na plik active_urls.json
		if os.path.exists(URLS):			# jezeli plik urls.json istnieje
			with open(URLS) as f:			# to go otwiera
				data = json.load(f)		# laduje jako json
				print json.dumps(data, indent=4, separators=(',',':'))	# wypisuje z wcieciem i przecinkiem miedzy rekordami
		if os.path.exists(AURLS):			# jezeli plik active_urls.json istnieje
			with open(AURLS) as fi:			# to go otwiera
				data2 = json.load(fi)		# laduje jako json
				print json.dumps(data2, indent=4, separators=(',',':')) 	# wypisuje z wcieciem i przecinkiem miedzy rekordami
	else:							# jezeli folder wynikowy nie istnial
		raise NameError("Brak folderu wynikowego")	# to zwraca exception

#--- Find results - znajduje folder z wynikami i poki co tyle...
def find_res():
	CWD=os.getcwd()
	RES=glob.glob('*.results')
	RES_PATH=cwd + '/' + RES
	os.chdir(RES_PATH)

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

def HELP():
	print "TO JEST HELP"
	os.system("node /root/javascr/box-js/run.js -h")

#--- Przygotowanie srodowiska pracy, utowrzenie folderow etc.
#def make_env():

#---MAIN---#
def main():
	check_state()

	f = io.StringIO()
	with redirect_stdout(f):
		run_analysis()

	send_output()

##### KONIEC DEFINICJI FUNKCJI #####

#--- RAW ---#
try:
	main()

except KeyboardInterrupt:
	print "Przerwanie dzialania!"

finally:
	print "\n\nTutaj cleanup"
	sys.exit()
