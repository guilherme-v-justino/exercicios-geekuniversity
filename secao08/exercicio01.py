"""Vetor com 5 elementos, armazenar numeros pares maiores que 0"""
vetor = []
pares = []
for n in range(1, 6):
    vetor.append(n)
    if n % 2 == 0:
        pares.append(n)
print(vetor)
for p in pares:
    print(p)
