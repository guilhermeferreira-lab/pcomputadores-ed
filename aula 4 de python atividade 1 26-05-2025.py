'''1. Contagem para a festa. Você está organizando uma festa de 
aniversário e precisa distribuir 10 convites. 
Escreva um programa que imprima uma mensagem numerada de 1 a 10,
 indicando para quem será entregue cada convite.

Exemplo de saída:

Entregando convite número 1
Entregando convite número 2
...
...
Entregando convite número 10'''

convite = int(input("quantos convites serão? "))

for i in range (1, 11):
    print('entregando o convite' , i)