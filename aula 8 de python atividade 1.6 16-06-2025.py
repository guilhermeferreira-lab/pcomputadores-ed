'''Média de Notas: Crie uma função que receba uma lista de notas e retorne a média.
'''

def med(nots):
    return sum(nots) / len(nots)

print(med([5, 7, 8, 7 , 5, 4]))