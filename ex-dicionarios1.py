num_favoritos = {'joão': '1', 'pedro': '7', 'maria': '2', 'paula': '10'}
print('Os números favoritos são:')
for num in num_favoritos:
    print(f'{num.title()}: {num_favoritos[num]}')

# identificar as chaves
for num in num_favoritos.keys():
    print(f'{num.title()}')

# para identificar os valores
for num in num_favoritos.values():
    print(f'{num.title()}')
