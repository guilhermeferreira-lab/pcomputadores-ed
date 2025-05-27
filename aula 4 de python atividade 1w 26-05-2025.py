'''1. Cofrinho inteligente: Imagine que você está guardando moedas 
em um cofrinho. A cada vez que você adiciona uma moeda,
o valor total aumenta. O programa deve continuar perguntando
o valor das moedas depositadas até que o total ultrapasse R$ 10,00.
 Ao final, exiba: "Meta atingida! Você já tem R$ XX,XX no cofrinho."

Dica: use uma variável acumuladora para somar os valores.
'''

#moeda = int(input("ensira uma moeda"))
cofre = 0
while (cofre < 10):
    moeda = int(input("ensira uma moeda"))
    cofre += moeda
print( "valor do cofre", cofre)