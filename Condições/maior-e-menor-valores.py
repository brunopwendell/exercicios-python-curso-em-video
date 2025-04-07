print("O Maior e o Menor")
n1 = float(input("Digite um número: "))
n2 = float(input("Digite outro número: "))
n3 = float(input("Digite um número: "))
if n1 > n2 and n1 > n3:
    print("Maior: {}".format(n1))
elif n2 > n3:
    print("Maior: {}".format(n2))
else:
    print("Maior: {}".format(n3))

if n1 < n2 and n1 < n3:
    print("Menor: {}".format(n1))
elif n2 < n3:
    print("Menor: {}".format(n2))
else:
    print("Menor: {}".format(n3))
