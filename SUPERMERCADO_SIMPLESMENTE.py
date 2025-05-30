class Alimento:
    def __init__(self, id, nome, preco):
        self.id = id
        self.nome = nome
        self.preco = preco
        self.proximo = None

    def __str__(self):
        return f"ID: {self.id}, Nome: {self.nome}, Preço: R${self.preco:.2f}"

class Supermercado:
    def __init__(self):
        self.head = None
        self.inicializar_supermercado()

    def inicializar_supermercado(self):
        alimentos_iniciais = [
            ("1", "Arroz", 20.50),
            ("2", "Feijão", 7.80),
            ("3", "Macarrão", 4.20),
            ("4", "Óleo", 6.00),
            ("5", "Açúcar", 3.50),
            ("6", "Café", 10.00),
            ("7", "Sal", 2.00),
            ("8", "Farinha", 4.00),
            ("9", "Leite", 3.90),
            ("10", "Manteiga", 8.50)
        ]

        anterior = None
        for id, nome, preco in alimentos_iniciais:
            novo_alimento = Alimento(id, nome, preco)
            if self.head is None:
                self.head = novo_alimento
            else:
                anterior.proximo = novo_alimento
            anterior = novo_alimento

    def adicionar_alimento(self, id, nome, preco):
        novo_alimento = Alimento(id, nome, preco)
        if not self.head:
            self.head = novo_alimento
            return
        atual = self.head
        while atual.proximo:
            atual = atual.proximo
        atual.proximo = novo_alimento

    def remover_alimento(self, id):
        atual = self.head
        anterior = None
        while atual and atual.id != id:
            anterior = atual
            atual = atual.proximo
        if atual is None:
            print("Alimento nÃ£o encontrado.")
            return
        if anterior is None:
            self.head = atual.proximo
        else:
            anterior.proximo = atual.proximo
        print(f"Alimento com ID {id} removido.")

    def listar_alimentos(self):
        alimentos = []
        atual = self.head
        while atual:
            alimentos.append(atual)
            atual = atual.proximo
        return alimentos

    def primeiro_alimento(self):
        return self.head

    def exibir_supermercado(self):
        atual = self.head
        while atual:
            print(atual)
            atual = atual.proximo

    def procurar_alimento_por_id(self, id):
        atual = self.head
        while atual:
            if atual.id == id:
                print("Alimento encontrado:")
                print(atual)
                if atual.proximo:
                    print("PrÃ³ximo alimento na lista:")
                    print(atual.proximo)
                else:
                    print("Este Ã© o Ãºltimo alimento da lista.")
                return
            atual = atual.proximo
        print("Alimento nÃ£o encontrado.")

def main():
    supermercado = Supermercado()

    while True:
        print("\nGerenciamento de Supermercado")
        print("1. Listar todos os alimentos")
        print("2. Exibir primeiro alimento")
        print("3. Adicionar alimento")
        print("4. Remover alimento")
        print("5. Procurar alimento por ID")
        print("6. Sair")

        escolha = int(input("Digite sua escolha: "))

        if escolha == 1:
            print("\nLista de todos os alimentos no supermercado:")
            supermercado.exibir_supermercado()
        elif escolha == 2:
            print("\nPrimeiro alimento na lista:")
            print(supermercado.primeiro_alimento())
        elif escolha == 3:
            id = input("Digite o ID do alimento: ")
            nome = input("Digite o nome do alimento: ")
            preco = float(input("Digite o preÃ§o do alimento: "))
            supermercado.adicionar_alimento(id, nome, preco)
            print("Alimento adicionado com sucesso.")
        elif escolha == 4:
            id = input("Digite o ID do alimento a ser removido: ")
            supermercado.remover_alimento(id)
        elif escolha == 5:
            id = input("Digite o ID do alimento a ser procurado: ")
            supermercado.procurar_alimento_por_id(id)
        elif escolha == 6:
            print("Saindo...")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()