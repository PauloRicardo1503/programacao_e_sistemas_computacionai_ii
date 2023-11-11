class Cadastro:
    def __init__(self, nome, data_N, Cpf, rua, cadastro ):
        self.nome = nome
        self.data_N = data_N
        self.Cpf = Cpf
        self.rua = rua
        self.cadastro = cadastro



def main ():
    print ('Seja bem vindo ao cadastramento de funcionario.')
    while True:
        print ('1. Cadastro de funcionario')
        print ('2. Lista de funcionarios')
        print ('3. Se já é cadastrado.')
        opcao = input("Digite o número da opção desejada: ")
        if opcao == "1":
            cadastro_funcionario()
        else:
            print ("Numero invalido")





def cadastro_funcionario():
    print('Precisamos de alguns dados seu para o cadastro.')
    nome = str(input("Digite seu nome:"))
    data_N = int(input("Digite a data de nascimento:"))
    Cpf = int(input("Digite o seu CPF:"))
    rua = str(input("Digite o endereço da sua residencia:"))
    cadastro = Cadastro(nome, data_N, Cpf, rua, cadastro)

if __name__ == '__main__':
    main()