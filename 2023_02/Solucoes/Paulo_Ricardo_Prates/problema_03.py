def par_ou_impar(numero):

    if(numero % 2 == 0):
        print ('O numero é par. ')
    else:
        print ('O numero é impar. ')

numero = int(input('Digite um valor: '))
par_ou_impar(numero)