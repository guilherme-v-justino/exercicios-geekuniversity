"""Mudar ações de acordo com indice de poluição recebido"""

i = float(input("Digite o índice de poluição atual: "))

if 0.3 <= i < 0.4:
    print("Industrias do grupo 1 devem suspender as atividades")
elif 0.4 <= i < 0.5:
    print(" Industrias do grupo 1 e 2 devem suspender as atividades")
elif i >= 0.5:
    print("Todos os grupos devem parar a atividade")
else:
    print("O índice de poluição está dentro dos parâmetros normais. Manter atividade industrial.")

