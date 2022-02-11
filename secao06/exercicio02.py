"""Ler um número. Se positivo armazenar em 'a', se negativo em 'b' e mostrar o resultado"""

valor = int(input("Digite um valor: "))

if valor > 0:
    a = valor
    print("O valor é positivo!")
    print(a)
else:
    b = valor
    print("O valor é negativo!")
    print(b)
