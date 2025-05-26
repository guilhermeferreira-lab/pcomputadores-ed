'''3. Tabuada do 3. Crie um programa que exiba a tabuada do número 3, do 1 ao 10. 
O formato da resposta deve seguir o padrão: 3 x 1 = 3, 3 x 2 = 6, e assim por diante.'''

numero = 3

for i in range(1, 11):
    print(numero, 'x', i, '=', numero * i)