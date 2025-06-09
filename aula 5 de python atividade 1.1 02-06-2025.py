'''Uma escola quer armazenar as notas de 5 alunos em uma lista.
 Peça as 5 notas ao usuário e, em seguida, mostre todas as notas digitadas.
'''



notas = []
for i in range (5):
    nota = float(input(f"digite as notas {i + 1}: "))
    notas.append(nota)
print(notas)