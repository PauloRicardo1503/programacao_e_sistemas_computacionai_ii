# O programa pensa num numero de n digitos e o usuario deve adivinhar esse numero em 10 tentativas
import random

NUM_DIGITS = 4
NUM_MAX_TENTATIVAS = 10

def main():
    num_tentativas = 1
    numero_aleatorio = pensa_numero_aleatorio() 
    print(numero_aleatorio)

    while num_tentativas < NUM_MAX_TENTATIVAS:

        numero_usuario = (str(input('Digite um numero com {} digitos!: '.format (NUM_DIGITS))))


        if verifica_numero(numero_aleatorio, numero_usuario):
            print("Voce acertou!")
            break
        else:
            print("Voce errou!")
            num_tentativas += 1            


def verifica_numero(numero_aleatorio, numero_usuario):

    if numero_usuario == numero_aleatorio:
        return True
    else:
        return False
    
def pensa_numero_aleatorio():

    possiveis_numeros = list('0123456789')
    random.shuffle(possiveis_numeros) #shuffle embaralha
    lista_numeros = possiveis_numeros[0:NUM_DIGITS]

    numero_aleatorio = ''

    for numero in lista_numeros:
        numero_aleatorio += str(numero)
    
    return numero_aleatorio

if __name__ == '__main__':
    main()