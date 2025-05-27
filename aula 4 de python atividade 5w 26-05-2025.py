'''
5. Calculadora de média até negativo: 
Você quer calcular a média de várias notas de aluno, mas não sabe quantas ainda vai receber. 
Faça um programa que peça notas (valores entre 0 e 10) ao usuário repetidamente, até que ele digite 
um valor negativo. Ao final, mostre a média de todas as notas, sem considerar o valor negativo.'''

nota = float(input("digite a nota"))
soma = 0
media = 0.0
contaNota = 0
while( nota > 0):
    soma += nota
    contaNota += 1
    nota = float(input("digite a nota"))
media = soma / contaNota
print(media)
    