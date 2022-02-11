"""Ler um número e verificar se é par ou ímpar. Se par, armazenar em p, se impar armazenar em i
e exibir as duas variaveis"""

p = 0
i = 0
n = int(input("Digite um número:"))

if n % 2 == 0:
    p = n
else:
    i = n
print(p)
print(i)
