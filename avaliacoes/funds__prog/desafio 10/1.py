listaDeNomes = []
while True:
    nome = str(input("Escreva um nome:"))
    choice = str(input("Deseja continuar? S/N\n"))
    listaDeNomes.append(nome)
    if choice.upper() != "S":
        print(listaDeNomes)
        break