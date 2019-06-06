import random

def jogar():

    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")

    numero_secreto = random.randrange(1, 101)
    total_de_tentativas = 0
    pontos = 1000
    pontos_perdidos = 0
    continuar = 1

    while continuar == 1:
        print("Qual o nível de dificuldade?")
        print("(1) Fácil (2) Médio (3) Difícil")

        nivel = int(input("Defina o nível: "))

        if nivel == 1:
            total_de_tentativas = 15
        elif nivel == 2:
            total_de_tentativas = 10
        elif nivel == 3:
            total_de_tentativas = 5
        else:
            print("Nível indisponível!")

        for rodada in range(1, total_de_tentativas + 1):
            print("Tentativa {} de {}".format(rodada, total_de_tentativas))

            chute = int(input("Digite um número entre 1 e 100: \n"))
            print("Você digitou " , chute)

            if(chute < 1 or chute > 100):
                print("Você deve digitar um número entre 1 e 100!")
                continue

            acertou = chute == numero_secreto
            maior   = chute > numero_secreto
            menor   = chute < numero_secreto
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

            if(acertou):
                print("Você acertou e fez {} pontos!".format(pontos))
                break
            else:
                if(maior):
                    print("Você errou! O seu chute foi maior do que o número secreto.")
                elif(menor):
                    print("Você errou! O seu chute foi menor do que o número secreto.")

        print("Fim do jogo!  O número era {}.".format(numero_secreto))
        print("Deseja continuar jogando ?")
        continuar = int(input("Digite [1] sim e [0] não: "))


    print("Fim do jogo")
if __name__ == "__main__":

    jogar()