import random
print('=' * 25, 'OLÁ, SEJA BEM VINDO(A) AO JOGO DA FORCA 🎮', '=' * 25)
print('''
    O objetivo deste jogo é descobrir uma palavra adivinhando as letras que ela possui. 
    A cada rodada, os jogadores irão simultaneamente escolher uma letra que suspeitem fazer parte da palavra. 
    Caso a palavra contenha esta letra, será mostrado em que posição(ões) ela está. Ao contrário, o jogador será enforcado.
    Você tem 6 chances.
    BOA SORTE !
==== MENU: ====
[a] - Alimentos
[l] - Lugares
[o] - Objetos
''')
alimentos = ['JABOTICABA', 'PINHA', 'MELANCIA', 'MANGA', 'GOIABA', 'ABACAXI', 'ACEROLA', 'LIMÃO']
lugares = ['GRAMADO', 'PARATI', 'SALVADOR', 'BANANEIRAS', 'MEXICO', 'BUENOS AIRES', 'SANTIAGO']
objetos = ['TECLADO', 'POLTRONA', 'QUADRO', 'TAPETE', 'TALHER', 'CADEIRA', 'MESA', 'GARRAFA']
reiniciar_jogo = True
while reiniciar_jogo:
    digitadas = []
    acertos = []
    erros = 0
    chances = 6
    valid_usuario = False
    while valid_usuario == False:
        usuario = input('DIGITE A OPÇÃO DESEJADA (a: alimentos, l: lugares e o: objetos): ').lower()
        if usuario == "a":
            palavra = random.choice(alimentos)
            break
        elif usuario == "l":
            palavra = random.choice(lugares)
            break
        elif usuario == "o":
            palavra = random.choice(objetos)
            break
        else:
            print("A categoria escolhida não é válida, por favor, selecione uma das opções do Menu!")
            continue
    while True:
        senha = ""
        for letra in palavra:
            senha += letra if letra in acertos else " _ "
        print(senha)
        if senha == palavra:
            print("Parabéns, você ganhou!")
            print("A palavra era {}".format(palavra))
            print('🪘🥇')
            break
        tentativa = input("\nDigite uma letra: ").upper().strip()
        if tentativa.isalpha() == False:
            print("O caracter inserido é inválido. Por favor insira uma letra do alfabeto")
        elif tentativa in digitadas:
            print("Você já tentou esta letra! As letras que você já tentou são: ")
            for item in digitadas:
                print(item, end=" ")
            continue
        else:
            digitadas += tentativa
            if tentativa in palavra:
                acertos += tentativa
                print("Parabéns, você acertou a letra! As letras que você já tentou são:")
                for item in digitadas:
                    print(item, end=" ")
            else:
                erros += 1
                print("Que pena, você errou! Tente novamente.")
                print("Você já cometeu", erros, "tentativas erradas e ainda tem", chances - erros, "tentativas")
                print("As letras que você já tentou são: ")
                for item in digitadas:
                    print(item, end=" ")
        print("\n\nX==:==\nX  :   ")
        print("X  O   " if erros >= 1 else "X")
        linha2 = ""
        if erros == 2:
            linha2 = "  |   "
        elif erros == 3:
            linha2 = " \|   "
        elif erros >= 4:
            linha2 = " \|/ "
        print("X%s" % linha2)
        linha3 = ""
        if erros == 5:
            linha3 += " /     "
        elif erros >= 6:
            linha3 += " / \ "
        print("X%s" % linha3)
        print("X\n===========")
        if erros == 6:
            print("Poxa, você foi enforcado!")
            print("A palavra era {}".format(palavra))
            print('💀️')
            break
    usuario = input("Deseja jogar novamente? Digite N ou S:")
    if usuario != 's' and usuario != 'n':
        print('Tecle s ou n.')
        usuario = input("Deseja jogar novamente? Digite N ou S:")
    elif usuario.lower() == "n":
        reiniciar_jogo = False

print("Jogo finalizado.")