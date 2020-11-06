import random
import string

print('H A N G M A N')
words = 'python', 'java', 'kotlin', 'javascript'
random_word = random.choice(words)
word = '-'.split() * len(random_word)
lives = 8
bank = []
def redo(x):
    while lives > 0:
        if len(x) != 1:
            print("You should input a single letter")
            x = input(f"\n{''.join(word)}\nInput a letter: ")
        if x.islower() == False:
            print("Please enter a lowercase English letter")
            x = input(f"\n{''.join(word)}\nInput a letter: ")
        if x not in string.ascii_lowercase:
            print("Please enter a lowercase English letter")
            x = input(f"\n{''.join(word)}\nInput a letter: ")
        if x in bank:
            print("You've already guessed this letter")
            x = input(f"\n{''.join(word)}\nInput a letter: ")
        else:
            bank.append(x)
            return x
while lives > 0:
    if random_word in ''.join(word):
        print(f"""\n{''.join(word)}
You guessed the word!
You survived!""")
        break
    x = input(f"\n{''.join(word)}\nInput a letter: ")
    x = redo(x)
    if x in random_word:
            for n in range(len(random_word)):
                if random_word[n] == x:
                    word[n] = x
                    bank.append(x)
    else:
        print("That letter doesn't appear in the word")
        bank.append(x)
        lives -= 1

else:
    print('You lost!')
