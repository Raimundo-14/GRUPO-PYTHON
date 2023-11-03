carros = ['corsa', 'S10', 'duster 1.6', 'amarok',
          'saveiro', 'forcus', 'duster 2.0 4x4']
print('Esse foram todos os carros que já possuí')
for carro in carros[0:]:
    print(carro.title())
print('Meus primeiros carros foram estes:')
for carro in carros[0:3]:
    print(carro.title())

print('Meus são meu ultimos carros: ')

for carro in carros[-3:]:
    print(carro.title())
