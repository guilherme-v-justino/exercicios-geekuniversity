"""Receber altura e sexo e calcular o peso ideal"""

altura = float(input("Qual é a sua altura?: "))
sexo = input("Qual o seu sexo (M/F) ?: ")

if sexo.lower() == 'm':
    peso_ideal = (72.7 * altura) - 58
elif sexo.lower() == 'f':
    peso_ideal = (62.1 * altura) - 44.7
else:
    print("Sexo não identificado!")
    peso_ideal = 0

print("Seu peso ideal é de {0:.2f}kg".format(peso_ideal))
