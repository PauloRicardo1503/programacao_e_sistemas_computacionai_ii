# importar as bibliotecas
import math
# definição de uma funçao main
def main():
    # o programa fica aqui

    peso = float(input('Dgite o seu peso: '))
    altura = float(input('Digite a sua altura: '))
    
    imc = calcula_imc(peso,altura)

    print(imc)
# verificador pra rodar o programa
def calcula_imc(peso,altura):
    imc = (peso / pow(altura,  2)) 
    return imc
    
    
    

if __name__ == '__main__':
    main()