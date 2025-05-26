'''
8. Soma de notas e cálculo de média. Uma professora quer somar as 
notas de 5 avaliações. Crie um programa que peça 5 notas e, ao final,
 exiba o total e a média das notas informadas.
'''

soma =  0
for i in range(1, 6):
    notas = float(input("quais são as notas :"))
    soma += notas
print("soma das notas", soma)

print("a media é: ", soma / 5)









