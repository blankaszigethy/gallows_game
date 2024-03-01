from lib.database import sentences
from lib.player import Player 
import random

class Game:
    

    running = True
    posssible_fails = 12
    letters = []

    def __init__(self):
        pass


    def setup_player(self):
        player_name = input("Enter your name: ")
        self.player = Player(player_name)
        self.player.display_name()


    def select_sentence(self):
        return random.choice(sentences)


    def win(self):
        print(self.player.name + " wins")


    def lose(self):
        print(self.player.name + " loses")
        self.running = False


    def correct(self, letter):
        print(f'The letter "{letter}" is in the sentence')


    def incorrect(self, letter):
        print(f'The letter "{letter}" isn\'t in the sentence')
        
        self.posssible_fails = self.posssible_fails - 1
        print(f"You have now only {self.posssible_fails} possible mistake(s)")
        
        if self.posssible_fails == 0:
            self.lose()


    def is_in(self, sentence, letter):
        if letter in sentence:
            return True
        else:
            return False
        

    def run(self):
        self.setup_player()
        print(sentences)

        sentence = self.select_sentence()
        print(sentence)

        while self.running:
            letter = input("Choose a letter: ")

            if letter in self.letters:
                print(f"Letter {letter} is already choosen")
                continue

            if len(letter) != 1:
                print("Please choose a valid letter")
                continue

            self.letters.append(letter)
            
            print("Your choice: " + letter)

            if self.is_in(sentence, letter):
                self.correct(letter)
            else:
                self.incorrect(letter)




g = Game()
g.run()    

