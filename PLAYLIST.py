class Musica: 
    """Classe que representa uma música na playlist."""
    def __init__(self, dados_musica): 
        self.dados_musica = dados_musica
        self.proximo = None 
        self.anterior = None 

    def __str__(self): 
        """Retorna uma representação em string da música."""
        return str(self.dados_musica) 
        
    
class PlaylistDupla: 
    """Classe que representa uma playlist de músicas."""
    def __init__(self): 
        self.cabeca = None 
        self.cauda = None 

    def adicionar_musica_no_final_duplo(self, dados_musica): 
        """Adiciona uma música no final da playlist."""
        novo_no_musical = Musica(dados_musica) 

        if not self.cabeca:  
            
            self.cabeca = novo_no_musical
            self.cauda = novo_no_musical
            print(f"'{dados_musica}' adicionada. A playlist tem sua primeira música! 🎉")
        else:
            
            self.cauda.proximo = novo_no_musical  
            novo_no_musical.anterior = self.cauda 
            self.cauda = novo_no_musical          
            print(f"'{dados_musica}' entrou no final da playlist. Que venha o próximo hit! 🎧")

    def adicionar_musica_no_inicio_duplo(self, dados_musica):
        """Adiciona uma música no início da playlist."""
        novo_no_musical = Musica(dados_musica)

        if not self.cabeca:  # Se a playlist estiver mais deserta que o Saara 🏜️
            # Mesma lógica de adicionar no final quando vazia: o novo nó é tudo!
            self.cabeca = novo_no_musical
            self.cauda = novo_no_musical
            print(f"'{dados_musica}' adicionada como a primeiríssima! Que honra! 🥇")
        else:
            # Se já tem alguém na liderança, o novo nó assume o posto!
            novo_no_musical.proximo = self.cabeca  # O novo nó aponta para a antiga cabeça
            self.cabeca.anterior = novo_no_musical # A antiga cabeça aponta de volta para o novo nó
            self.cabeca = novo_no_musical          # E o novo nó é coroado como a nova cabeça! 👑
            print(f"'{dados_musica}' assumiu a liderança da playlist! 🌟")

    def buscar_musica_duplo(self, dados_musica_procurada):
        """Busca uma música na playlist e retorna o nó se encontrar, ou None."""
        if not self.cabeca:
            # Se não tem nem cabeça, não tem nem como começar a procurar... 🤷
            # print("Playlist vazia, nada para buscar aqui!") # Opcional: mensagem de feedback
            return None

        atual = self.cabeca
        posicao = 1 # Opcional: para saber a posição
        while atual:
            if atual.dados_musica == dados_musica_procurada:
                # EUREKA! Achamos! Eureka!
                # print(f"'{dados_musica_procurada}' encontrada na posição {posicao}!") # Opcional
                return atual  # Retorna o nó inteiro, assim temos acesso a tudo dele
            atual = atual.proximo
            posicao += 1

        # Se o loop terminou e não achamos nada, a música não está na playlist 😥
        # print(f"'{dados_musica_procurada}' não encontrada na playlist.") # Opcional
        return None

    def remover_musica_duplo(self, dados_musica_remover):
        """Remove uma música da playlist."""
        no_para_remover = self.buscar_musica_duplo(dados_musica_remover)

        if not no_para_remover:
            print(f"'{dados_musica_remover}' não encontrada. Nada para remover. Ufa! 😮‍💨")
            return False # Indica que a remoção falhou

        # Caso 1: O nó a ser removido é o único nó na lista
        if no_para_remover == self.cabeca and no_para_remover == self.cauda:
            self.cabeca = None
            self.cauda = None
            print(f"'{dados_musica_remover}' removida. A playlist ficou mais vazia que cinema em dia de estreia de filme cult! 텅~")
            return True

        # Caso 2: O nó a ser removido é a cabeça da lista (mas não o único)
        elif no_para_remover == self.cabeca:
            self.cabeca = no_para_remover.proximo # A nova cabeça é o próximo do nó removido
            self.cabeca.anterior = None # A nova cabeça não tem anterior
            print(f"'{dados_musica_remover}' (antiga cabeça) removida. Nova música no comando! 🚀")
            return True

        # Caso 3: O nó a ser removido é a cauda da lista (mas não o único)
        elif no_para_remover == self.cauda:
            self.cauda = no_para_remover.anterior # A nova cauda é o anterior do nó removido
            self.cauda.proximo = None # A nova cauda não tem próximo
            print(f"'{dados_musica_remover}' (antiga cauda) removida. A festa acabou mais cedo para ela! 😢")
            return True

        # Caso 4: O nó a ser removido está no meio da lista
        else:
            no_anterior = no_para_remover.anterior
            no_proximo = no_para_remover.proximo

            no_anterior.proximo = no_proximo # O anterior ao removido agora aponta para o próximo do removido
            no_proximo.anterior = no_anterior # O próximo ao removido agora aponta para o anterior do removido
            print(f"'{dados_musica_remover}' removida do meio da playlist. A vida segue! 🚶‍♀️🚶‍♂️")
            return True

        # Limpar ponteiros do nó removido (boa prática, mas opcional se o nó não for mais usado)
        # no_para_remover.proximo = None
        # no_para_remover.anterior = None
        # Não é estritamente necessário aqui se o Python garbage collector cuidar dele.

    def mostrar_playlist_frente(self):
        """Mostra todas as músicas da playlist, da primeira à última."""
        if not self.cabeca:
            print("A playlist está mais vazia que show de stand-up em velório...")
            return

        print("\n🎶 Sua Playlist (do início ao fim):")
        atual = self.cabeca
        contador = 1
        while atual:
            print(f"  {contador}. {atual.dados_musica}")
            atual = atual.proximo
            contador += 1
        if contador == 1: # Só entrou no loop se não for None, mas se só tiver 1 item, o contador será 2.
             # Esta condição é redundante se a primeira checagem 'if not self.cabeca' for feita.
             # Mas vamos manter para clareza caso a lógica mude.
             pass # A mensagem de vazia já foi tratada.

    def mostrar_playlist_tras(self):
        """Mostra todas as músicas da playlist, da última à primeira."""
        if not self.cauda: # Se não tem cauda, não tem cabeça, está vazia!
            print("A playlist está tão vazia que dá pra ouvir o eco...")
            return

        print("\n🎶 Sua Playlist (do fim ao início - Rebobinando! ⏪):")
        atual = self.cauda
        contador = 1
        while atual:
            print(f"  {contador}. {atual.dados_musica}")
            atual = atual.anterior
            contador += 1

    def __str__(self): 
        """Retorna uma representação em string da playlist."""
        if not self.cabeca: 
            # Se a cabeça for None, a playlist está vazia como um teatro depois que alguém gritou "FOGO!" 🏃‍♂️💨
            # Essa linha retorna uma mensagem engraçada quando a playlist está vazia
            return "A playlist está mais vazia que meu bolso no fim do mês! 💸"
        # Caso contrário, temos ao menos uma música - é como ter pelo menos um amigo na festa 🎉
        return "Playlist com músicas (detalhes em breve!)" 
    
