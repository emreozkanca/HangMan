import random
import requests
import re
import sys
#get a random word from the dictionary
def get_word(self):
    #select a word length
    length = int(input("Select a word length: "))
    #length must be > 0
    if length <= 0:
        print("Word length must be greater than 0!")
        sys.exit()
    #get the dictionary
    r = requests.get(self.url)
    #split the dictionary into a list of words with regex
    dictionary = re.findall(r'[a-zA-Z]{'+str(length)+'}', r.text)
    #select a random word from the list with try and except
    try:
        word = random.choice(dictionary)
    except:
        print("No words of that length in the dictionary!")
        sys.exit()
    #check if the word is the right length
    while len(word) != length:
        word = random.choice(dictionary)
    return word