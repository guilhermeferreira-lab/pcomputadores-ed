'''3. Contagem regressiva para lançamento:
 Você está programando a contagem regressiva de um foguete.
O programa deve exibir os números de 10 até 1 na tela, um por um, e ao final exibir: "Lançamento!"

Dica: comece a variável em 10 e vá diminuindo com -1.
'''

contador = 10
while contador >= 1:
    print(f"Contando: {contador}")
    contador -= 1
print("Lançamento!")