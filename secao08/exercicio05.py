"""Vetor com 10 numeros. Mostre os valores acima de 50 e sua posição no vetor."""

vetor = []
maior_50 = False
for n in range(0, 10):
    num = int(input("Digite um valor: "))
    vetor.append(num)
for n in vetor:
    if n > 50:
        print("O valor {0} é maior que 50 e está na posição {1}".format(n, vetor.index(n)))
        maior_50 = True
if not maior_50:
    print("Não existem valores maiores que 50")



