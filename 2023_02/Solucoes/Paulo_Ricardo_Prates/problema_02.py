# Começo com importacoes
import math # Exemplo não vai servir pra nada no programa

# Defino funções
def multiplica(multi1, multi2):
    multiplicacao = multi1 * multi2
    return  multiplicacao

# Corpo do software - começa o programa
multi1 = int(input('Digite o primeiro valor:'))
multi2 = int(input('Digite o segundo valor:'))

# Chamo a função que faz o que eu quero
resultado = multi1 * multi2
print(resultado)
