'''
Avaliacao : 1 bimestre - Programacao 2 
Professor: Pedro Lealdino Filho, PhD.
Turma: A

Integrantes do Grupo: 
-Paulo Ricardo Prates   
-Pedro Henrique Thomen
-Luis Henryque Novakoski
-
-

Instruções:

0. Faca uma cópia desse arquivo para que você desenvolva sua solução
1. Após terminar, publique sua solução no classroom na atividade da prova

Problema:

Seu grupo foi contratado para desenvolver um aplicativo gerenciamento de vendas
e estoque para uma revenda de veículos online. 

Seu aplicativo deve conter as seguintes funcionalidades:

- Um menu com opçoes para o usuário
- Verificar estoque de veículos: crie um estoque fictício
- Registrar um veículo
- Vender um veículo
- Adicionar o valor de venda do veículo em um controle de finanças, o seu custo e o lucro obtido
- Printar um demonstrativo de todas as vendas e compras dos veículos 


'''
estoque = ['Gol', 'Palio', 'Lancer', 'Peugeot', 'S10', 'Ranger']
class Veiculo:
    def __init__(self, nome, preco_compra):
        self.nome = nome
        self.preco_compra = preco_compra
        self.preco = 0
        self.lucro = 0 


def main():
    print("Seja bem-vindo à MotorMania, somos uma revenda de veículos totalmente online.")
    print("1 - Verificar estoque.")
    print("2 - Registrar veiculo.")
    print("3 - Vender um veiculo.")
    print("4 - Controle de finança.")
    print("5 - Sair")
    opcao = input("Digite o número da opção desejada: ")
    if opcao == "1":
        verificar_estoque()
    elif opcao == "2":
        registrar_veiculo()
    elif opcao == "3":
        vender_veiculo()
    elif opcao == "4":
        controle()
    else:
        print("Opção inválida.")

def registrar_veiculo():
    nome = input("Digite o nome do veiculo:")
    preco = input("Digite o valor do carro:")
    veiculo = Veiculo(nome, preco)
    estoque.append(veiculo)
    print(f"{nome} foi adicionado ao estoque")

def vender_veiculo():
    nome = input("Digite o nome do veiculo a ser vendido.")
    for veiculo in estoque:
        if veiculo.nome == nome:
            preco = float(input(f"Digite o preco de venda {veiculo.nome}"))
            veiculo.preco = preco.venda
            veiculo.lucro = veiculo.preco - veiculo.preco_compra
            print(f"{veiculo.nome} foi vendido com sucesso! Lucro R${veiculo.lucro}")
            return
        
def verificar_estoque():
    print("Aqui está a lista de modelos de carros:")
    print('''
         1-Gol
         2-Palio
         3-Lancer
         4-Peugeot
         5-S10
         6-Ranger''')

    modelo_carro = input("Digite o número do modelo do carro que você deseja: ")

    carros(modelo_carro)

def carros(modelo_carro):
    if modelo_carro == "1":
        print("Gol G4 2008 completo por apenas R$26.000")
    elif modelo_carro == "2":
        print("Palio economy 2010 com 100.000 km rodados por apenas R$12.000")
    elif modelo_carro == "3":
        print("Lancer Evolution X 2.0 2014 com 50.000 km rodados por apenas R$150.000")
    elif modelo_carro == "4":
        print("Peugeot 308 1.6 thp 2014 com 90.000 km rodados por apenas R$43.000")
    elif modelo_carro == "5":
        print("S10 2023 0 km por apenas R$215.000")
    elif modelo_carro == "6":
        print("Ranger 2024 0 km por apenas R$320.000")
    else:
        print("Modelo de carro não reconhecido.")
def controle():
    if not estoque:
            print("Nenhuma venda realizada ainda.")
    else:
            print("\nDemonstrativo de Vendas e Compras:")
            for veiculo in estoque:
                if veiculo.preco_venda > 0:
                    print(f"{veiculo.nome}: Venda por R${veiculo.preco_venda}, Lucro: R${veiculo.lucro}")
                else:
                    print(f"{veiculo.nome}: Ainda não foi vendido.")
if __name__ == '__main__':
    main()
