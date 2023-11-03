minhas_pizzas = ['frango', 'queijo', 'doce']
sua_pizza = minhas_pizzas[:]
minhas_pizzas.append('peperoni')
sua_pizza.append('4 queijos')
print('Minha lista de pizzas favoritas são estas:')
for minhas_pizza in minhas_pizzas[:]:

    print(minhas_pizza.title())
print(minhas_pizzas)
print(sua_pizza)
