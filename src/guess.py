#guess a letter
def guess(self):
    #get a letter
    letter = input("Guess a letter: ")
    #check if the letter is in the word
         
    if letter in self.word:
        #print correct message
        print("Correct!")
        #check if the letter is in the display 
        if letter in self.display:
            print("You already guessed that letter!")
        else:
            #check if the letter is in the word
            for i in range(len(self.word)):
                if letter == self.word[i]:
                    self.display[i] = letter
            #display the word
            print(" ".join(self.display))
            #check if the word is complete
            if self.word == "".join(self.display):
                self.win = True
                self.game_over = True
    else:
        #check if the letter is in the guesses
        if letter in self.guesses:
            print("You already guessed that letter!")
        else:
            #add the letter to the guesses
            self.guesses.append(letter)
            #decrease the number of lives
            self.lives -= 1
            print("You have {} lives left!".format(self.lives))
            #check if the lives are 0
            if self.lives == 0:
                self.game_over = True
                self.win = False
            #display the word
            print(" ".join(self.display))