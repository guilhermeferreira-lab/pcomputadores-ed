'''Peça 4 nomes de alunos e exiba apenas os nomes que começam com a letra “A”.'''

nomes = []
for i in range(4):
    nome = str(input(f"digite os nomes{i + 1}: "))
    nomes.append(nome)
for nome in nomes:
    if(nome.startswith("A") or nome.startswith("a")):
        print(nome)