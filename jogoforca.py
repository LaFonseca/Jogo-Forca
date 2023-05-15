import random

# Lista de palavras para o jogo da forca.
palavras = ['mesa', 'futebol', 'brasil', 'caderno', 'celular', 'garrafa', 'clima', 'temperatura']

## Seleciona uma palavra aleatória e cria uma lista.
palavra = random.choice(palavras)
letras = list(palavra)

### plota o número de traços do tamanho da palavra.
tracos = ['_'] * len(palavra)

#### Número de tentativas.
tentativas = 6

##### Loop do jogo.
while tentativas > 0:
    
    print(' '.join(tracos))

    
    letra = input('Digite uma letra: ')

    
    if letra in letras:
        ###### Substitui o traço pela letra na posição correta.
        for i in range(len(letras)):
            if letras[i] == letra:
                tracos[i] = letra
    else:
        ####### Reduz o número de tentativas.
        tentativas -= 1
        print('Letra não encontrada. Você tem mais', tentativas, 'tentativas.')

    ######## Verifica se o jogo acabou.
    if '_' not in tracos:
        print('Parabéns, você ganhou!')
        break

######### Se o número de tentativas acabou, o jogador perdeu a partida.
if tentativas == 0:
    print('Você perdeu. A palavra era', palavra)