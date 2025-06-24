import random

with open('genz_words.txt') as f:
    word_bank = [line.strip() for line in f]
    word = random.choice(word_bank)

    guess = ['_'] * len(word)

    tries = 10

# Game loop
while tries > 0:
    print('\nCurrent word: ' + ' '.join(guess))

    guessLetter = input('Guess a letter: ')

    if guessLetter in word:
        for i in range(len(word)):
            if word[i] == guessLetter:
                guess[i] = guessLetter
        print('Great guess cutie!')

    else:
        tries -= 1
        print('Nah uh. Wrong guess! You have now only ' + str(tries) + ' remaining')

    if '_' not in guess:
        print('\nWoohoo! You guessed the word: ' + word)
        break

if '_' in guess:
    print('Oops, you have run out of attempts :( \nThe word was: ' + word)
