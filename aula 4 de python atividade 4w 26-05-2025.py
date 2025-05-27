'''4. Validador de número positivo: 
O programa deve pedir ao usuário que digite um número positivo. 
Caso o número informado seja negativo, o programa deve pedir novamente, 
até que o usuário informe um valor válido. Quando isso acontecer, exiba: "Valor aceito: X"

Dica: o while deve se repetir enquanto o número for menor que zero.'''

numero = int(input("digite um numero: "))
while(numero < 0):
    numero = int(input("digite um numero novamente: "))
print(numero)