if __name__ == '__main__':
    # 🚀 MODO PILOTO AUTOMÁTICO ATIVADO! 🚀
    # Esta condição é como um detector de "Quem está me chamando?"
    # Se você rodar o arquivo diretamente (python PLAYLIST.py), essa parte roda
    # Se importar como módulo (import PLAYLIST), essa parte fica quietinha
    # Exemplo: É como sua campainha - só toca quando alguém aperta o botão diretamente!
    
    print("🎶 Bem-vindo ao Testador de Playlists Duplamente Encadeadas! 🎶")
    print("    Prepare-se para ver ponteiros dançando como se não houvesse amanhã! 🕺💃")

    # --- Bloco 1: O Nascimento da Playlist Vazia ---
    # 👶 FASE EMBRIONÁRIA DA PLAYLIST 👶
    # Aqui estamos criando uma playlist vazia, como um caderno novo sem nenhuma anotação
    # É tipo uma TV ligada num canal fora do ar - só estática e potencial!
    print("\n--- Bloco 1: Criando a playlist (Ela nasce pelada e sem músicas!) ---")
    playlist_show = PlaylistDupla() # Instanciamos nossa playlist - é como montar o palco antes do show!
    print("\n--- Playlist Inicialmente (Ecoando no vazio...) ---")
    playlist_show.mostrar_playlist_frente() # Chamamos o método que mostra a playlist - mas é como olhar para um deserto 🏜️

    # --- Bloco 2: Contratando a Banda (Adicionando Músicas) ---
    # 🎸 FASE DE RECRUTAMENTO: TRAZENDO OS ARTISTAS! 🎸
    # Agora começamos a adicionar músicas na nossa playlist, como quem coloca ingredientes numa receita
    # Cada música é como um passageiro entrando no trem da festa! 🚂🎉
    # Exemplo: Imagine uma fila para montanha-russa - alguns entram pela fila normal (final),
    # outros são VIPs e furam a fila (início)!
    print("\n--- Bloco 2: Adicionando Músicas (Montando o line-up do festival!) ---")
    
    # Adicionando "Bohemian Rhapsody" no final. Clássico é clássico, né? Entra por último pra fechar com chave de ouro (por enquanto).
    playlist_show.adicionar_musica_no_final_duplo("Bohemian Rhapsody - Queen")
    
    # "Imagine" chega de penetra e fura a fila, entrando no início. Paz e amor, mas primeiro eu! ✌️🥇
    playlist_show.adicionar_musica_no_inicio_duplo("Imagine - John Lennon")
    
    # "Stairway to Heaven" chega atrasado, mas garante seu lugar no final. A escada pro céu pode esperar um pouquinho. ☁️🚶‍♂️
    playlist_show.adicionar_musica_no_final_duplo("Stairway to Heaven - Led Zeppelin")
    
    # "Smells Like Teen Spirit" chega chutando a porta e vai direto pro início. A rebeldia adolescente não espera! 🎸🔥
    playlist_show.adicionar_musica_no_inicio_duplo("Smells Like Teen Spirit - Nirvana")
    
    # "Like a Rolling Stone" chega rolando e para no final. Como uma pedra que rola, sabe como é... 🗿🎶
    playlist_show.adicionar_musica_no_final_duplo("Like a Rolling Stone - Bob Dylan")
    
    # Comentário da ordem esperada:
    # Depois dessa bagunça de gente entrando por tudo que é lado, a fila deve estar assim:
    # 1. Nirvana (Entrou por último no início)
    # 2. Imagine (Entrou antes do Nirvana no início)
    # 3. Queen (Primeiro a entrar no final)
    # 4. Led Zeppelin (Entrou depois do Queen no final)
    # 5. Bob Dylan (Entrou por último no final)
    # Ordem esperada: Nirvana, Imagine, Queen, Led Zeppelin, Bob Dylan

    print("\n--- Playlist Após Adições (Agora temos um show de verdade!) ---")
    # Mostrando a playlist do início ao fim. É o "setlist oficial".
    playlist_show.mostrar_playlist_frente()
    # Mostrando de trás pra frente. "DJ, SOLTA O REVERSE! ⏪" Pra ver se os ponteiros 'anterior' estão espertos.
    playlist_show.mostrar_playlist_tras()

    # --- Bloco 3: Detetives Musicais em Ação (Buscando Músicas) ---
    # "Sherlock Holmes, temos um caso! A música X está na playlist?" 🕵️‍♂️🎶
    print("\n--- Bloco 3: Buscando Músicas (Onde está Wally... digo, a música?) ---")
    musicas_a_procurar = ["Imagine - John Lennon", "Hotel California - Eagles", "Bohemian Rhapsody - Queen"]
    for musica_titulo_procurado in musicas_a_procurar: # Para cada música na nossa lista de "procurados da justiça musical"
        # Chamamos nosso detetive particular, o método buscar_musica_duplo.
        no_encontrado = playlist_show.buscar_musica_duplo(musica_titulo_procurado)
        if no_encontrado: # Se o detetive voltou com algo além de poeira nos bolsos...
            print(f"✅ Encontrada: '{no_encontrado.dados_musica}'! Estava escondida, a danadinha!")
            # Vamos dar uma espiada nos vizinhos pra ver se ela não está causando problemas.
            if no_encontrado.anterior: print(f"   ⬅️ Quem vem antes dela na fila: {no_encontrado.anterior.dados_musica}")
            if no_encontrado.proximo: print(f"   ➡️ Quem vem depois dela na fila: {no_encontrado.proximo.dados_musica}")
        else: # Se o detetive voltou de mãos abanando...
            print(f"❌ Não encontrada: '{musica_titulo_procurado}'. Deve ter ido dar uma volta... ou nunca esteve aqui. 🤷")

    # --- Bloco 4: A Faxina Musical (Removendo Músicas) ---
    # Algumas músicas não passaram no teste de popularidade. Hora da eliminação! 👢🎶
    # É tipo o "Big Brother" das músicas, só que aqui a gente que manda sair.
    print("\n--- Bloco 4: Removendo Músicas (Aquele momento tenso da faxina!) ---")
    # Relembrando a ordem antes da degola: Nirvana, Imagine, Queen, Led Zeppelin, Bob Dylan

    print("\nRemovendo 'Bohemian Rhapsody - Queen' (estava ali no meio, coitada):")
    playlist_show.remover_musica_duplo("Bohemian Rhapsody - Queen") # Adeus, Queen! Foi bom enquanto durou.
    playlist_show.mostrar_playlist_frente() # Como ficou a fila depois da saída dela?
    # Esperado: Nirvana, Imagine, Led Zeppelin, Bob Dylan (O Led Zeppelin virou vizinho do Imagine)

    print("\nRemovendo 'Smells Like Teen Spirit - Nirvana' (era a primeira da fila, a líder da banda):")
    playlist_show.remover_musica_duplo("Smells Like Teen Spirit - Nirvana") # Nirvana se foi, deixando Imagine na liderança.
    playlist_show.mostrar_playlist_frente()
    # Esperado: Imagine, Led Zeppelin, Bob Dylan

    print("\nRemovendo 'Like a Rolling Stone - Bob Dylan' (a última, fechando a porta ao sair):")
    playlist_show.remover_musica_duplo("Like a Rolling Stone - Bob Dylan") # Bob Dylan rolou pra fora da playlist.
    playlist_show.mostrar_playlist_frente()
    # Esperado: Imagine, Led Zeppelin (Só sobraram os veteranos)

    print("\nTentando remover música inexistente ('Hey Jude' - acho que ela está em outra festa):")
    playlist_show.remover_musica_duplo("Hey Jude - The Beatles") # Não vai acontecer nada, porque ela nem aqui está.
    # É como tentar demitir alguém que não trabalha na sua empresa. 😂

    print("\nRemovendo as restantes para esvaziar (limpando o palco geral!):")
    playlist_show.remover_musica_duplo("Imagine - John Lennon") # Adeus, paz e amor!
    playlist_show.remover_musica_duplo("Stairway to Heaven - Led Zeppelin") # A escada pro céu foi desmontada.
    playlist_show.mostrar_playlist_frente() # Playlist vazia de novo. "Cabô o show, pessoal!"

    # --- Bloco 5: Teste do Sobrevivente Solitário (Remover Único Elemento) ---
    # O que acontece se só tem UMA música e a gente remove ela? Drama! 😱
    print("\n--- Bloco 5: Teste Rápido - O Destino do 'One Hit Wonder' ---")
    playlist_unica = PlaylistDupla() # Nova playlist, novinha em folha.
    playlist_unica.adicionar_musica_no_final_duplo("One - U2") # Só uma música, a "One". Que apropriado.
    playlist_unica.mostrar_playlist_frente() # "Olha eu aqui, sozinho!"
    print("Removendo 'One - U2' (o único sobrevivente):")
    playlist_unica.remover_musica_duplo("One - U2") # E então, não havia mais nenhum...
    playlist_unica.mostrar_playlist_frente() # Vazio. Silêncio. Fim. 🎬

    print("\n🎉 Testes Concluídos! Se não explodiu nada e a ordem das músicas fez sentido,")
    print("   Sua playlist é oficialmente mais estável que minha última dieta! SUCESSO! 🎉")
    print("   Pode comemorar com sua música favorita (que não foi removida acidentalmente, espero!) 🥳")
