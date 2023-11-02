# numeros = []
# for cubo in range(1, 11):
#    numero = cubo**3
#   numeros.append(numero)
#   print(numeros)
#
'''
numeros = []
for cubo in range(1, 11):
    numeros.append(cubo**3)
    print(numeros)'''

numeros = [cubo**3 for cubo in range(1, 11)]
print(numeros)

quadrado = [num**2 for num in range(1, 11)]
print(quadrado)
