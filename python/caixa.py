# Nome: João Victor Bortoluzzi Miraya
# Curso: Análise e Desenvolvimento de Sistemas
# Disciplina: Projeto Integrador Extensionista – ADS 1
# Semestre Letivo: 1º Termo – 2025

# Define a classe para os produtos do mercado
class Produtos:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def __str__(self):
        return f"{self.nome} - R$ {self.preco:.2f}"

# Define a classe Caixa para gerenciar os produtos e o total da compra
class Caixa:
    def __init__(self):
        self.produtos = []
        self.total = 0.0

    def adicionar_produto(self, produto):
        self.produtos.append(produto)
        self.total += produto.preco

    def calcular_total(self):
        return self.total

    def listar_produtos(self):
        return [str(produto) for produto in self.produtos]

    def finalizar_compra(self):
        if not self.produtos:
            return "Nenhum produto na cesta."
        produtos_str = "\n".join(self.listar_produtos())
        total_str = f"Total: R$ {self.calcular_total():.2f}"
        return f"Compra finalizada:\n{produtos_str}\n{total_str}"


def main():
    # Produtos disponíveis no mercado
    produtos_disponiveis = [
        Produtos("Arroz", 20.00),
        Produtos("Feijão", 8.50),
        Produtos("Macarrão", 6.30),
        Produtos("Óleo", 7.90),
        Produtos("Leite", 4.25),
    ]

    caixa = Caixa()

    print("---- Mercadinho BigBom ----")
    while True:
        print("\nProdutos disponíveis:")
        for i, produto in enumerate(produtos_disponiveis, start=1):
            print(f"{i} - {produto}")
        print("0 - Finalizar compra")

        escolha = input("Digite o número do produto para adicionar (0 para finalizar): ")

        if escolha == '0':
            break

        if not escolha.isdigit() or not (1 <= int(escolha) <= len(produtos_disponiveis)):
            print("Opção inválida. Tente novamente.")
            continue

        produto_escolhido = produtos_disponiveis[int(escolha) - 1]
        caixa.adicionar_produto(produto_escolhido)
        print(f"Produto '{produto_escolhido.nome}' adicionado ao caixa.")

    # Finaliza e mostra total
    print("\n" + caixa.finalizar_compra())

    # Pede valor pago e calcula troco
    while True:
        try:
            valor_pago = float(input("Digite o valor pago pelo cliente: R$ "))
            total = caixa.calcular_total()
            if valor_pago < total:
                print(f"Valor insuficiente. O total é R$ {total:.2f}. Tente novamente.")
                continue
            troco = valor_pago - total
            print(f"Troco a ser devolvido: R$ {troco:.2f}")
            break
        except ValueError:
            print("Por favor, digite um valor numérico válido.")


if __name__ == "__main__":
    main()
