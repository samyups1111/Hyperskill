import random
import string
from sys import exit

def play():
    i = 0
    while i == 0:
        answer = input('Type "play" to play the game, "exit" to quit: ')
        if answer == "play":
            break
        elif answer == "exit":
            exit()
        else:
            i += 0
play()
print('H A N G M A N')
words = 'python', 'java', 'kotlin', 'javascript'
random_word = random.choice(words)
word = '-'.split() * len(random_word)
lives = 8
bank = []
def complete_check(entry):
        if len(entry) != 1:
            print("You should input a single letter")
            return False
        elif entry.islower() == False:
            print("Please enter a lowercase English letter")
            return False
        elif ((entry not in "abcdefghijklmnopqrstuvwxyz")
        and (len(entry) == 1)):
            print("Please enter a lowercase English letter")
            return False
        elif entry in bank:
            print("You've already guessed this letter")
            return False
        else:
            return True
while lives > 0:
    if random_word in ''.join(word):
        print(f"""\n{''.join(word)}
You guessed the word!
You survived!""")
        break
    x = input(f"\n{''.join(word)}\nInput a letter: ")
    valid = complete_check(x)
    if valid == False:
        continue
    else:
        if x not in random_word:
            print("That letter doesn't appear in the word")
            bank.append(x)
            lives -= 1
        else:
            for n in range(len(random_word)):
                if random_word[n] == x:
                    word[n] = x
                    bank.append(x)
else:
    print('You lost!')
play()
