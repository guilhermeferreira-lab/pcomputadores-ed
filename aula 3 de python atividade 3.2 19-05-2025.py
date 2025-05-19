'''3.2) Desempenho escolar: Solicite ao usuário que informe a nota de um aluno (de 0 a 10)
 e classifique seu desempenho, considerando-se os intervalos a seguir:

Abaixo de 5: "Reprovado"
De 5 até 6.9: "Recuperação"
7 ou mais: "Aprovado"'''

nota = float(input("qual é a nota:"))

if (nota <= 5):
    print("reprovado")
elif (nota < 6.9):
    print("recuperação")
else:
    print("aprovado")