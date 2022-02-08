import time
from src.guess import *
#play the game
def play(self):
        while self.game_over == False:
            guess(self)
            time.sleep(1)
        if self.win == True:
            print("You won!")
        else:
            print("You lost!")