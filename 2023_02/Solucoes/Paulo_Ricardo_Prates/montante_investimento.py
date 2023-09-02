def main():
    capital = float(input("Digite o valor a ser investido: "))
    taxa = float(input("Digite a taxa de juros por periodo %: "))
    periodos = int(input("Digite a quantidade de periodos investido: "))

    montante = calcula_montante(capital, taxa, periodos)

    print('O valor final do investimento depois de {} periodos é: {}'.format(periodos, round(montante, 2)))


    print('O valor do seu rendimento é: {}' .format(montante - capital))

    
def calcula_montante(c, t, n):
    # Montante = capital_investido * (1 + taxa_juros/100) ** periodo
    montante = c * (1 + t/100) ** n

    return montante


if __name__ == '__main__':
    main() 