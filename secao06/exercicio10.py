"""Algoritmo que classifica o nadador em categorias de acordo com idade"""

idade = int(input("Qual é a idade do atleta? "))
if 5 <= idade <= 7:
    print("Infantil A")
elif 8 <= idade <= 11:
    print("Infantil B")
elif 12 <= idade <= 13:
    print("Juvenil A")
elif 14 <= idade <= 17:
    print("Juvenil B")
elif idade >= 18:
    print("Adulto")
else:
    print("Ainda não atingiu idade requerida.")
