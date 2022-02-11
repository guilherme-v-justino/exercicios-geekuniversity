"""Algoritmo para calcular salário, levando em conta horas extras"""

excesso = 0
codigo = int(input("Qual o seu código?:"))
numero_horas = int(input("Qual o número de horas trabalhadas?: "))

if numero_horas > 50:
    excesso = numero_horas - 50
    numero_horas = numero_horas - excesso
extra = excesso * 20
salario = numero_horas * 10
total = extra + salario

print("Código de trabalhador: {0}".format(codigo))
print("O seu salário deste mês será {0} reais".format(salario))
print("Seu pagamento por horas extras será de {0}".format(extra))
print("Totalizando {0} reais".format(total))
