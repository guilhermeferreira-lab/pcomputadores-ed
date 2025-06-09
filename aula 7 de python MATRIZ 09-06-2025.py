matrizm = []
for i in range (3):
    linha = []
    for j in range(3):
        valor = int(input('valor :'))
        linha.append(valor)
    matrizm.append(linha)
for linha in matrizm:
    print(linha)
