"""Algoritmo que conte até 100 e a cada multiplo de 10, imprima um texto"""

for n in range(1, 101):
    print(n)
    if n % 10 == 0:
        print("Múltiplo de 10")
