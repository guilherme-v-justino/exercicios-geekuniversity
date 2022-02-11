vetor = []
codigo = int(input("Digite o código: "))
if codigo != 0:
    for n in range(0, 5):
        num = int(input("Digite um valor: "))
        vetor.append(num)
    if codigo == 1:
        for n in vetor:
            print(n)
    if codigo == 2:
        vetor.reverse()
        for n in vetor:
            print(n)





