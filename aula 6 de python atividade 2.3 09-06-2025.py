'''Crie uma matriz 4x1 com números fornecidos pelo usuário
 e imprima seus elementos multiplicados por 2.
'''
mult = 0
Matrizm = []

for i in range(4):
    linha = []
    for j in range (1):
        valor = int(input('valor:'))
        mult = valor * 2
        linha.append(mult)
    Matrizm.append(linha)

for linha in Matrizm:
    print(linha)