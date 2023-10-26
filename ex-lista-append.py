carros = ['uno', 'ford']
# append -> inserir um item na lista na ultima posição
carros.append('honda')
carros.append('dodger')
# insert -> inserir um item na lista na posição desejada
carros.insert(2, 'suzuki')
# del -> deletar um item da lista
del carros[1]

print(carros[0].title())
print(carros[1].title())
print(carros[2].title())
print(carros[3].title())
# print(carros[4].title())
