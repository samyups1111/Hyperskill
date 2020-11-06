import random

print('H A N G M A N')
words = 'python', 'java', 'kotlin', 'javascript'
random_word = random.choice(words)
word = '-'.split() * len(random_word)
lives = 8
while lives:
    if random_word in ''.join(word):
        print(f"""\n{''.join(word)}
You guessed the word!
You survived!""")
        break
    x = input(f"\n{''.join(word)}\nInput a letter: ")
    if x in random_word:
        if x in word:
            lives -= 1
            print('No improvements')
        else:
            for n in range(len(random_word)):
                if random_word[n] == x:
                    word[n] = x
    else:
        lives -= 1
        print("That letter doesn't appear in the word")
else:
    print('You lost!')
