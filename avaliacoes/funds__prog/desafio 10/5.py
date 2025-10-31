listaTupla = (4, 7, 0, 8, 1,)
print("Primeiro número da lista: ", listaTupla(0))
print("Último número da lista:", listaTupla(-1))

print("Os três primeiros números da lista: ", listaTupla[:3])

choice_num = int(input("Escreva um número, para ver se esse número está na lista: "))
if choice_num in listaTupla:
    print(f"O número {choice_num} está presente na lista")
else:
    print(f"O número {choice_num} NÃO está presente na lista")