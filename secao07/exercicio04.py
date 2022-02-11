"""Ler 10 valores e positivos, encontrar o maior valor, o menor e calcular média"""

maior = -999
menor = 999
soma = 0

for n in range(1, 11):
    valor = int(input("Digite um número: "))
    if valor > 0:
        if valor > maior:
            maior = valor
        if valor < menor:
            menor = valor
        soma = soma + valor
    else:
        valor = int(input("Digite um número"))
media = soma / 10

print("O maior número é {0}".format(maior))
print("O menor número é {0}".format(menor))
print("A média é {0}".format(media))
