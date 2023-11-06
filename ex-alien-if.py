alien_colors = ['verde', 'amarelo', 'vermelho']
jogo = input('Qual cor você escolhe: verde, amarelo ou vermelho? ')
if jogo in alien_colors:
    if jogo == 'verde':
        print('você ganhou 5 pontos!')
    elif jogo == 'amarelo':
        print('Você ganhou 10 pontos')
    elif jogo == 'vermelho':
        print('Você ganhou 20 pontos')
    else:
        print('Você perdeu o jogo!')
