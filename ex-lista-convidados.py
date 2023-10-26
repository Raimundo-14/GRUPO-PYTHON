lista_convidados = ['Raimundo', 'Talitha',
                    'pedrinho', 'paola', 'fenelon', 'danilo']

lista_convidados.append('robson')
lista_convidados.insert(4, 'jorge')
lista_convidados.insert(5, 'fred')
del lista_convidados[6]
length = len(lista_convidados)
print(length)
print('Olá, seja bem vindo,' + ' ' + lista_convidados[0].title())
print('Que bom vê você aqui,' + ' ' + lista_convidados[1].title())
print(lista_convidados[2].title(
) + ' e ' + lista_convidados[3].title() + ' '+'podem brincar a vontade no parquinho!')
print('infelizmente ' +
      lista_convidados[5].title() + ' ' 'não poderá comparecer ao evento hoje,' + ' ' + lista_convidados[6].title() + ' ' + 'terá que substitui-lo')
