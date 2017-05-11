# 04-2017 Mateusz Piorkowski (c) - Worker JS
# v0.5 11-05-2017 15:21
# /==README==\
# step 0 - przygotowanie srodowiska (wlasny folder)
# step 1 - dekodowanie pliku jse (o ile taki zostal podany)
# step 2 - wlasciwa analiza
# step 3 - czyscimy po sobie (do ustalenia czy usuwamy foldery czy nie | oraz w zaleznosci od tego jak zostanie przekazany plik do analizy to usuwamy tmp)
# step 4 - wysylamy wynik analiz na stdout -> !!!JAKO JSON!!!
# \==README==/
from random import randint
import subprocess
import json
import os,shutil
import datetime

# -- TRASH
now=datetime.datetime.now()

# -- GLOBAL
node="/usr/bin/node"
boxjs="/root/javascr/box-js/run.js"
decoder="/root/javascr/box-js/decoder"
ID_NR=str(now.day)+'_'+str(now.month)+'_'+str(randint(1000,9999))				# nazwa folderu roboczego skladajaca sie z dnia miesiaca + numeru miesiaca + randomowego 4 znakowego inta
n = 0												# zmienna sluzaca do zliczenia wywolan fora z analizy

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


# -- FUNKCJA DEKODUJACA
def __decode(s_name):										# step 1
	global  decoder 									# Pobiera lokalizacje (sciezke) decodera ze zmiennej globalnej
	try:
		o_name = "/d_jsanal.tmp"									# Tworzy nazwe pliku wyjsciowego -> o_name (podmienia tylko .jse na .js)
		proc = subprocess.Popen([decoder, s_name, o_name], stdout = subprocess.PIPE)	# Dekompiluje wskazany plik  
		(out, err) = proc.communicate()							# Zarzadza wyjsciami [domyslnie program nic nie wypisuje]
		print out									# DEBUG
		print err									# DEBUG
		return os.getcwd()+o_name							# Zwrocenie sciezki pliku wynikowego
	except:
		raise NameError("ERROR:"+str(_))						# Jezeli cos sie nie udalo to zwraca blad i wynik dzialania ostatniego polecenia -> _ (podkreslenie to zmienna zawierajaca wynik dzialania ostatniego polecenia)
		

# -- FUNKCJA ANALIZUJACA
def __anal(s_name):										# step 2 (funkcja nic nie zwraca bo wynik analizy jest w plikach)
	substring = "timed out"									# Definicja stringa szukanego w wyjsciu subprocesu dla -> box-js/run.js
	out="timed out"										# Dodany po to zeby for wykonal sie przynajmniej raz (ze wzgledu na ifa w srodku)
	global node, boxjs, n									# Pobiera lokalizacje (sciezki) dla nodejs oraz sandboxa box-js
	for timeout in [F.t10,F.t30,F.t60,F.t120,F.t360]:					# Proboj analizowac plik dla wskazanych timeoutow jezeli w out pojawi sie 'timed out'	
		if substring in out:								# Jezeli analiza zakonczyla sie timeoutem to powtorz
			flags=' '.join([timeout, F.nfe, F.d])					# Flagi z jakimi ma zostac uruchomiona analiza
			proc = subprocess.Popen([node, boxjs, s_name, flags], stdout=subprocess.PIPE]	# Analizujemy
			(out, err) = proc.communicate()						# Przypisujemy wyjscie z analizy do zmienych out oraz err
			with open('debug.log','w') as f:					# DEBUG
				f.write("OUTPUT:\r\n"out+err)					# DEBUG
			print "TIMEDOUT"							# DEBUG
			n += 1
			continue								# time out sie pojawil wiec wracamy do for'a
		else:
			print "WYNIK POZYTYWNY"							# DEBUG
			break									# timeoutu nie ma wiec lecim dalej 
	if substring in out:									# W przypadku gdy petla [:65]for zakonczyla sie z wynikiem negatywnym (tzn gdy doszlo do timeoutu) to wypisujemy ta informacje
		print "Analiza nieudana - time out"						# DEBUG
		raise NameError("Analysis TIMED OUT")
		

# -- FUNKCJA ZWRACAJACA WYNIK ANALIZY
def __send(plik):										# step 3
	# funkcja ma zwracac wynik w postaci slownika
	output = {}										# tworzymy pusty slownik #TODO #TMP
	try: 
		if n == 1:									# sprawdzamy czy analiza powiodla sie od razu czy za 'n razem
			os.chdir(basename(plik)+'.results')					# wchodzimy do folderu z wynikami
			with open("urls.json") as f:
				output = json.load(f)
		elif n > 1:
			os.chdir(basename(plik)+"."+n+'.results')				# wchodzimy do najaktualniejszego folderu z wynikami
			if os.path.exists("urls.json"):
				with open("urls.json") as f:
					output = json.load(f)
					print json.dumps(output, indent=4, separators=(',',':'))
			elif os.path.exists("active_urls.json"):
				with open("active_urls.json") as f:
					output = json.load(f)
					print json.dumps(output, indent=4, separators=(',',':'))
	except:	
		raise NameError("cos poszlo nie tak przy przesylaniu wynikow!\r\n ERROR:"+_)


# -- FUNKCJA PRZYGOTOWAWCZA
def __init(plik):											# step 0
	global ID_NR										# importujemy globalna nazwe folderu roboczego 
	try:
		if not os.path.exists(ID_NR):							# jezeli folder nie istnieje 
			error="Tworze folder \'"+ID_NR+"\'"					# DEBUG
			os.makedirs(ID_NR)							# to tworzymy nowy - nie zakladam kolizji
		error="Zmieniam folder na \'"+ID_NR+"\'"					# DEBUG
		os.chdir(ID_NR)									# wchodzimy do nowo utworzonego folderu
		with open ("jsanal.tmp",'w') as file:						# Otwieramy tymczasowy plik (zapisujemy podany obiekt do pliku)
			file = plik.read()							# zapisujemy podany obiekt w celu dalszej analizy (box-js pracuje na pliku)
		return os.getcwd()+"/jsanal.tmp"
	except:
		raise NameError("__init() zawiodl przy: "+error)				# DEBUG


def __cleanup():										# step 4
	# usuwamy pliki tmp oraz ewentualnie workdir
	os.chdir('..')										# Wychodzimy z folderu roboczego
	shutil.rmtree(ID_NR, ignore_errors=True)						# Usuwamy folder roboczy wraz z zawartoscia
	print "Cleanup DONE"									# DEBUG

def main(plik, mode):											# ewentualnie zmienic na def run(plik): tak zeby bylo ladnie
# step 0
	plik = __init(plik)
# step 1
	if mode == 'd':								# TODO - aplikacja nadrzedna decyduje co robic
		plik = __decode(plik)
	else:
		pass
# step 2
	__anal(plik)
# step 3 
	__send(plik)
# step 4
	__cleanup()
