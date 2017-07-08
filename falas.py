import re

    #letras = "[a-zA-Z]*"
letras = '\b([a-zA-Z]+)\b' #nope


o = open("starwars.txt")

linhas = o.readlines()

for l in linhas:
    resultado = re.findall(letras, l)
    if resultado > 0:
        print l
