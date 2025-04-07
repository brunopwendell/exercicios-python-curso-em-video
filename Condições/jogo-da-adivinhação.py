from random import randint
print("Jogo da Adivinhação")
numero = randint(0,5)

numero_usuario = int(input("Digite um número entre 0 a 5: "))
if numero == numero_usuario:
    print("Parabéns, você acertou o número")
else:
    print("Infelizmente, você errou o número")
