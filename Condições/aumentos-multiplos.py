print("Aumento do Salário")
salario = float(input("Digite seu salário: R$"))
if salario > 1250:
    potencia = salario * 10/100
    salario = salario + potencia
    print("Você vai ter um aumento de 10% o que vale a R$ {:.2f} tendo um total de R$ {:.2f}".format(potencia,salario))
else:
    potencia = salario * 15 / 100
    salario = salario + potencia
    print("Você vai ter um aumento de 15% o que vale a R$ {:.2f} tendo um total de R$ {:.2f}".format(potencia, salario))
