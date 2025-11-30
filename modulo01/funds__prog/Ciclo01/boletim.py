alunos_matriculados = []
escolha = int(input("Quantos alunos cadastrados?"))

for i in range(escolha):
    aluno = []
    nome = str(input("Qual o nome do aluno?\n"))
    aluno.append(nome)
    nota_um = float(input("Qual a primeira nota?\n"))
    aluno.append(nota_um)
    nota_dois = float(input("Qual a segunda nota?\n"))
    aluno.append(nota_dois)
    nota_tres = float(input("Qual a terceira nota?\n"))
    aluno.append(nota_tres)
    media = (nota_um + nota_dois + nota_tres)/3
    aluno.append(media)
    if media >= 7.0:
        msg = "Aprovado"
        aluno.append(msg)
    elif media >= 5.0 and media < 7.0:
        msg = "Recuperação"
        aluno.append(msg)
    elif media < 5.0:
        msg = "Reprovado"
        aluno.append(msg)
    else:
        print("Error")
    alunos_matriculados.append(aluno)
print("""Boletim
      ['Nome', Primeira nota, Segunda nota, Terceira nota, Média, 'Situação do aluno']""")
for i in alunos_matriculados:
    print("|===================================================================|")
    print(i)
