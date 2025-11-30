# Desenvolva um módulo Python chamado `adicionando_carrinho.py` que contenha uma função para adicionar
# produtos a um carrinho de compras em uma loja online. A função deve receber o nome do produto,
# descrição e preço como parâmetros e armazenar essas informações em uma lista. Além disso, a função
# deve exibir uma mensagem confirmando que o produto foi adicionado com sucesso.
import catalogos_produtos

def adicionar_produto():
    # Criar uma lista, representando o carrinho
    carrinho = []
    carrinho_prices = []

    while True:
        novo_produto = input("Digite o id do produto você deseja adicionar ao carrinho:")
        if novo_produto.lower() == "sair":
            print("Finalizando a adição de produtos ao carrinho.")
            print("---------------------------------")
            print("Produtos no carrinho:")
            for produto in carrinho:
                print(f"{produto}º pedido - Livro {catalogos_produtos.itens[produto]["title"]} -> R$ {catalogos_produtos.itens[produto]["price"]:.2f}")
            print(f"Total a pagar: R$ {sum(carrinho_prices):.2f}")
            break
        
        try:
            id_produto = int(novo_produto)
            carrinho.append(id_produto)
            title_livro = catalogos_produtos.itens[id_produto]["title"]
            price_livro = catalogos_produtos.itens[id_produto]["price"]
            print(f"Livro {title_livro} adicionado com sucesso no carrinho!")
            carrinho_prices.append(price_livro)
            print(f"Preço a pagar até o momento: R$ {sum(carrinho_prices):.2f}")
        except ValueError:
            print("Por favor, digite um id válido")
            continue
        except KeyError:
            print("Por favor, digite um id válido")
            continue