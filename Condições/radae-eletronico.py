print("Radar Eletrônico")
velocidade = float(input("Qual sua velocidade? "))
if velocidade >= 80:
    velocidade -= 80
    if velocidade == 0:
        print("Você recebera uma multa no valor de R$ 7,00")
    else:
        velocidade *= 7
        print("Você recebera uma multa no valor de R$ {:.2f}".format(velocidade))
else:
    print("Parabéns, continue a dirijir com segurança")