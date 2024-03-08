from lib.database import sentences
from lib.player import Player 
import random

class Game:
    

    running = True
    posssible_fails = 12
    correct_letters = []
    letters = []

    def __init__(self):
        pass

    # itt adja meg az ember a nevét
    def setup_player(self):
        player_name = input("Enter your name: ")
        self.player = Player(player_name)
        self.player.display_name()

    # ez választ ki random egy mondatot
    def select_sentence(self):
        return random.choice(sentences)

    #ez írja ki a játékos nevét és azt ha nyer
    def win(self):
        print(self.player.name + " wins")
        self.running = False

    #ez írja ki a játékos nevét, és ha veszít
    def lose(self):
        print(self.player.name + " loses")
        self.running = False

    #ha eltalál egy betűt, ami szerepel az adott mondatban, kiírja h ez a betű benne van a mondatban
    def correct(self, letter):
        print(f'The letter "{letter}" is in the sentence')

        self.correct_letters.append(letter)
      
    #ha egy olyan betűt ír be, ami nincs a mondatban, akkor kiírja hogy ez a betű nem szerepel 
    #a mondatban és kiírja, hogy hány lehetőséged van még hibázni, és ha elfogytak a lehetőséged kiírja,hogy vesztettél
    def incorrect(self, letter):
        print(f'The letter "{letter}" isn\'t in the sentence')
        
        self.posssible_fails = self.posssible_fails - 1
        print(f"You have now only {self.posssible_fails} possible mistake(s)")
        
        if self.posssible_fails == 0:
            self.lose()

    #ha szerepel az adott betű a mondatban, kiírja hogy true ha minden más akko false
    def is_in(self, sentence, letter):
        if letter.lower() in sentence.lower():
            return True
        else:
            return False
        
    #itt kiadja,h adj meg egy betűt, azt is ha az adott betű szerepelt már benne, ha a betű nem egyezik 1-el(szóval ha több betűt írunk be)
    #akkor kiírja, h helyes betűt írj be
    def run(self):
        self.setup_player()

        sentence = self.select_sentence()

        while self.running:
            print("")
            print("")
            placeholder = self.create_placeholder(sentence)
            filled = self.fill_with_correct_letters(sentence, placeholder)
            print(filled)

            if filled == sentence:
                self.win()
                continue

            letter = input("Choose a letter: ")
            print("")
            print("")

            if letter in self.letters:
                print(f"Letter {letter} is already choosen")
                continue

            if len(letter) != 1:
                print("Please choose a valid letter")
                continue

            self.letters.append(letter)
            

            if self.is_in(sentence, letter):
                self.correct(letter)
            else:
                self.incorrect(letter)

    #itt ha szóköz van a mondatban,akkor egy üres helyet hagy neki, bármi más esetben(szóval ha betű van)alsóvonalat mutat
    def create_placeholder(self, sentence):
        placeholder = ""

        i = 0

        while i < len(sentence):

            if sentence[i] == " ":
                placeholder +=  " "   # += hozzáad a strighez új karaktereket
            else:
                placeholder += "_"
            i = i + 1

        return placeholder

    #lekicsinyítettük abetűket
    def fill_with_correct_letters(self, sentence, placeholder):
        for letter in self.correct_letters:
            i = 0
            while i < len(sentence):
                if letter.lower() == sentence[i].lower():
                    placeholder = placeholder[:i] + sentence[i] + placeholder[i + 1:]

                i = i + 1
        return placeholder
    
# SENTENCE = "Ez egy teszt feladat"
# 
# p = create_placeholder(SENTENCE)
# print(p)
# 
# f = fill_with_correct_letters(SENTENCE, p, ["e", "t"])
# print(f)



g = Game()
g.run()    

