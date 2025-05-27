'''2. Senha segura: Você precisa criar um sistema de acesso
 com verificação de senha. O programa deve pedir ao usuário que digite a senha até que ela esteja correta.
 A senha correta é "segredo123". Quando o usuário acertar, exiba: "Bem-vindo ao sistema!"

Dica: use o operador != para verificar se a senha está errada.
'''


senha = ""
while senha != "segredo123":
    senha = input("Digite a senha correta: ")

print("Bem-vindo ao sistema!")