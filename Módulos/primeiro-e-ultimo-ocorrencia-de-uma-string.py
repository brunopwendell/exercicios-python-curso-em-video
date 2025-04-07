frase = input("Digite uma frase: ").strip().lower()

print("Quantas vezes aparece a letra A: {}".format(frase.count("a")))
print("Em que Posição aparece a primeira vez: {}".format(frase.find("a")+1))
print("Em que Posição aparece a ultimo vez: {}".format(frase.rfind("a")+1))