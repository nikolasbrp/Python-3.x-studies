import random

final = "sim"

while final == "sim":

    n = random.randint(0, 10)

    resposta = input("Chute um número de 0 a 10: ")
    resposta = int(resposta)

    while resposta != n:

        if resposta < n:
            resposta = input("Seu número é menor do que a resposta, chute outro número: ")
            resposta = int(resposta)

        elif resposta > n:
            resposta = input("Seu número é maior do que a resposta, chute outro número: ")
            resposta = int(resposta)

    else:
        n = str(n)
        print("Parabéns, o número correto era " + n)
        final = input("Você deseja continuar? ")

else:
    print("Obrigado por jogar!")