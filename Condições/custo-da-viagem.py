print("O preço da viagem")
km = float(input("Qual é a distância que você quer percorrer: "))
valor = 0
if km > 200:
    valor = km * 0.45
else:
    valor = km * 0.50
print("Você vai começar sua viagem em KM {}".format(km))
print("E o preço da sua passagem é R$ {:.2f}".format(valor))
