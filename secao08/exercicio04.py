"""Somar os elementos de um vetor com 20 numeros"""

vetor = []
soma = 0

for n in range(0, 20):
    num = int(input("Digite um número {0}/20: ".format(n + 1)))
    vetor.append(num)
    soma = soma + num
print(" A soma dos elementos é {0}".format(soma))
