import random
import string

words = 'python', 'java', 'kotlin', 'javascript'
random_word = random.choice(words)
word = '-'.split() * len(random_word)
bank = []


# Checks if we correctly guessed the whole word
def is_word_correct(word):
    return random_word in ''.join(word)

# Returns True if valid input
# Prints error message and returned False if invalid input
def validate(guess):
    if len(guess) != 1:
        print("You should input a single letter")
        return False
    elif not guess.islower():
        print("Please enter a lowercase English letter")
        return False
    elif guess in bank:
        print("You've already guessed this letter")
        return False
    else:
        return True

# Only updates the word with the correctly guessed letter
def update_word_with_guess(guess):
    for n in range(len(random_word)):
        if(random_word[n] == guess):
            word[n] = guess

# Contains the main part of the code
print('H A N G M A N')
lives = 8

while lives > 0:

    if is_word_correct(word):
        print(f"""\n{''.join(word)}\nYou guessed the word!\nYou survived!""")
        break;
    else:

        guess = input(f"\n{''.join(word)}\nInput a letter: ")

        is_valid = validate(guess)

        if not is_valid: 
            continue
        else:
            bank.append(guess)
            if guess in random_word:
                update_word_with_guess(guess)
            else:
                print("\nThat letter doesn't appear in the word")
                lives -= 1
                if lives == 0:
                    print('You lost!')  
