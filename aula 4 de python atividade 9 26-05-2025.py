'''9. Contagem regressiva para o lançamento. Simule a contagem regressiva de um foguete,
 começando em 10 e terminando com a mensagem "Lançamento!".'''

for i in range(10, -1, -1):
    print(i,'!')
    if(i == 0):
        print("Lançamento!")