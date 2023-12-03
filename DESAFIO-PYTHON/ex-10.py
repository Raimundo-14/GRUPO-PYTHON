texto = str(input('Digite uma palavra:')).lower()
texto1 = texto[::-1]
if texto == texto1:
    print('Esta palavra e um polímdromo')
else:
    print('Esta palavra não é um polímdromo')

print(texto)
