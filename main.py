#Create a hangman game.
from src.get_word import *
from src.guess import *
from src.guessforpc import *
from src.get_wordforpc import *



class Hangmanforpc:
    #initialize the game
    def __init__(self):
        self.word = get_wordforpc().get_word()
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
        display_wordforpc.display_word(self)
        #get the word
        guessforpc.guess(self)
        #play the game
        playforpc.play(self)


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
    #choose the game
    game = input("Do you want to play the game for pc or for you? (pc/you)")
    if game == "you":
        Hangman()
    elif game == "pc":
        Hangmanforpc()
    else:
        print("Please enter a valid input.")

    
        
