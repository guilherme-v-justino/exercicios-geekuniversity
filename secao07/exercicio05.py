"""Receber usuario e senha. Emitir erro caso usuario = senha"""

nome = input("Digite o nome do usuário: ")
senha = input("Digite sua senha: ")

while nome == senha:
    print("A senha deve ser diferente do nome de usuário: ")
    nome = input("Digite o nome do usuário: ")
    senha = input("Digite sua senha: ")
