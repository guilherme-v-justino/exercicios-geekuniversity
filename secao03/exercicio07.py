"""Algoritmo para determinar peso ideal com base na altura"""

altura = float(input("Qual é a sua altura?: "))
peso_ideal = (72.7 * altura) - 58

print("O seu peso ideal, de acordo com a sua altura, é de {0:.2f} kg".format(peso_ideal))
