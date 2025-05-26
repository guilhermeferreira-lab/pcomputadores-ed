'''
12) Crie uma proposta original de programa que utilize a estrutura de repetição for.
Pense em uma situação diferente das que já foram trabalhadas anteriormente e elabore 
um pequeno programa que faça uso do laço for.
Na sua resposta, apresente uma breve descrição do que o programa faz e, em seguida, 
mostre a implementação do código.
'''

import random
numero = 0
for i in range(1, 6):
    numero = random.randint(1, 10)
    if(numero % 2 == 0):
        print("voce morreu, perdeu uma vida")
    else:
        print("voce esta vivo")
