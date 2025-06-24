# WordWhiz - Word Guessing Game

This is a simple word guessing game written in Python. The game selects a random word from a word bank stored in a text file (`genz_words.txt`). The player is given 10 attempts to guess letters in the word. Each correct guess fills in the corresponding letter(s) in the word, while incorrect guesses reduce the number of attempts.

## Features

- **Word Selection**: The game randomly selects a word from a text file (`genz_words.txt`), which contains a list of words.
- **Game Loop**: The player has 10 attempts to guess the word by entering letters.
- **Guess Feedback**: After each guess, the game provides feedback indicating if the letter is in the word.
- **Game Over**: The game ends when the player correctly guesses the word or runs out of attempts.
  
## Requirements

- Python 3.x
- A `genz_words.txt` file containing a list of words (one word per line).

## How to Run the Game

1. **Clone the repository** (or download the files):

    ```bash
    git clone https://github.com/yourusername/word-guessing-game.git
    ```

2. **Prepare the word bank**: Ensure you have a file named `genz_words.txt` in the same directory as the Python script. Each line in the file should be a single word.

3. **Run the game**:

    ```bash
    python word_guessing_game.py
    ```

    Replace `word_guessing_game.py` with the name of the Python file if it's different.

## Example

```bash
Current word: _ _ _ _ _ _ _
Guess a letter: e
Great guess cutie!

Current word: _ e _ _ e _ _
Guess a letter: t
Nah uh. Wrong guess! You have now only 9 remaining

...
