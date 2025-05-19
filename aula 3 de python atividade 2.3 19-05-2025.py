'''2.3) Verificação de trânsito: Um motorista precisa verificar se está acima do limite de velocidade 
de 80 km/h. Peça a velocidade atual e exiba "Multa por excesso de velocidade" se for maior que 80, ou 
"Velocidade dentro do permitido" caso contrário.
'''

velocidade = int(input("qual a velocidade :"))

if (velocidade >= 80):
    print("multa por excesso de velocidade")
else:
    print("velocidade permitida")