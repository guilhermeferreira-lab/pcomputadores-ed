'''6. Jogo de adivinhação: Crie um jogo simples em que o programa “pensa” em um número secreto 
(por exemplo, 7) e o usuário tenta adivinhar. Enquanto o palpite estiver errado, peça novo chute. 
Ao acertar, parabenize o jogador.

Dica: dê um import random, e use o método random.randint(1, 10)
 para gerar um número aleatório entre 1 e 10, 
por exemplo.'''

import random
numero = 0
adivinha =  int(input("adivinhe o numero: "))
numero = random.randint(1, 10)
while(adivinha != numero):
    print("errou!")
    adivinha =  int(input("adivinhe o numero: "))
print("acertou", numero)

