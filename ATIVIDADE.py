# 1. Classe base Midia
class Midia:
    """
    Representa uma mídia genérica com título e duração.
    """
    def __init__(self, titulo, duracao):
        self.titulo = titulo
        self.duracao = duracao

    def exibir_informacoes(self):
        """
        Imprime o título e a duração da mídia.
        """
        print(f"Título: {self.titulo}, Duração: {self.duracao} minutos")

# 2. Subclasse Video
class Video(Midia):
    """
    Representa um vídeo, herdando de Midia e adicionando resolução.
    """
    def __init__(self, titulo, duracao, resolucao):
        super().__init__(titulo, duracao)
        self.resolucao = resolucao

    def exibir_informacoes(self):
        """
        Imprime o título, a duração e a resolução do vídeo.
        """
        print(f"Título: {self.titulo}, Duração: {self.duracao} minutos, Resolução: {self.resolucao}")

# 3. Subclasse Audio
class Audio(Midia):
    """
    Representa um áudio, herdando de Midia e adicionando formato.
    """
    def __init__(self, titulo, duracao, formato):
        super().__init__(titulo, duracao)
        self.formato = formato

    def exibir_informacoes(self):
        """
        Imprime o título, a duração e o formato do áudio.
        """
        print(f"Título: {self.titulo}, Duração: {self.duracao} minutos, Formato: {self.formato}")

# 4. Subclasse Foto
class Foto(Midia):
    """
    Representa uma foto, herdando de Midia e adicionando resolução e formato.
    """
    def __init__(self, titulo, duracao, resolucao, formato):
        super().__init__(titulo, duracao)
        self.resolucao = resolucao
        self.formato = formato

    def exibir_informacoes(self):
        """
        Imprime o título, a duração, a resolução e o formato da foto.
        """
        print(f"Título: {self.titulo}, Duração: {self.duracao} minutos, Resolução: {self.resolucao}, Formato: {self.formato}")

# 5. Classe Playlist
class Playlist:
    """
    Representa uma playlist que contém uma lista de objetos Midia.
    """
    def __init__(self, nome):
        self.nome = nome
        self.midias = []

    def adicionar_midia(self, midia):
        """
        Adiciona uma mídia à playlist.
        """
        self.midias.append(midia)
        print(f"'{midia.titulo}' adicionado à playlist '{self.nome}'.")

    def remover_midia(self, titulo):
        """
        Remove uma mídia da playlist pelo título.
        """
        midia_encontrada = None
        for midia in self.midias:
            if midia.titulo == titulo:
                midia_encontrada = midia
                break
        if midia_encontrada:
            self.midias.remove(midia_encontrada)
            print(f"'{titulo}' removido da playlist '{self.nome}'.")
        else:
            print(f"Mídia '{titulo}' não encontrada na playlist '{self.nome}'.")

    def exibir_midias(self):
        """
        Exibe as informações de todas as mídias na playlist.
        """
        if not self.midias:
            print(f"A playlist '{self.nome}' está vazia.")
            return
        print(f"\n--- Mídias na Playlist: {self.nome} ---")
        for midia in self.midias:
            midia.exibir_informacoes()
        print("-------------------------------------")

# 6. Classe Usuario
class Usuario:
    """
    Representa um usuário com nome, ID e uma playlist.
    """
    def __init__(self, nome, id_usuario):
        self.nome = nome
        self.id = id_usuario
        self.playlist = Playlist(f"Playlist de {nome}") # Cada usuário tem sua própria playlist

    def adicionar_midia_a_playlist(self, midia):
        """
        Adiciona uma mídia à playlist do usuário.
        """
        self.playlist.adicionar_midia(midia)

    def remover_midia_da_playlist(self, titulo):
        """
        Remove uma mídia da playlist do usuário pelo título.
        """
        self.playlist.remover_midia(titulo)

    def exibir_playlist_do_usuario(self):
        """
        Exibe a playlist do usuário.
        """
        print(f"\n--- Playlist de {self.nome} (ID: {self.id}) ---")
        self.playlist.exibir_midias()
        print("------------------------------------------")

