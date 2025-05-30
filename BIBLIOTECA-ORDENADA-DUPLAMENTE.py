from datetime import datetime, timedelta

class Livro:
    def __init__(self, id, nome, data_devolucao=None):
        self.id = id
        self.nome = nome
        self.data_devolucao = data_devolucao
        self.proximo = None
        self.anterior = None

    def __str__(self):
        return f"ID: {self.id}, Nome: {self.nome}, Data de Devolução: {self.data_devolucao}"

class Acervo:
    def __init__(self):
        self.head = None
        self.tail = None
        self.inicializar_acervo()

    def inicializar_acervo(self):
        livros_iniciais = [
            ("1", "Livro A"),
            ("2", "Livro B"),
            ("3", "Livro C"),
            ("4", "Livro D"),
            ("5", "Livro E"),
            ("6", "Livro F"),
            ("7", "Livro G"),
            ("8", "Livro H"),
            ("9", "Livro I"),
            ("10", "Livro J")
        ]

        anterior = None
        for id, nome in livros_iniciais:
            novo_livro = Livro(id, nome)
            if self.head is None:
                self.head = novo_livro
            else:
                anterior.proximo = novo_livro
                novo_livro.anterior = anterior
            anterior = novo_livro
        self.tail = anterior

    def adicionar_livro(self, id, nome):
        novo_livro = Livro(id, nome)
        if not self.head:
            self.head = novo_livro
            return
        self.tail.proximo = novo_livro
        novo_livro.anterior = self.tail
        self.tail = novo_livro

    def remover_livro(self, id):
        atual = self.head
        while atual and atual.id != id:
            atual = atual.proximo
        if atual is None:
            print("Livro não encontrado.")
            return
        if atual.anterior:
            atual.anterior.proximo = atual.proximo
        if atual.proximo:
            atual.proximo.anterior = atual.anterior
        if atual == self.head:
            self.head = atual.proximo
        if atual == self.tail:
            self.tail = atual.anterior
        print(f"Livro com ID {id} removido.")

    def primeiro_livro(self):
        return self.head

    def exibir_acervo(self):
        atual = self.head
        while atual:
            print(atual)
            atual = atual.proximo

    def procurar_livro_por_id(self, id):
        head_atual = self.head
        tail_atual = self.tail
        
        while head_atual and tail_atual and head_atual != tail_atual and head_atual.proximo != tail_atual:
            if head_atual.id == id:
                print("Livro encontrado (a partir do head):")
                print(head_atual)
                if head_atual.proximo:
                    print("Próximo livro na lista:")
                    print(head_atual.proximo)
                else:
                    print("Este é o último livro na lista.")
                return
            if tail_atual.id == id:
                print("Livro encontrado (a partir do tail):")
                print(tail_atual)
                if tail_atual.proximo:
                    print("Próximo livro na lista:")
                    print(tail_atual.proximo)
                else:
                    print("Este é o último livro na lista.")
                return
            
            head_atual = head_atual.proximo
            tail_atual = tail_atual.anterior

        print("Livro não encontrado.")

    def alugar_livro(self, id, dias_para_devolucao):
        atual = self.head
        while atual:
            if atual.id == id:
                data_devolucao = datetime.now() + timedelta(days=dias_para_devolucao)
                atual.data_devolucao = data_devolucao.strftime("%d/%m/%Y")
                print(f"Livro '{atual.nome}' alugado até {atual.data_devolucao}")
                return
            atual = atual.proximo
        print("Livro não encontrado.")

    def alugar_livro(self, id, dias_para_devolucao):
        atual = self.head
        while atual:
            if atual.id == id:
                data_devolucao = datetime.now() + timedelta(days=dias_para_devolucao)
                atual.data_devolucao = data_devolucao.strftime("%d/%m/%Y")
                print(f"Livro '{atual.nome}' alugado até {atual.data_devolucao}")
                return
            atual = atual.proximo
        print("Livro não encontrado.")

class Usuario:
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome
        self.proximo = None
        self.anterior = None

    def __str__(self):
        return f"ID: {self.id}, Nome: {self.nome}"

