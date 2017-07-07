import time 
import sys

filme = open("starwars.txt")

frames = filme.readlines()

texto = ""
for f in frames:
    texto += f

frames = texto.split("[H")

def clear():
    print(chr(27) + "[2J")

def delay():
    o = open("config.cfg")
    cfg = o.readlines()
    duration = float(cfg[0])
    time.sleep(duration)

for f in frames:
    clear()
    print f
    try:
        delay()
    except:
        print "" 
