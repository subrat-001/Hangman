import random
def rand() :
    f=open("E:\hangman\words.txt","r")
    words=f.read()
    w=words.split("\n")
    word=[]
    for a in w:
        word.append(a.upper()) 
    a=random.choice(word)
    return a