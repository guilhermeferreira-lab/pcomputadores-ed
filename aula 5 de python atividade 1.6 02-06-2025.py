''' Crie uma lista com o nome de 3 cidades e depois mostre os nomes em ordem inversa à digitada.'''

citys = []
for i in range (3):
    city = str(input(f"igite o nome das cidades {i + 1}: "))
    citys.append(city)
for i in reversed(citys):
    print(i)
    