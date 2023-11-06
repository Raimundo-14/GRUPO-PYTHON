# Estágio da vida

info_idade = int(input('Qual a sua idade? '))

if info_idade >= 0 and info_idade <= 2:
    print('Você é bebê')
elif info_idade >= 3 and info_idade <= 4:
    print('Você é uma criança pequena')
elif info_idade >= 5 and info_idade <= 13:
    print('Você é um(a) garoto(a)')
elif info_idade >= 14 and info_idade <= 20:
    print('Você é um adolescente')
elif info_idade <= 64:
    print('Você é adulto')
else:
    print('Você e um idoso(a)')
