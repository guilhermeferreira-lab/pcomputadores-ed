'''11-) Controle de Temperatura em Estufas Inteligentes:
Imagine que você trabalha em uma fazenda que utiliza estufas inteligentes para o cultivo de plantas.
Cada estufa possui sensores que registram a temperatura do ambiente em tempo real.
Seu papel é desenvolver um programa que, para 5 estufas,
leia a temperatura atual e classifique-a da seguinte forma:

Abaixo de 15°C: "Temperatura muito baixa! Risco para as plantas."
Entre 15°C e 25°C: "Temperatura ideal."
Acima de 25°C: "Temperatura alta! Acionar ventilação."

O programa deve exibir a mensagem correspondente para cada estufa.'''

for i in range(1, 6):
    temperatura =  int(input("qual a temperatura das estufas: "))
    if(temperatura < 15):
        print("Temperatura muito baixa! Risco para as plantas.")
    elif (temperatura <= 25):
        print("Temperatura ideal.")
    else:
        print( "Temperatura alta! Acionar ventilação.")