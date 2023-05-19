import random as r
from unidecode import unidecode


def showHangman(vidas):
    
    #Créditos: chrishorton (https://gist.github.com/chrishorton/8510732aa9a80a03c829b09f12e20d9c)
    hangman = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''']
    #ao inves de printar um hangman daqui, vai printar a ascii art final
    if vidas == 1:
        pass

    else:
        vidas *= -1
        #multiplicando por -1 nós tornamos o numero negativo, para que o vetor seja lido ao contrário. A posição -5 será equivalente à posição 1 do vetor.
        print(hangman[vidas])

def setPalavra():
    with open("palavras.txt") as arquivo:
       palavras = arquivo.read().splitlines()
   	
   #Se a varíavel palavras for vazia, o if será False, portanto, só ocorrerá caso seja possível retirar uma palavra de um arquivo chamado palavras.txt.
    if palavras:
    	#sorteia a palavra
        palavraSorteada = r.choice(palavras)
        #retira os acentos e ç dela 
        palavraSorteada = unidecode(palavraSorteada)
        #deixa ela toda minuscula
        palavraSorteada = palavraSorteada.lower()
        
        print(palavraSorteada)

        return palavraSorteada
   #Se palavras for vazio: 
    else:
        print("A lista de palavras não foi carregada corretamente, definindo palavra padrão.")
        
        return "pneumoultramicroscopicossilicovulcanoconiotico"


def setDificuldade(user_input):
    #cria-se um dicionário com as dificuldades disponíveis
    dificuldade = {"normal": 6, "tormento": 4, "inferno": 2, "pesadelo": 1}
    #transforma o input do usuario em minusculo
    user_input = user_input.lower()
    #Se o usuario tiver escrito certo, vai ser selecioanda a dificuldade escrita
    if user_input in dificuldade:
        vidas = dificuldade[user_input]
        print(f"Dificuldade selecionada: {user_input} \nNúmero de vidas: {vidas}")
    #caso contrario, se lascou
    else: 
        print("Parece que você inseriu uma dificuldade que não existe, baseando-se nas suas capacidades de escrita, foi definida a dificuldade pesadelo.")
        vidas = 1
        print("Dificuldade selecionada: Pesadelo \nNúmero de vidas: ", vidas)
    
    return vidas


def getLetras(lista_letras):
    #aqui, checamos o input do usuário, comparando o input com a lista de letras já inseridas
    ok = False
    
    while not ok:
    	#deixamos o input minusculo
        tentativa = input("Insira uma letra ").lower()
        #tiramos o acento da letra caso tenha sido colocado acento
        tentativa = unidecode(tentativa)
	    
        #se o usuario colocar uma letra que já tentou antes
        if tentativa in lista_letras:
            print("voce ja tentou essa amigao")

	#se o usuario inserir mais de uma letra de uma vez
        elif len(tentativa) != 1:
            print("insira somente UMA letra!!!!!!")
            
        #se o usuario inserir um numero ou um símbolo
        elif not tentativa.isalpha():
            print("insira uma letra amigao")
    
        else:
            ok = True
    
    return tentativa

def showBoard(secret, lista_letras):
    
    #criamos uma variável vazia
    palavra = ''
    for letra in secret:
        #checamos se as letras inseridas pelo usuario estão presentes na palavra sorteada, se estiverem, incrementamos a variável com essa letra
        if letra in lista_letras:
            #deixamos a letra incrementada em maisculo, só pra ficar bonito
            palavra += letra.upper() + ''
        #se a letra não estiver presente, concatenamos com um _, representando um espaço vazio
        else:
            palavra += '_'

    print(palavra)

def startGame():
    #inicia as variáveis
    vitoria = False
    letras_usadas = []
    letras_corretas = []
    dificuldade = input("Qual dificuldade deseja jogar? Normal, Tormento, Inferno ou Pesadelo? ")

    #chama as funções
    palavra_sorteada = setPalavra()
    vidas = setDificuldade(dificuldade)

    while vidas > 0:
        contador = 0
        #colocamos a lista de letras usadas em ordem alfabética.
        letras_usadas = sorted(letras_usadas)
        #o join pega todos os elementos de uma lista e adiciona eles em uma string, aqui, falamos para o programa adicionar os elementos da lista letras_usadas na vírgula, então cada elemento recebe a vírgula após ele.
        print("\nLetras usadas: ", ", ".join(letras_usadas), "\n")
        #mostramos a palavra
        showBoard(palavra_sorteada, letras_corretas)
        #pedimos o input do usuario
        user_guess = getLetras(letras_usadas)
        #depois que o input passa pelas verificações, ele é adicionado à lista de letras usadas
        letras_usadas.append(user_guess)
        
        #checamos se a letra que o usuário inseriu está presente na palavra sorteada
        if user_guess in palavra_sorteada:
            #Se estiver, adicionamos a letra à lista de letras corretas
            letras_corretas.append(user_guess)
        
        #se a letra for errada, chamamos a função de mostrar a forca passando a variavel vidas
        else:
            showHangman(vidas)
            #e em seguida, retiramos uma vida
            vidas -= 1
   
        #comparamos as duas listas para saber se o usuário acertou todas as letras
        for i, j in zip(letras_corretas, palavra_sorteada):
            if i in palavra_sorteada:
                contador += 1
            
            #se o contador for igual ao length da palavra sorteada sem repetição de letras significa que o usuario venceu o jogo
            #o set basicamente cria uma tupla de elementos únicos, ou seja, sem repetição de letras, numeros, etc.
            if contador == len(set(palavra_sorteada)):
                print("Você venceu!")
                print("A palavra sorteada era: ", palavra_sorteada)
                vitoria = True
        
        #deve ter uma maneira melhor de fazer isso, mas o importante é funcionar
        if vitoria:
            break

    else:

        print(r''' ___________.._______
| .__________))______|
| | / /      ||
| |/ /       ||
| | /        ||.-''.
| |/         |/  _  \
| |          ||  `/,|
| |          (\\`_.'
| |         .-`--'.
| |        /Y . . Y\
| |       // |   | \\
| |      //  | . |  \\
| |     ')   |   |   (`
| |          ||'||
| |          || ||
| |          || ||
| |          || ||
| |         / | | \
""""""""""|_`-' `-' |"""|
|"|"""""""\ \       '"|"|
| |        \ \        | |
: :         \ \       : :  
. .          `'       . . ''')
        print("Créditos ASCII ART: Manus O'Donnell")
        print(r" _  _   __    ___  ____    ____  ____  ____  ____  ____  _  _   ")
        print(r"/ )( \ /  \  / __)(  __)  (  _ \(  __)(  _ \(    \(  __)/ )( \/")
        print(r"\ \/ /(  O )( (__  ) _)    ) __/ ) _)  )   / ) D ( ) _) ) \/ ( ")
        print(r" \__/  \__/  \___)(____)  (__)  (____)(__\_)(____/(____)\____/ ")
        print("A palavra sorteada era: ", palavra_sorteada)

#main
jogo = True
while jogo:
    startGame()

    resposta = input("Parece que o jogo acabou... Quer jogar de novo?? Sim / Nao ")

    if resposta.lower() in ("nao", "não", "n"):
        break
    
    else:
        pass

print("Te vejo na próxima então!")


