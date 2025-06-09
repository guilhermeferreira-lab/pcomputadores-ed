'''Um professor quer calcular a média das idades dos 6 alunos que participaram de uma aula.
 Solicite as idades e exiba a média.'''

notas = []
for i in range (6):
    nota = float(input(f"digite as notas {i + 1}: "))
    notas.append(nota)
media = sum(notas)/ len(notas)
print(media)