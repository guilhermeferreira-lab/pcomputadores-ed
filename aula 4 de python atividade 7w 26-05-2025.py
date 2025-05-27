'''7. Digita um número enquanto par. Programa que solicita um novo número enquanto o valor 
informado for par.'''

numero =int(input("digite um numero :"))
while(numero % 2 == 0):
    numero =int(input("digite um numero novamente :"))
print("fim")