class Biblioteca:
    def __init__(self):
        self.usuarios_head = None
        self.usuarios_tail = None
        self.acervo = Acervo()
        self.inicializar_usuarios()

    def inicializar_usuarios(self):
        usuarios_iniciais = [
            ("1", "Daniel"),
            ("2", "Violeta"),
            ("3", "Francisco")
        ]

        anterior = None
        for id, nome in usuarios_iniciais:
            novo_usuario = Usuario(id, nome)
            if self.usuarios_head is None:
                self.usuarios_head = novo_usuario
            else:
                anterior.proximo = novo_usuario
                novo_usuario.anterior = anterior
            anterior = novo_usuario
        self.usuarios_tail = anterior

    def adicionar_usuario(self, id, nome):
        novo_usuario = Usuario(id, nome)
        if not self.usuarios_head:
            self.usuarios_head = novo_usuario
            self.usuarios_tail = novo_usuario
            return
        self.usuarios_tail.proximo = novo_usuario
        novo_usuario.anterior = self.usuarios_tail
        self.usuarios_tail = novo_usuario

    def remover_usuario(self, id):
        atual = self.usuarios_head
        while atual and atual.id != id:
            atual = atual.proximo
        if atual is None:
            print("Usuário não encontrado.")
            return
        if atual.anterior:
            atual.anterior.proximo = atual.proximo
        if atual.proximo:
            atual.proximo.anterior = atual.anterior
        if atual == self.usuarios_head:
            self.usuarios_head = atual.proximo
        if atual == self.usuarios_tail:
            self.usuarios_tail = atual.anterior
        print(f"Usuário com ID {id} removido.")

    def listar_usuarios(self):
        atual = self.usuarios_head
        while atual:
            print(atual)
            atual = atual.proximo

    def procurar_usuario_por_id(self, id):
        atual = self.usuarios_head
        while atual:
            if atual.id == id:
                return atual
            atual = atual.proximo
        return None
    
    def ordenar_usuarios(self):
        if self.usuarios_head is None or self.usuarios_head.proximo is None:
            return

        trocou = True
        while trocou:
            trocou = False
            atual = self.usuarios_head
            while atual.proximo:
                if int(atual.id) > int(atual.proximo.id):
                    # Troca os valores entre os nós
                    atual.id, atual.proximo.id = atual.proximo.id, atual.id
                    atual.nome, atual.proximo.nome = atual.proximo.nome, atual.nome
                    trocou = True
                atual = atual.proximo


def main():
    biblioteca = Biblioteca()

    while True:
        print("\nGerenciamento de Biblioteca")
        print("1. Listar todos os usuários")
        print("2. Adicionar usuário")
        print("3. Remover usuário")
        print("4. Selecionar usuário e gerenciar acervo")
        print("5. Ordenar usuários por ID")
        print("6. Sair")

        escolha = int(input("Digite sua escolha: "))

        if escolha == 1:
            print("\nLista de todos os usuários:")
            biblioteca.listar_usuarios()
        elif escolha == 2:
            id = input("Digite o ID do usuário: ")
            nome = input("Digite o nome do usuário: ")
            biblioteca.adicionar_usuario(id, nome)
            print("Usuário adicionado com sucesso.")
        elif escolha == 3:
            id = input("Digite o ID do usuário a ser removido: ")
            biblioteca.remover_usuario(id)
        elif escolha == 4:
            id = input("Digite o ID do usuário: ")
            usuario = biblioteca.procurar_usuario_por_id(id)
            if usuario:
                while True:
                    print("\nGerenciamento de Acervo")
                    print("1. Listar todos os livros")
                    print("2. Exibir primeiro livro da vitrine")
                    print("3. Adicionar livro")
                    print("4. Remover livro")
                    print("5. Procurar livro por ID")
                    print("6. Alugar livro")
                    print("7. Voltar")

                    escolha_acervo = int(input("Digite sua escolha: "))

                    if escolha_acervo == 1:
                        print("\nLista de todos os livros no acervo:")
                        biblioteca.acervo.exibir_acervo()
                    elif escolha_acervo == 2:
                        print("\nPrimeiro livro da vitrine (head da lista):")
                        print(biblioteca.acervo.primeiro_livro())
                    elif escolha_acervo == 3:
                        id_livro = input("Digite o ID do livro: ")
                        nome_livro = input("Digite o nome do livro: ")
                        biblioteca.acervo.adicionar_livro(id_livro, nome_livro)
                        print("Livro adicionado com sucesso.")
                    elif escolha_acervo == 4:
                        id_livro = input("Digite o ID do livro a ser removido: ")
                        biblioteca.acervo.remover_livro(id_livro)
                    elif escolha_acervo == 5:
                        id_livro = input("Digite o ID do livro a ser procurado: ")
                        biblioteca.acervo.procurar_livro_por_id(id_livro)
                    elif escolha_acervo == 6:
                        id_livro = input("Digite o ID do livro a ser alugado: ")
                        dias_para_devolucao = int(input("Digite o número de dias para devolução: "))
                        biblioteca.acervo.alugar_livro(id_livro, dias_para_devolucao)
                    elif escolha_acervo == 7:
                        break
                    else:
                        print("Opção inválida! Tente novamente.")
            else:
                print("Usuário não encontrado.")
        elif escolha == 5:
            biblioteca.ordenar_usuarios()
            print("Usuários ordenados com sucesso.")
        elif escolha == 6:
            print("Saindo...")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()