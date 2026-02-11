import random 
numero = random.randint(1,20)

while True:
    chute = int(input("Digite Seu Chute de 1 a 20: "))
    if chute == numero:
        break
    else:
        print("Errou")

print("Você Acertou")