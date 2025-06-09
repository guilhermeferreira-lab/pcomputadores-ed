'''Solicite 5 números ao usuário e mostre quantos deles são pares.'''
numeros = []
for i in range(5):
    numero = int(input(f"digite os numeros {i +1 }: "))
    numeros.append(numero)
for numero in numeros:
    if(numero % 2 == 0):
        print(numero)