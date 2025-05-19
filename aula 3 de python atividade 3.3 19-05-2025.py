'''3.3) Avaliação de IMC (simplificada): Peça ao usuário seu IMC (Índice de Massa Corporal).
 Classifique-o conforme os seguintes intervalos:

Abaixo de 18.5: "Abaixo do peso"
Entre 18.5 e 24.9: "Peso normal"
25 ou mais: "Acima do peso"
'''

peso = float(input("qual seu IMC:"))

if (peso <= 18.5):
    print("IMC muito baixo")
elif (peso <= 24.9):
    print("IMC normal")
else:
    print("IMC muito alto")
