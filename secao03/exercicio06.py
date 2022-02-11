"""Algoritmo para calcular salário"""

quantidade_de_horas = int(input("Quantas horas você trabalhou no mês?: "))
valor_hora = float(input("Quanto você ganha por hora?: "))

salario = (quantidade_de_horas * valor_hora)

print("Seu salário deste mês é de {0:.2f} reais".format(salario))
