'''Conversor de Temperatura: Crie uma função que receba uma temperatura em Celsius
 e retorne a temperatura em Fahrenheit.
 Para tanto, use a fórmula: (Celsius * 9/5) + 32'''

def temp(numero):
    return (numero * 9/5) + 32

numero = int(input("entre com a temperatura em celsius : "))
print(temp(numero))