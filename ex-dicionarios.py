pessoas = {'nome': 'raimundo', 'sobrenome': 'albuquerque',
           'idade': '42', 'cidade': 'joão pessoa'}
nome = pessoas['nome']
sobrenome = pessoas['sobrenome']
cidade = pessoas['cidade']
idade = pessoas['idade']
for pessoa in pessoas:
    print(f'{pessoa.title()}: {pessoas[pessoa].title()}')
    print(f'O nome do aluno é: {pessoas[pessoa]}')
print(pessoas['nome'].title(), pessoas['sobrenome'].title(),
      pessoas['cidade'].title(), pessoas['idade'])
print(pessoas['nome'], pessoas['sobrenome'])
print(f'O nome do aluno e: {nome}')
print(f'O nome do aluno e: {nome.title()}')
print(
    f'O aluno {nome.title()} {sobrenome.title()}, natural de {pessoas[pessoa].title()} com {idade} anos de idade, foi aprovado no curso!!')
