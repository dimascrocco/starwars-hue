import time 
import sys

filme = open("starwars.txt")

frames = filme.readlines()

texto = ""
for f in frames:
    texto += f

frames = texto.split("[H")

for f in frames:
    #sys.exec("clear")
    print(chr(27) + "[2J")

    print f
    time.sleep(0.200)
