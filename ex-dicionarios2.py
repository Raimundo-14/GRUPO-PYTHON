glossarios = {'algoritmo': 'é basicamente um conjunto de passos para certa tarefa.',
              'linguagem': 'conjunto de definições (sintáticas e semânticas) usadas para fazer um texto que o computador é capaz de entender, ou seja, um programa de computador.',
              'código': 'conjunto de palavras ou símbolos contendo instruções para o computador.',
              'código Fonte': 'código de um programa. O computador o usa para gerar uma versão do programa que é capaz de processar.',
              'código de Máquina': 'código que a máquina consegue entender e executar.'}

for glossario in glossarios:
    print(f'{glossario.title()}: \n {glossarios[glossario]}')

# for glossario in glossarios.values():
    # print(f'{glossario.title()}')
