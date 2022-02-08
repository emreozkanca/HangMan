#display the word
def display_word(self):
    for i in range(len(self.word)):
        self.display.append("_")
    print(" ".join(self.display))