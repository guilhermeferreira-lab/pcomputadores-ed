''' Armazene 5 números inteiros e mostre o menor valor.'''

numeros = []
for i in range(5):
    numero = int(input(f"digite os numeros {i + 1}: "))
    numeros.append(numero)
menor_numero = min(numeros)
print(menor_numero)