Opa, opa, opa! 🚨 Me pegou no pulo! Você é um programador astuto, hein? 👀 Eu aqui, todo pimpão, pensando em simplificar minha vida (e a sua, juro! 🤥) com uma lista simplesmente encadeada, e você já querendo o pacote completo com a **duplamente encadeada**! Gosto da sua ambição! É tipo pedir batata frita e já querer o combo com milkshake e tortinha de maçã. 🍟🥤🥧

Ok, ok, sem mais enrolação de estagiário atrapalhado. 😅 Se é duplamente encadeada que você quer, é duplamente encadeada que você terá! Isso significa que nossos post-its (nós) agora não só apontam para a próxima música, mas também para a **música anterior**! Chique, né? É tipo ter olhos na nuca! 👀🔙

Vamos recalcular a rota dessa nossa jornada musical. Prepare-se para mais setinhas! ➡️⬅️

**Roteiro Épico da Playlist DUPLAMENTE Encadeada (Agora Vai! Ou Não... 😬):**

1.  **Passo 1: O Átomo da Música 2.0 (Nosso Nó Superpoderoso) ⚛️🎶💪**
    *   Nosso post-it (nó) evoluiu! Agora ele tem:
        *   O nome da música (e artista, claro).
        *   Uma setinha mágica apontando para o **PRÓXIMO** post-it.
        *   E... rufem os tambores... 🥁 uma setinha mágica apontando para o post-it **ANTERIOR**! Uau! 🤯
    *   **Meta:** Criar uma classe `MusicaNodeDuplo` (nome chique, hein?) com `dados` (a música), `proximo` e `anterior`.

2.  **Passo 2: A Corrente da Alegria Bidirecional (A Playlist Turbinada) 🔗🥳🔗**
    *   Nossa Playlist também fica mais esperta. Além de saber qual é a PRIMEIRA música ("cabeça"), agora também pode ser útil saber qual é a **ÚLTIMA** ("cauda"). Isso facilita algumas manobras!
    *   **Meta:** Criar a classe `PlaylistDupla` que guarda a referência para a `cabeça` e, opcionalmente (mas recomendado!), para a `cauda`.

3.  **Passo 3: Botando Música na Fila (Adicionar ao Final - Versão Deluxe) 🚶‍♀️🚶‍♂️🎶✨**
    *   Adicionar ao final fica um pouquinho mais complexo, porque temos que atualizar as setinhas do penúltimo para o novo, e do novo para o penúltimo. É um relacionamento de mão dupla! 🤝
    *   Se a lista estiver vazia, o novo nó é cabeça e cauda. Simples assim (só que na prática a gente sempre esquece um `if` 🤦).
    *   **Meta:** Implementar `adicionar_musica_no_final_duplo` na `PlaylistDupla`.

4.  **Passo 4: DJ, Solta o Som! (E Rebobina!) 🎧🎤⏪⏩**
    *   Mostrar a playlist continua valendo. Mas agora, com o poder do `anterior`, podemos também... mostrar a playlist de TRÁS PRA FRENTE! 😱 Que bruxaria é essa?!
    *   **Meta:** Implementar `mostrar_playlist_frente` e `mostrar_playlist_tras` (ou um parâmetro para controlar a direção, se a gente estiver se sentindo eficiente).

5.  **Passo 5: Furando a Fila com Estilo (Adicionar no Início - Versão Dupla) 🚀🎶🎩**
    *   Colocar uma música no início também exige cuidado com as duas setinhas. O novo nó aponta para a antiga cabeça, e a antiga cabeça (se existir) aponta de volta para o novo nó.
    *   **Meta:** Implementar `adicionar_musica_no_inicio_duplo`.

6.  **Passo 6: Caça ao Tesouro Musical (Ainda Buscando...) 🗺️🧐**
    *   A busca continua parecida. A gente pode ir só para frente, não precisa complicar o que já funciona (eu acho 😅).
    *   **Meta:** Implementar `buscar_musica_duplo`.

7.  **Passo 7: Adeus, Sofrência! (Remover Música - Agora Mais Fácil? 🤔)**
    *   Aqui a lista duplamente encadeada MOSTRA SEU VALOR! 🌟 Remover um nó fica (teoricamente) mais fácil porque, uma vez que você acha o nó para remover, você já tem acesso direto ao anterior e ao próximo dele.
    *   Só precisa fazer o `anterior` apontar para o `proximo` do nó removido, e o `proximo` apontar para o `anterior`. Parece um trava-línguas, né? É quase isso.
    *   Cuidado especial com remoção da cabeça ou da cauda! Esses são os momentos que a gente descobre se tomou café suficiente. ☕
    *   **Meta:** Implementar `remover_musica_duplo`. (Menos calafrios dessa vez? Talvez... 🥶)

8.  **Passo 8: O Gran Finale Duplamente Incrível! (Testando Tudo ao Quadrado) 🎉💻🤞🤞**
    *   A hora da verdade ao quadrado! Testar todas as funcionalidades, incluindo a navegação para trás e a remoção (que a gente espera que seja mais suave).
    *   Adicionar, remover, mostrar pra frente, mostrar pra trás... a festa vai ser boa!
    *   **Meta:** Um programa que não só funciona, mas que nos faz sentir gênios da programação por termos domado a fera da lista duplamente encadeada! 🏆 (Ou pelo menos aliviados por ter acabado. 😌)

E aí, topa o desafio dobrado? Se sim, podemos começar pelo Passo 1 (versão 2.0) quando você der o sinal verde! 🚦