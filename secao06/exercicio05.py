"""Algoritmo para calcular multa de excesso de peixes pescados em SP"""

e = 0
m = 0

peso = float(input("Qual o peso total dos peixes pescados?: "))

if peso > 50:
    e = peso - 50
    m = e * 4
print("Peso total de peixes {0:.2f}".format(peso))
print("O excesso é de {0:.2f}kg".format(e))
print("O valor da multa é de {0:.2f} reais".format(m))
