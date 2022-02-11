"""Ler número inteiro e diferenciar par, ímpar, positivo e negativo"""

num = int(input("Digite um número: "))

if num % 2 == 0:
    if num > 0:
        print("Este número é par e positivo")
    if num < 0:
        print("Este número é par e negativo")
else:
    if num > 0:
        print("Este número é ímpar e positivo")
    if num < 0:
        print("Este número é ímpar e negativo")
