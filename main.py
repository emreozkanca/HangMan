#Create a hangman game.
from src.get_word import *
from src.guess import *



class Hangman:
    #initialize the game
    def __init__(self):
        self.word = get_word().get_word()
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
        display_word.display_word(self)
        #get the word
        guess.guess(self)
        #play the game
        play.play(self)
        

if __name__ == "__main__":
    Hangman()
