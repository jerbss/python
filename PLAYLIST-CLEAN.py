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

        if not self.cabeca:  
            self.cabeca = novo_no_musical
            self.cauda = novo_no_musical
            print(f"'{dados_musica}' adicionada como a primeiríssima! Que honra! 🥇")
        else:
            novo_no_musical.proximo = self.cabeca  
            self.cabeca.anterior = novo_no_musical 
            self.cabeca = novo_no_musical          
            print(f"'{dados_musica}' assumiu a liderança da playlist! 🌟")

    def buscar_musica_duplo(self, dados_musica_procurada):
        """Busca uma música na playlist e retorna o nó se encontrar, ou None."""
        if not self.cabeca:
            return None

        atual = self.cabeca
        posicao = 1 
        while atual:
            if atual.dados_musica == dados_musica_procurada:
                return atual
            atual = atual.proximo
            posicao += 1

        
        
        return None

    def remover_musica_duplo(self, dados_musica_remover):
        """Remove uma música da playlist."""
        no_para_remover = self.buscar_musica_duplo(dados_musica_remover)

        if not no_para_remover:
            print(f"'{dados_musica_remover}' não encontrada. Nada para remover. Ufa! 😮‍💨")
            return False 

        
        if no_para_remover == self.cabeca and no_para_remover == self.cauda:
            self.cabeca = None
            self.cauda = None
            print(f"'{dados_musica_remover}' removida. A playlist ficou mais vazia que cinema em dia de estreia de filme cult! 텅~")
            return True

        
        elif no_para_remover == self.cabeca:
            self.cabeca = no_para_remover.proximo 
            self.cabeca.anterior = None 
            print(f"'{dados_musica_remover}' (antiga cabeça) removida. Nova música no comando! 🚀")
            return True

        
        elif no_para_remover == self.cauda:
            self.cauda = no_para_remover.anterior 
            self.cauda.proximo = None 
            print(f"'{dados_musica_remover}' (antiga cauda) removida. A festa acabou mais cedo para ela! 😢")
            return True

        
        else:
            no_anterior = no_para_remover.anterior
            no_proximo = no_para_remover.proximo

            no_anterior.proximo = no_proximo 
            no_proximo.anterior = no_anterior 
            print(f"'{dados_musica_remover}' removida do meio da playlist. A vida segue! 🚶‍♀️🚶‍♂️")
            return True

        
        
        
        

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
        if contador == 1: 
             
             
             pass 

    def mostrar_playlist_tras(self):
        """Mostra todas as músicas da playlist, da última à primeira."""
        if not self.cauda: 
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
            
            
            return "A playlist está mais vazia que meu bolso no fim do mês! 💸"
        
        return "Playlist com músicas (detalhes em breve!)" 
    
if __name__ == '__main__':
    
    
    
    
    
    
    print("🎶 Bem-vindo ao Testador de Playlists Duplamente Encadeadas! 🎶")
    print("    Prepare-se para ver ponteiros dançando como se não houvesse amanhã! 🕺💃")

    
    
    
    
    print("\n--- Bloco 1: Criando a playlist (Ela nasce pelada e sem músicas!) ---")
    playlist_show = PlaylistDupla() 
    print("\n--- Playlist Inicialmente (Ecoando no vazio...) ---")
    playlist_show.mostrar_playlist_frente() 

    print("\n--- Bloco 2: Adicionando Músicas (Montando o line-up do festival!) ---")
    
    
    playlist_show.adicionar_musica_no_final_duplo("Bohemian Rhapsody - Queen")
    
    
    playlist_show.adicionar_musica_no_inicio_duplo("Imagine - John Lennon")
    
    
    playlist_show.adicionar_musica_no_final_duplo("Stairway to Heaven - Led Zeppelin")
    
    
    playlist_show.adicionar_musica_no_inicio_duplo("Smells Like Teen Spirit - Nirvana")
    
    
    playlist_show.adicionar_musica_no_final_duplo("Like a Rolling Stone - Bob Dylan")
    
    
    
    
    
    
    
    
    

    print("\n--- Playlist Após Adições (Agora temos um show de verdade!) ---")
    
    playlist_show.mostrar_playlist_frente()
    
    playlist_show.mostrar_playlist_tras()

    
    
    print("\n--- Bloco 3: Buscando Músicas (Onde está Wally... digo, a música?) ---")
    musicas_a_procurar = ["Imagine - John Lennon", "Hotel California - Eagles", "Bohemian Rhapsody - Queen"]
    for musica_titulo_procurado in musicas_a_procurar: 
        
        no_encontrado = playlist_show.buscar_musica_duplo(musica_titulo_procurado)
        if no_encontrado: 
            print(f"✅ Encontrada: '{no_encontrado.dados_musica}'! Estava escondida, a danadinha!")
            
            if no_encontrado.anterior: print(f"   ⬅️ Quem vem antes dela na fila: {no_encontrado.anterior.dados_musica}")
            if no_encontrado.proximo: print(f"   ➡️ Quem vem depois dela na fila: {no_encontrado.proximo.dados_musica}")
        else: 
            print(f"❌ Não encontrada: '{musica_titulo_procurado}'. Deve ter ido dar uma volta... ou nunca esteve aqui. 🤷")

    
    
    
    print("\n--- Bloco 4: Removendo Músicas (Aquele momento tenso da faxina!) ---")
    

    print("\nRemovendo 'Bohemian Rhapsody - Queen' (estava ali no meio, coitada):")
    playlist_show.remover_musica_duplo("Bohemian Rhapsody - Queen") 
    playlist_show.mostrar_playlist_frente() 
    

    print("\nRemovendo 'Smells Like Teen Spirit - Nirvana' (era a primeira da fila, a líder da banda):")
    playlist_show.remover_musica_duplo("Smells Like Teen Spirit - Nirvana") 
    playlist_show.mostrar_playlist_frente()
    

    print("\nRemovendo 'Like a Rolling Stone - Bob Dylan' (a última, fechando a porta ao sair):")
    playlist_show.remover_musica_duplo("Like a Rolling Stone - Bob Dylan") 
    playlist_show.mostrar_playlist_frente()
    

    print("\nTentando remover música inexistente ('Hey Jude' - acho que ela está em outra festa):")
    playlist_show.remover_musica_duplo("Hey Jude - The Beatles") 
    

    print("\nRemovendo as restantes para esvaziar (limpando o palco geral!):")
    playlist_show.remover_musica_duplo("Imagine - John Lennon") 
    playlist_show.remover_musica_duplo("Stairway to Heaven - Led Zeppelin") 
    playlist_show.mostrar_playlist_frente() 

    
    
    print("\n--- Bloco 5: Teste Rápido - O Destino do 'One Hit Wonder' ---")
    playlist_unica = PlaylistDupla() 
    playlist_unica.adicionar_musica_no_final_duplo("One - U2") 
    playlist_unica.mostrar_playlist_frente() 
    print("Removendo 'One - U2' (o único sobrevivente):")
    playlist_unica.remover_musica_duplo("One - U2") 
    playlist_unica.mostrar_playlist_frente() 

    print("\n🎉 Testes Concluídos! Se não explodiu nada e a ordem das músicas fez sentido,")
    print("   Sua playlist é oficialmente mais estável que minha última dieta! SUCESSO! 🎉")
    print("   Pode comemorar com sua música favorita (que não foi removida acidentalmente, espero!) 🥳")
