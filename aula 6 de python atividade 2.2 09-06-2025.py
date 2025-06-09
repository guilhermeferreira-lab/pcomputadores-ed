'''Leia uma matriz 2x2 e calcule a soma de todos os seus elementos.'''

somaV = 0
Matrizm = []

for i in range(2):
    linha = []
    for j in range (2):
        valor = int(input('valor:'))
        linha.append(valor)
        somaV = somaV + valor
    Matrizm.append(linha)

for linha in Matrizm:
    print(linha)

print(somaV)