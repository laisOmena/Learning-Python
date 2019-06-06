import forca
import adivinhacao

def escolha():
    print("*******************************")
    print("******Escolha o seu jogo!******")
    print("*******************************")

    print("(1) Forca (2) Adivinhação")
    escolha = int(input("Qual jogo você quer jogar? "))

    if escolha == 1:
        print("jogando forca")
        forca.jogar()
    elif escolha == 2:
        print("Jogando adivinhação")
        adivinhacao.jogar()
        
if __name__ == "__main__":
    escolha()