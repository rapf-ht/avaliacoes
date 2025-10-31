listaDeCores = ["Rosa", "Vermelho", "Azul", "Cinza", "Preto"]
print(listaDeCores)
corRemove = str(input("Escreva a cor que deseja retirar da lista\n"))
if corRemove.capitalize() in listaDeCores:
    listaDeCores.remove(corRemove)
    print("Lista Atual: ", listaDeCores)