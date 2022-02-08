#Create a hangman game.
from src.get_word import *
from src.display_word import *
from src.guess import *
from src.play import *


class Hangman:
    #enter url for the dictionary
    url = "https://raw.githubusercontent.com/StarlangSoftware/Dictionary/master/src/main/resources/turkish_dictionary.txt"
    #initialize the game
    def __init__(self):
        #initialize the game
        self.word = get_word(self)
        #set the number of lives
        self.lives = 10
        #set the display
        self.display = []
        #set the guesses
        self.guesses = []
        #set the game over
        self.game_over = False
        #set the win
        self.win = False
        #display the word
        display_word(self)
        #guess the word
        guess(self)
        #play the game
        play(self)
        

if __name__ == "__main__":
    Hangman()
