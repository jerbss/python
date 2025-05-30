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

    def __str__(self): 
        """Retorna uma representação em string da playlist."""
        if not self.cabeca: 
            
            return "A playlist está mais vazia que meu bolso no fim do mês! 💸"
        return "Playlist com músicas (detalhes em breve!)" 
    
if __name__ == '__main__':
    print("\n--- Criando e Adicionando Músicas na Playlist ---")
    minha_playlist_top = PlaylistDupla()
    print(minha_playlist_top) 

    minha_playlist_top.adicionar_musica_no_final_duplo("Bohemian Rhapsody - Queen")
    minha_playlist_top.adicionar_musica_no_final_duplo("Stairway to Heaven - Led Zeppelin")
    minha_playlist_top.adicionar_musica_no_final_duplo("Imagine - John Lennon")
    minha_playlist_top.adicionar_musica_no_final_duplo("Like a Rolling Stone - Bob Dylan")

    
    print(f"\nEstado atual da playlist: {minha_playlist_top}")

    if minha_playlist_top.cabeca:
        print(f"Primeira música: {minha_playlist_top.cabeca.dados_musica}")
    if minha_playlist_top.cauda:
        print(f"Última música: {minha_playlist_top.cauda.dados_musica}")
        
        if minha_playlist_top.cauda.anterior:
            print(f"Música anterior à última: {minha_playlist_top.cauda.anterior.dados_musica}")
        else:
            print("A última música não tem uma anterior (isso só deve acontecer se houver apenas uma música).")
        
    if minha_playlist_top.cabeca and minha_playlist_top.cabeca.proximo:
        print(f"Música seguinte à primeira: {minha_playlist_top.cabeca.proximo.dados_musica}")
