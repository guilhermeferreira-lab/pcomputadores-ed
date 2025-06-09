'''Um supermercado deseja armazenar os preços de 4 produtos.
 Após o preenchimento, exiba apenas os preços maiores que R$10,00.'''

produtos = []
for i in range(4):
    produto = float(input(f"digite o preço dos produtos {i + 1}: "))
    produtos.append(produto)
for produto in produtos:
    if produto > 10:
        print(produto)
