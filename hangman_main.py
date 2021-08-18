from tkinter.constants import N
from hangman import rand
from hangman2 import solver
random_word=rand()
ramdom_word=random_word.upper()
print("you have 5 guesses")
solver(random_word)
a=input("")