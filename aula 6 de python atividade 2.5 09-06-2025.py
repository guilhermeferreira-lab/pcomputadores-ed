''' Leia uma matriz 2x3, 
conte e mostre separadamente quantos elementos são par e quantos elementos são impar.'''
contapar = 0
contaimpar = 0
Matrizm = []

for i in range(2):
    linha = []
    for j in range (3):
        valor = int(input('valor:'))
        linha.append(valor)
        if(valor % 2 == 0):
            contapar += 1
        else:
            contaimpar += 1
    Matrizm.append(linha)

for linha in Matrizm:
    print(linha)
print("existem essa quantidade de numeros pares:", contapar)
print("existem essa quantidade de numeros impares:", contaimpar)