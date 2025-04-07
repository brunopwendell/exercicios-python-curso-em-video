import random
numero = random.randint(0 , 9999)
print(numero)
u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10
print("Milhar: {}".format(m))
print("Centena: {}".format(c))
print("Dezena: {}".format(d))
print("Unidade: {}".format(u))



