ler = open('Doc.txt', 'r').read()
ler1 = ler.split()

texto = []
for l in ler1:
    texto.append(ler1.count(l))

print("String\n" + ler + "\n")
print("Lista\n" + str(ler1) + "\n")
print("Frequências\n" + str(texto) + "\n")
print("Pares\n" + str(list(zip(ler1, texto))))
