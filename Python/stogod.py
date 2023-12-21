from random import shuffle

lista = ['','','1']

def shuffle_of_list(lista_parametar):
    shuffle(lista_parametar)
    return lista_parametar

def guessFunction():
    guess = ''

    while guess not in ['0','1','2']:
        guess = input("Izaberi broj 0, 1 ili 2:  ")
    return int(guess)

def check_guess():
    

shuffle_liste(lista)
guessFunction()