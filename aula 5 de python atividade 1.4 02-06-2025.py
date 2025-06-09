'''Armazene os nomes de 5 frutas em uma lista e mostre as frutas uma por uma.'''
frutas = []
for i in range(6):
    fruta = str(input(f"digite as frutas{i + 1}: "))
    frutas.append(fruta)
for fruta in frutas:
    print(fruta)