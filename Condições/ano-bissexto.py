print("Ano Bissexto")
ano = int(input("Digite um Ano para saber se é Bissexto: "))
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print("O ano de {} é bissexto".format(ano))
else:
    print("O ano de {} não é bissexto".format(ano))
    