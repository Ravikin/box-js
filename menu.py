import boxjs

name=raw_input("Podaj sciezke pliku do analizy: ")
flags=raw_input("Podaj argumenty dla analizy: ")
#flags=flags.split()
#flags=', '.join(flags)

boxjs.anal(str(name),str(flags))
