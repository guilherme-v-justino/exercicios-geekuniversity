"""Gerador de tabuada"""

num = int(input("Informe um número entre 1 e 10: "))

while 1 > num > 10:
    num = int(input("Informe um número: "))
print("Tabuada de {0}".format(num))
for i in range(0, 11):
    print(" {0} x {1} = {2}".format(num, i, (num * i)))

