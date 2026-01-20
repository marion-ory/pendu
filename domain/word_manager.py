import random

def word_choice():
    with open("mots.txt", "r") as word_list:
        stock_words = word_list.read().splitlines()
    
    return random.choice(stock_words).lower()