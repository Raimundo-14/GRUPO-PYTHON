nome = input('Qual o seu nome? ')
idade = int(input('Qual a sua idade? '))
if idade <= 17:
    print('Olá, {}! Você tem {} anos, portanto não pode dirigir'.format(nome, idade))
else:
    print('Olá, {}! Você tem {} é poderá dirigi!'.format(nome, idade))
    print('Digira com responsabilidade, {}!'.format(nome))
