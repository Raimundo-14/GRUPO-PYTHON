carros = ['audi', 'bmw', 'subaru', 'toyota', 'ford', 'renault']
for carro in carros:
    if carro == 'bmw':
        print(carro.upper())
        if carro == 'subaru':
            print(carro.lower())
            if carro == 'toyota':
                print(carro.upper())
    else:
        print(carro.title())
