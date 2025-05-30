from datetime import datetime, timedelta

class Livro:
    def __init__(self, id, nome, data_devolucao=None):
        self.id = id
        self.nome = nome
        self.data_devolucao = data_devolucao
        self.proximo = None

    def __str__(self):
        return f"ID: {self.id}, Nome: {self.nome}, Data de Devolução: {self.data_devolucao}"

class Acervo:
    def __init__(self):
        self.head = None
        self.tail = None  
        self.inicializar_acervo()

    def inicializar_acervo(self):
        livros_iniciais = [
            ("1", "Livro A"), ("2", "Livro B"), ("3", "Livro C"),
            ("4", "Livro D"), ("5", "Livro E"), ("6", "Livro F"),
            ("7", "Livro G"), ("8", "Livro H"), ("9", "Livro I"),
            ("10", "Livro J")
        ]
        for id, nome in livros_iniciais:
            self.adicionar_livro(id, nome)

    def adicionar_livro(self, id, nome):
        novo_livro = Livro(id, nome)
        if not self.head:
            self.head = self.tail = novo_livro
        else:
            self.tail.proximo = novo_livro
            self.tail = novo_livro

    def remover_livro(self, id):
        atual = self.head
        anterior = None
        while atual and atual.id != id:
            anterior = atual
            atual = atual.proximo
        if not atual:
            print("Livro não encontrado.")
            return
        if anterior:
            anterior.proximo = atual.proximo
            if atual == self.tail:
                self.tail = anterior
        else:
            self.head = atual.proximo
            if atual == self.tail:
                self.tail = None
        print(f"Livro com ID {id} removido.")

    def primeiro_livro(self):
        return self.head

    def exibir_acervo(self):
        atual = self.head
        while atual:
            print(atual)
            atual = atual.proximo

    def procurar_livro_por_id(self, id):
        atual = self.head
        while atual:
            if atual.id == id:
                print("Livro encontrado:")
                print(atual)
                if atual.proximo:
                    print("Próximo livro na lista:")
                    print(atual.proximo)
                else:
                    print("Este é o último livro da lista.")
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

    def __str__(self):
        return f"ID: {self.id}, Nome: {self.nome}"

class Biblioteca:
    def __init__(self):
        self.usuarios_head = None
        self.acervo = Acervo()
        self.inicializar_usuarios()

    def inicializar_usuarios(self):
        usuarios_iniciais = [
            ("1", "Daniel"),
            ("2", "Violeta"),
            ("3", "Francisco")
        ]

        for id, nome in usuarios_iniciais:
            self.adicionar_usuario(id, nome)

    def adicionar_usuario(self, id, nome):
        novo_usuario = Usuario(id, nome)
        if not self.usuarios_head:
            self.usuarios_head = novo_usuario
            return
        atual = self.usuarios_head
        while atual.proximo:
            atual = atual.proximo
        atual.proximo = novo_usuario

    def remover_usuario(self, id):
        atual = self.usuarios_head
        anterior = None
        while atual and atual.id != id:
            anterior = atual
            atual = atual.proximo
        if not atual:
            print("Usuário não encontrado.")
            return
        if anterior:
            anterior.proximo = atual.proximo
        else:
            self.usuarios_head = atual.proximo
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

def main():
    biblioteca = Biblioteca()

    while True:
        print("\nGerenciamento de Biblioteca")
        print("1. Listar todos os usuários")
        print("2. Adicionar usuário")
        print("3. Remover usuário")
        print("4. Selecionar usuário e gerenciar acervo")
        print("5. Sair")

        escolha = int(input("Digite sua escolha: "))

        if escolha == 1:
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
                    print("1. Listar livros")
                    print("2. Exibir primeiro livro")
                    print("3. Adicionar livro")
                    print("4. Remover livro")
                    print("5. Procurar livro por ID")
                    print("6. Alugar livro")
                    print("7. Voltar")
                    escolha_acervo = int(input("Escolha: "))

                    if escolha_acervo == 1:
                        biblioteca.acervo.exibir_acervo()
                    elif escolha_acervo == 2:
                        print(biblioteca.acervo.primeiro_livro())
                    elif escolha_acervo == 3:
                        id_livro = input("ID do livro: ")
                        nome_livro = input("Nome do livro: ")
                        biblioteca.acervo.adicionar_livro(id_livro, nome_livro)
                    elif escolha_acervo == 4:
                        id_livro = input("ID do livro a remover: ")
                        biblioteca.acervo.remover_livro(id_livro)
                    elif escolha_acervo == 5:
                        id_livro = input("ID do livro: ")
                        biblioteca.acervo.procurar_livro_por_id(id_livro)
                    elif escolha_acervo == 6:
                        id_livro = input("ID do livro: ")
                        dias = int(input("Dias para devolução: "))
                        biblioteca.acervo.alugar_livro(id_livro, dias)
                    elif escolha_acervo == 7:
                        break
                    else:
                        print("Opção inválida!")
            else:
                print("Usuário não encontrado.")
        elif escolha == 5:
            print("Saindo...")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()