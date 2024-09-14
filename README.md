# Hangman Game

## Overview

This project is a simple Hangman game built using Streamlit, a popular framework for creating interactive web applications in Python. The game allows users to guess letters or the entire word while providing feedback and displaying a hangman drawing based on the number of remaining tries.

## Features

- Interactive web interface built with Streamlit
- ASCII art display of the hangman figure
- Random word selection from a predefined list
- Letter and full-word guessing functionality
- Game state management with feedback and try tracking
- Option to play the game again
## Code Explanation

- **`count_letters(word)`**: Uses `Counter` from the `collections` module to count the occurrences of each letter in the given word and returns a dictionary with these counts.

- **`display_hangman(tries)`**: Returns an ASCII representation of the hangman figure based on the number of remaining tries, which visually represents the current state of the game.

- **`get_word()`**: Selects a random word from the predefined `word_list` and returns it for the game.

- **`get_hint(word, word_completion)`**: Provides a hint by revealing one letter of the word if a certain number of incorrect guesses have been made, helping players progress in the game.

- **`reset_game()`**: Resets the game state to start a new round, initializing variables such as the word to guess, the current state of the word, the number of tries, and tracking guesses.

- **`process_letter_guess(guess, word)`**: Processes a single letter guess, updating the game state based on whether the guess is correct or not, and adjusts the number of remaining tries accordingly.

- **`process_word_guess(guess, word)`**: Handles guesses where the player attempts to guess the entire word, checking for correctness and updating the game state if the guess is correct or incorrect.

- **`game()`**: The main function that manages the flow of the game, including displaying the hangman figure, handling user inputs, providing hints, and determining the end of the game.


Acknowledgements
Streamlit for providing a powerful and easy-to-use framework for creating interactive web apps.
ASCII art resources for the hangman figure.
