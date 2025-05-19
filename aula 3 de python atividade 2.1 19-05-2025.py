'''2.1) Entrada no parque: No parque municipal, só é permitida a entrada de pessoas com 18 anos ou mais.
 Sendo assim, solicite a idade de uma pessoa. Se ela for maior ou igual a 18, mostre "Entrada permitida"; 
 caso contrário, "Entrada proibida para menores de idade".
'''

idade = int(input("qual a sua idade: "))

if (idade >= 18):
    print("entrada permitida")
else:
    print("acesso negado")