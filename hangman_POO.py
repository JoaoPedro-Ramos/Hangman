from random import choice
from time import sleep


class Hangman:

    def __init__(self):
        self.lista = ['python', 'java', 'kotlin', 'javascript']
        self.escolha_computador = None
        self.tracos = None
        self.letra_player = None
        self.letras_digitadas = []
        self.erros = 0
        self.play_exit = None

    def inicializacao(self):
        print('Iniciando o jogo!')
        print('Regras: \n-> Digite apenas uma letra por vez\n-> Você pode errar somente 8 vezes\n-> Preste atenção nas mensagens, elas podem te ajudar\n-> DIVIRTA-SE!')
        sleep(4)
        print()
        print('H A N G M A N')
        print()
        self.menu() 

    def menu(self):
        self.play_exit = str(input('Type "play" to play the game, "exit" to quit: ')).upper()
        self.escolha_computador = choice(self.lista)
        self.tracos = '-' * len(self.escolha_computador)
        self.letras_digitadas = []
        self.p_e()
    
    def p_e(self):
        if self.play_exit == 'EXIT':
            return None
        elif self.play_exit == 'PLAY':
            self.tela_input()
        else:
            self.menu()


    def tela_input(self):
        print()
        print(f'\033[1;32m{self.tracos}')
        print(f'\033[1;31mERROS: {self.erros}\033[m')
        self.letra_player = input('Input a letter: ')
        self.one_letter()

    def one_letter(self):
        if len(self.letra_player) == 1:
            self.cond_min()
        else:
            print('\033[1;33mYou should print a single letter\033[m')
            self.tela_input()

    def cond_min(self):
        if self.letra_player in 'abcçdefghijklmnopqrstuvwxyz':
            self.add_letra()
        else:
            print('\033[1;33mIt is not an ASCII lowercase letter\033[m')
            self.tela_input()

    def add_letra(self):
        if self.letra_player in self.escolha_computador:
            if self.letra_player not in self.tracos:
                for i in range(len(self.escolha_computador)):
                    if self.escolha_computador[i] in self.letra_player:
                        self.tracos = self.tracos[:i] + self.escolha_computador[i] + self.tracos[i + 1:]
            elif self.letra_player in self.tracos:
                print('\033[1;33mYou already typed this letter\033[m')
            self.condicoes()
        else: 
            self.else_add_letra()

    def else_add_letra(self):
        if self.letra_player not in self.letras_digitadas:
            print('\033[1;33mNo such letter in the word\033[m')
            self.erros += 1
        else:
            print('\033[1;33mYou already typed this letter\033[m')
            self.erros += 1
        self.condicoes()
        
    def condicoes(self):
        self.letras_digitadas.append(self.letra_player)
        if self.erros == 8:
            print('\033[1;31mYou are hanged!\033[m')
            self.menu()
        else:
            if self.tracos == self.escolha_computador:
                print(f'You guessed the word \033[1;34m{self.tracos}\033[m!', '\n\033[1;32mYou survived!\033[m')
                self.menu()
            elif self.letra_player != self.escolha_computador:
                self.tela_input()


classe = Hangman()
classe.inicializacao()
