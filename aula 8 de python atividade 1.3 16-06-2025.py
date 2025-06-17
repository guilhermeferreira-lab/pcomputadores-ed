''' Calculadora de Área de Retângulo:
 Crie uma função que receba a base e a altura de um retângulo e retorne a área.'''

def area(base, altura):
    return base * altura

x = int(input("qual a base? :"))
y = int(input("qual a altura? :"))

print(area(x, y))

