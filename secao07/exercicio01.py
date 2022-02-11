"""Algoritmo que determina maior valor entre números até uma condição de parada"""

maior = 0
n = int(input("Digite um valor: "))
while n != 0:
    if n > maior:
        maior = n
    n = int(input("Digite um novo valor: "))
print("O maior valor é {0}".format(maior))
