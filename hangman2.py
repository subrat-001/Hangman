from body import printing
import random
def display(words):
    a=""
    for i in words:
        a+=i
        a+=" "
    return a

def rand(guess):
    return random.choice(guess)

def word(listed):
    a=""
    for i in listed:
        a+=i
    return a
def solver(random_word):
    guess_list=[]
    n=0
    new_list=[]
    soln=[]
    for a in random_word:
        if a==" ":
            soln.append(" ")
        else:
            soln.append("_")
    done=[]
    for i in random_word:
            new_list.append(i)
            if i ==" ":
                pass
            else:
                guess_list.append(i)
    cho=rand(guess_list)
    q=0
    for i in random_word:
        if i== cho:
            soln.pop(q)
            soln.insert(q,cho)
            guess_list.pop(guess_list.index(cho))
            done.append(cho)
        else:
            pass
        q+=1
    print(display(word(soln)))
    while n!=5:
        ava=False
        reuse=False
        guess = str(input(" : ")).upper()[0]
        if guess.isalpha() is False:
            print("is not a letter")
            continue
        for d in done:
            if d==guess:
                reuse= True
                if d==cho:
                    print("in the clue")
                    break
                print("already guessed")
                break
        if reuse is True:
            continue
        done.append(guess)
        o=0
        for i in new_list:
            if i==guess:
                ava=True
                soln.pop(o)
                soln.insert(o,guess)
                guess_list.pop(guess_list.index(guess))
            else:
                pass
            o+=1
        if ava is True:
            print(display(word(soln)))
        if ava is False:
            print(display(word(soln)))
            n+=1
        r=5-n
        printing(n)
        if guess_list == []:
            break;
        if n==5:
            break
    b=word(new_list)
    if n==5:
        print(f"You Lose,The word is {display(random_word)}")
    else :
        print(f"""you win!!!
        {word(display(random_word))}""")
        