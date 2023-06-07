import random

class Forca:
    def jogar ():
        print("="*27)
        print("Bem vindo ao jogo da Forca!")
        print("="*27)

        palavra_secreta = "banana"
        letras_acertadas = ["_", "_", "_", "_", "_", "_"]

        enforcou = False
        acertou = False

        print(letras_acertadas)

        while (not enforcou and not acertou):
            chute = input("Qual letra? ")
            chute = chute.strip()

            index = 0
            for letra in palavra_secreta:
                if (chute.upper() == letra.upper()):
                    letras_acertadas[index] = letra
                index = index + 1

            if palavra_secreta == chute:
                print("Você acertou!")
                break

            print(letras_acertadas)

        print("Fim do jogo")

class Adivinhacao:
    def jogar ():
        print("="*33)
        print("Bem vindo ao jogo de Adivinhação!")
        print("="*33)

        numero_secreto = random.randrange(1, 101)
        total_de_tentativas = 0
        pontos = 1000

        print("Qual nível de dificuldade?")
        print("(1) Fácil (2) Médio (3) Difícil")

        nivel = int(input("Defina o nível: "))

        if (nivel == 1):
            total_de_tentativas = 20
        elif (nivel == 2):
            total_de_tentativas = 10
        else:
            total_de_tentativas = 5

        for rodada in range(1, total_de_tentativas + 1):
            print("Tentativa {} de {}".format(rodada, total_de_tentativas))

            chute_str = input("Digite um número entre 1 e 100: ")
            print("Você digitou ", chute_str)
            chute = int(chute_str)

            if (chute < 1 or chute > 100):
                print("Você deve digitar um número entre 1 e 100!")
                continue

            acertou = chute == numero_secreto
            maior = chute > numero_secreto
            menor = chute < numero_secreto

            if (acertou):
                print("Você acertou e fez {} pontos!".format(pontos))
                break
            else:
                if (maior):
                    print("Você errou! O seu chute foi maior do que o número secreto.")
                elif (menor):
                    print("Você errou! O seu chute foi menor do que o número secreto.")
                pontos_perdidos = abs(numero_secreto - chute)
                pontos = pontos - pontos_perdidos

        print("Fim do jogo")

def escolhe_jogo():
    print("="*28)
    print("BEM VINDO A CENTRAL DE JOGOS")
    print("="*28)

    print("(1) Forca (2) Adivinhação")

    jogo = int(input("Qual jogo? "))

    if(jogo == 1):
        print("Iniciando jogo da Forca...")
        Forca.jogar()
    elif(jogo == 2):
        print("Iniciando jogo da Adivinhação...")
        Adivinhacao.jogar()
escolhe_jogo()