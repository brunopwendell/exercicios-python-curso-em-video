from math import hypot
print("Hipotenusa de um Triângulo Retângulo")
cateto_oposto = float(input("Qual é o comprimento do Cateto Oposto: "))
cateto_adjacente = float(input("Qual é o comprimento do Cateto Adjacente: "))

print("A Hipotenusa é {:.2f}".format(hypot(cateto_oposto,cateto_adjacente)))
