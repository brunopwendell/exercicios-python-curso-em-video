import random
print("Sorteio para Apresentação ")
nome1 = input("Digite o nome do 1° aluno: ")
nome2 = input("Digite o nome do 2° aluno: ")
nome3 = input("Digite o nome do 3° aluno: ")
nome4 = input("Digite o nome do 4° aluno: ")
alunos = [nome1,nome2,nome3,nome4]
random.shuffle(alunos)
print("A ordem será")
print(alunos)
