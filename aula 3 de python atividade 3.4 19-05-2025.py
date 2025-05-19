'''3.4) Sistema de notas com conceito: Solicite uma nota de 0 a 10 
e classifique o conceito do aluno:

9 a 10: "Conceito A"
7 a 8.9: "Conceito B"
5 a 6.9: "Conceito C"
Abaixo de 5: "Conceito D"'''

nota = int(input("qual a nota: "))

if (nota < 5):
    print("Conceito D")
elif (nota <= 6.9):
    print("Conceito C")
elif (nota <= 8.9):
    print("Conceito B")
else:
    print("Conceito A")