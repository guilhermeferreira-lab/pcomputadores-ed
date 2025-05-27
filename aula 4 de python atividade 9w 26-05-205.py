'''Contador de dígitos pares em uma sequência: Peça ao usuário que digite 10 números inteiros,
 um a um. Conte e, ao final, informe quantos desses números eram pares.'''

contador = 0
contaPar = 0
contaImpar = 0
while(contador <= 4):
    numero = int(input("digite um numero :"))
    if(numero % 2 == 0):
        contaPar +=1
    else:
        contaImpar += 1
    contador += 1

print(contaImpar)
print(contaPar)