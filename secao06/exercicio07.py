"""Ler 4 numeros, calcular o quadrado e imprimir com condição"""

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))
n4 = int(input("Digite o quarto número: "))

q1 = n1 ** 2
q2 = n2 ** 2
q3 = n3 ** 2
q4 = n4 ** 2

if q3 >= 100:
    print(q3)
else:
    print(q1)
    print(q2)
    print(q3)
    print(q4)
