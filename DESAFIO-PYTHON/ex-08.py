ler = open('Doc.txt', 'r')
ler1 = ler.read().split()
print(ler.read())
print(ler1)

texto = []
for l in ler1:
    texto.append(ler1.count(l))
# texto = [ler1.count(l) for l in ler1]
# print('\n' + texto + '\n')
print('\n' + str(ler1) + '\n')
print('\n' + str(texto) + '\n')
print('\n' + str(list(zip(ler1, texto))) + '\n')
