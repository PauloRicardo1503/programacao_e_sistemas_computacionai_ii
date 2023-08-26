import random
NUM_DIGITS = 3
MAX_GUESSES = 10
NUM = 145 #Exemplo mais simples
def main():
    print('''
            Numero Secreto é um jogo de adivinhação:
            
            Estou pensando em um numero com () digitos com numero não repetidos.
            tente adivinhar qual é o numero. Aqui vão algumas dicas:
            Quando eu digito  Isso significa:
            Pico              Um digito esta mas na posição errada
            Fermi             Um digito esta correto e na posição correta
            Bagels            Nenhum digito esta correto
            
            Por exemplo, se o numero secreto for 248 e seu chute fot 843, a dica será 
                    Fermi Pico.'''.format(NUM_DIGITS))
    
    controle_de_execucao = 0

    while True:
        numero_do_usuario = str(input('Digite um numero com 3 digitos:'))

        controle_de_execucao != 1

        if verifica_numero_valido(numero_do_usuario):
            verifica_igualdade(numero_do_usuario)

        if controle_de_execucao > MAX_GUESSES:
            break

    # Como verificar as posições dos numero do usuario com o numero pra adivinhar.
    


def verifica_numero_valido(numero):
        if len(numero) == 3:
            return True
            
        else:
            return False

def verifica_igualdade(numero):
        if numero == NUM:
            print('voce ACERTOU.')
        else:
            print('voce errou.')


if __name__ == '__main__':
         main()