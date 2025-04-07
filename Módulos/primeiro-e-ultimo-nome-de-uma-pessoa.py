nome = input("Digite seu Nome Completo: ").strip()
dividido = nome.split()
print("O seu primeiro nome é {}".format(dividido[0]))
print("O seu último nome é {}".format(dividido[len(dividido)-1]))
