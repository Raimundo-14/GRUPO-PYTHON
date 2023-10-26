carros = ['fiat', 'ford', 'chevrolet']
carros.append('dodger')
carros.insert(4, 'volks')
ultimo_carros = carros.pop(2)
print('O ultimo carro a ser vendido foi um:' +
      ' ' + ultimo_carros.title() + '.')
print('O nome do carro é:' + ' ' + carros[1].title())
print('Nosso primeiro carro foi um:' + ' ' + carros[0].title())
