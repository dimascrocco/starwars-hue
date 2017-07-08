import time 
import sys

filme = open("starwars.txt")
frames = filme.readlines()

texto = ""
for f in frames:
    texto += f

frames = texto.split("[H")

print "frames", len(frames)


def show(frame):
    print frames[frame]

def clear():
    print(chr(27) + "[2J")

def delay():
    o = open("config.cfg")
    cfg = o.readlines()
    duration = float(cfg[0])
    time.sleep(duration)

def play():
    for f in frames:
        clear()
        print f
        try:
            delay()
        except:
            print "" 

def main():
    symbols = set()
    tf = {}
    for f in frames:
        for l in f:
            for c in l:
                symbols.add(c)
                if not tf.get(c):
                    tf[c] = 0
                tf[c] += 1
    del tf['\n']
    print "n simbolos:", len(symbols)
    print "simbolos:", "".join(sorted(symbols)).replace('\n', '')
    tf = sorted(tf.items(), key=lambda x: x[1], reverse=True)

    count = 0
    print "frequencia dos simbolos:"
    for k, v in tf:
        print count, ord(k), "->", k, v
        count += 1


    last = 0
    while True:
        n = raw_input("({0}) frame: ".format(last))
        try:
            value = int(n)
            show(value)
            last = value
        except:
            last += 1
            show(last)

if __name__ == "__main__":
    main()
