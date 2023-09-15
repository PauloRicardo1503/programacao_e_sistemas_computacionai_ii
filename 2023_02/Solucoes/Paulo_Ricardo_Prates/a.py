class Veiculo:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

estoque = []

def main():
    print("Seja bem-vindo à MotorMania, somos uma revenda de veículos totalmente online.")
    while True:
        print("1 - Verificar estoque.")
        print("2 - Registrar veículo.")
        print("3 - Sair.")
        opcao = input("Digite o número da opção desejada: ")
        if opcao == "1":
            verificar_estoque()
        elif opcao == "2":
            registrar_veiculo()
        elif opcao == "3":
            break
        else:
            print("Opção inválida. Tente novamente.")

def registrar_veiculo():
    nome = input("Digite o nome do veículo: ")
    preco = input("Digite o valor do veículo: ")
    veiculo = Veiculo(nome, preco)
    estoque.append(veiculo)
    print(f"{nome} foi adicionado ao estoque")

def verificar_estoque():
    if not estoque:
        print("Não há veículos no estoque.")
    else:
        print("Aqui está a lista de modelos de carros disponíveis:")
        for index, veiculo in enumerate(estoque, start=1):
            print(f"{index} - {veiculo.nome} por apenas R${veiculo.preco}")

if __name__ == '__main__':
    main()
