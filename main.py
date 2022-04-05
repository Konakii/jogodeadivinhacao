import random
while True:
    var = input('Eu estou pensando em um numero! Tente adivinhar qual numero eu estou pensando: ')
    var = int(var)
    numero = random.randint(0,99)
    if var > numero:
            print('muito alto! tente novamente')
            print()
    elif var < numero:
            print('muito baixo! tente novamente')
            print()
    elif var == numero:
            print('É esse!')
            print()
            v = input('Gostaria de jogar novamente?(s/n): ')
            if v == 's':
                pass
            else:
                print('Obrigado por jogar, até breve!')
                break  
