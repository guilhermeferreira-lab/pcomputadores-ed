'''8. Tabuada: Programa que solicita um número e mostra a tabuada desse número.'''

numero = int(input("digite um numero :"))
contador= 1
while(contador <= 10):
    print(numero, "X", contador, "=", numero * contador)
    contador += 1

