'''Leia uma matriz 2x3 e conte quantos elementos são maiores que 10.
'''

maior10 = 0
Matrizm = []

for i in range(2):
    linha = []
    for j in range (3):
        valor = int(input('valor:'))
        linha.append(valor)
        if(valor > 10):
           print(valor)
           maior10 += 1
    Matrizm.append(linha)

for linha in Matrizm:
    print(linha)
print("existem tanto numeros maiores que 10:", maior10)