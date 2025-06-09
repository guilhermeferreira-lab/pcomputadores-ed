'''Uma livraria quer registrar os preços de 5 livros. Depois, exiba o maior valor registrado.'''

livros = []
for i in range(5):
    livro = int(input(f"digite os preços {i + 1}: "))
    livros.append(livro)
max_livros = max(livros)
print(max_livros)