'''Registre a temperatura de 7 dias e mostre a média semanal.
'''

temps = []
for i in range(7):
    temp = float(input(f"digite a temperatura{i + 1}: "))
    temps.append(temp)
media = sum(temps)/ len(temps)
print(media)    