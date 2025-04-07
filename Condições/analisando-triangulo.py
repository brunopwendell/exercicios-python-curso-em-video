print("Analisador de Triângulo")
print("="*25)
c1 = float(input("Digite o 1º Comprimento: "))
c2 = float(input("Digite o 2º Comprimento: "))
c3 = float(input("Digite o 3º Comprimento: "))
if (c1 + c2 > c3) and (c1 + c3 > c2) and (c2 + c3 > c1):
    print("Você consegui formar um Triângulo")
else:
    print("Você não conseguiu formar um Triângulo")

