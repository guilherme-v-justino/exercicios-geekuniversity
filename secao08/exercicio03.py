""""Vetor com 10 numeros que seja impresso em ordem inversa"""

vetor = []
for n in range(0, 10):
    num = int(input("Digite um número: "))
    vetor.append(num)
vetor.reverse()
for n in vetor:
    print(n)
