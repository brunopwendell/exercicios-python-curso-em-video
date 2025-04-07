nome = input("Digite seu Nome Completo: ").strip()
print("Seu nome com todas as Letras Maiúsculos: {}".format(nome.upper()))
print("Seu nome com todas as Letras Minúsculas: {}".format(nome.lower()))
print("Quantas Letras totais: {}".format(len(nome) - nome.count(" ")))
print("Quantidade de Letras no Primeiro Nome: {}".format((nome.find(" "))))
"""dividido = nome.split()
print("Quantidade de Letras no Primeiro Nome: {}".format(len(dividido[0])))
"""
