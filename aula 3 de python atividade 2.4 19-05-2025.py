'''2.4) Verificação de temperatura corporal: Peça ao usuário que informe sua temperatura corporal.
 Se for maior ou igual a 37.5, exiba "Possível febre"; caso contrário, "Temperatura normal".'''

temperatura = float(input("qual sua temperatura?: "))

if (temperatura >= 37.5):
    print("possivel febre")
else:
    print("temperatura normal")


    import random

    numeroAleatorio = random.randint(1, 6)
    print(numeroAleatorio)