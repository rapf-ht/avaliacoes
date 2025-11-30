# Desenvolva um módulo Python chamado `catalogo_produtos.py` que contenha uma função para exibir
# um catálogo de produtos disponíveis em uma loja online. Cada produto deve ter um nome, descrição
# e preço. A função deve formatar a saída de maneira clara e organizada.
# Os produtos de exemplo são:
# 1. Nome: "Camiseta", Descrição: "Camiseta de algodão confortável", Preço: 29.90
# 2. Nome: "Calça Jeans", Descrição: "Calça jeans azul escura", Preço: 99.90
# 3. Nome: "Tênis Esportivo", Descrição: "Tênis para corrida e caminhada", Preço: 149.90

# adicionar_produto(produtos, "Boné", "Boné esportivo ajustável", 39.90)
# adicionar_produto(produtos, "Mochila", "Mochila resistente para uso diário", 89.90)
# adicionar_produto(produtos, "Relógio", "Relógio digital à prova d'água", 199.90)

itens = {
    1:{"title": "O Hobbit",
     "author": "J.R.R. Tolkien",
     "price": 49.90},
    2:{"title": "Dom Casmurro",
     "author": "Machado de Assis",
     "price": 39.90},
    3:{"title": "1984",
     "author": "George Orwell",
     "price": 59.90},
    4:{"title": "A Menina que Roubava Livros",
     "author": "Markus Zusak",
     "price": 44.90},
    5:{"title": "O Pequeno Príncipe",
     "author": "Antoine de Saint-Exupéry",
     "price": 29.90}
}

# Função responsável por exibir os produtos disponíveis no catálogo
def exibir_catalogo(itens):
    print("\n Catálogo de produtos disponíveis: ")
    print("---------------------------------")
    for id_produto, dados_produto in itens.items():
        print(f"ID: {id_produto}")
        print(f"Autor: {dados_produto["author"]}")
        print(f"Título: {dados_produto["title"]}")
        print(f"Preço: R$ {dados_produto["price"]:.2f}")
        print(f"\n---------------------------------")