# 7. Classe Biblioteca
class Biblioteca:
    """
    Representa a biblioteca multimídia principal, gerenciando usuários e suas playlists.
    """
    def __init__(self):
        self.usuarios = {} # Dicionário para armazenar usuários, com ID como chave

    def adicionar_usuario(self, usuario):
        """
        Adiciona um usuário à biblioteca.
        """
        if usuario.id not in self.usuarios:
            self.usuarios[usuario.id] = usuario
            print(f"Usuário '{usuario.nome}' (ID: {usuario.id}) adicionado à biblioteca.")
        else:
            print(f"Erro: Usuário com ID '{usuario.id}' já existe.")

    def remover_usuario(self, id_usuario):
        """
        Remove um usuário da biblioteca pelo ID.
        """
        if id_usuario in self.usuarios:
            nome_usuario = self.usuarios[id_usuario].nome
            del self.usuarios[id_usuario]
            print(f"Usuário '{nome_usuario}' (ID: {id_usuario}) removido da biblioteca.")
        else:
            print(f"Erro: Usuário com ID '{id_usuario}' não encontrado.")

    def listar_usuarios(self):
        """
        Lista todos os usuários na biblioteca.
        """
        if not self.usuarios:
            print("Nenhum usuário cadastrado na biblioteca.")
            return
        print("\n--- Usuários na Biblioteca ---")
        for id_usuario, usuario in self.usuarios.items():
            print(f"Nome: {usuario.nome}, ID: {usuario.id}")
        print("------------------------------")

    def gerenciar_playlist_do_usuario(self, id_usuario):
        """
        Permite gerenciar a playlist de um usuário específico.
        """
        if id_usuario in self.usuarios:
            usuario = self.usuarios[id_usuario]
            print(f"\nGerenciando playlist de {usuario.nome}:")
            usuario.exibir_playlist_do_usuario()
        else:
            print(f"Erro: Usuário com ID '{id_usuario}' não encontrado.")

# --- Exemplo de Uso ---
if __name__ == "__main__":
    # Criando instâncias de mídias
    filme1 = Video("O Senhor dos Anéis", 178, "1080p")
    musica1 = Audio("Bohemian Rhapsody", 6, "MP3")
    foto1 = Foto("Por do Sol na Praia", 2, "4K", "JPEG")
    filme2 = Video("Interestelar", 169, "4K")
    musica2 = Audio("Stairway to Heaven", 8, "FLAC")

    # Exibindo informações das mídias
    print("--- Informações das Mídias Criadas ---")
    filme1.exibir_informacoes()
    musica1.exibir_informacoes()
    foto1.exibir_informacoes()
    filme2.exibir_informacoes()
    musica2.exibir_informacoes()

    # Criando usuários
    usuario1 = Usuario("Alice", "user001")
    usuario2 = Usuario("Bob", "user002")

    # Criando a biblioteca
    minha_biblioteca = Biblioteca()

    # Adicionando usuários à biblioteca
    minha_biblioteca.adicionar_usuario(usuario1)
    minha_biblioteca.adicionar_usuario(usuario2)
    minha_biblioteca.adicionar_usuario(Usuario("Alice", "user001")) # Tentando adicionar usuário duplicado

    # Listando usuários
    minha_biblioteca.listar_usuarios()

    # Adicionando mídias às playlists dos usuários
    usuario1.adicionar_midia_a_playlist(filme1)
    usuario1.adicionar_midia_a_playlist(musica1)
    usuario1.adicionar_midia_a_playlist(foto1)

    usuario2.adicionar_midia_a_playlist(filme2)
    usuario2.adicionar_midia_a_playlist(musica2)

    # Exibindo playlists dos usuários
    usuario1.exibir_playlist_do_usuario()
    usuario2.exibir_playlist_do_usuario()

    # Removendo uma mídia da playlist de um usuário
    usuario1.remover_midia_da_playlist("Bohemian Rhapsody")
    usuario1.exibir_playlist_do_usuario()

    # Tentando remover mídia inexistente
    usuario1.remover_midia_da_playlist("Música Inexistente")

    # Removendo um usuário da biblioteca
    minha_biblioteca.remover_usuario("user001")
    minha_biblioteca.listar_usuarios()

    # Tentando gerenciar playlist de usuário removido
    minha_biblioteca.gerenciar_playlist_do_usuario("user001")

    # Gerenciando playlist de um usuário existente
    minha_biblioteca.gerenciar_playlist_do_usuario("user002")

