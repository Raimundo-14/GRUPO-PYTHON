frutas = ['maça', 'banana', 'cajú', 'laranja']
q_frutas = input('Qual sua frta favorita? ')
if q_frutas in frutas:
    if q_frutas == 'maça':
        print('Humm, otima escolha, {}'.format(q_frutas))
    elif q_frutas == 'banana':
        print('{} é otima para evitar câimbras'.format(q_frutas.title()))
    elif q_frutas == 'cajú':
        print('{} é uma fruta deliciosa, tipica do nordeste!'.format(q_frutas.title()))
    elif q_frutas == 'laranja':
        print('{} é uma fruta rica em vitamina C'.format(q_frutas.title()))
    else:
        print('Também é uma otima fruta!!')
