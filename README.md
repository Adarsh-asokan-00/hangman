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

- **`count_letters(word)`**: Computes the frequency of each letter in the given word and returns a dictionary with letters as keys and their counts as values.

- **`display_hangman(tries)`**: Provides an ASCII art representation of the hangman figure based on the number of remaining tries. This function helps visualize the game's progress and the player's current status.

- **`get_word()`**: Randomly selects a word from the predefined `word_list`. This function ensures that each game starts with a new and randomly chosen word.

- **`reset_game()`**: Resets the game state to initialize a new game. It selects a new word, resets the word completion display, clears guessed letters and words, and sets the number of tries to the initial value.

- **`process_letter_guess(guess, word)`**: Processes a guess where the player guesses a single letter. Updates the display of the word in progress based on whether the guess is correct or not and adjusts the number of remaining tries.

- **`process_word_guess(guess, word)`**: Handles a full word guess from the player. It checks if the guessed word matches the selected word, updates the game state accordingly, and adjusts the number of remaining tries if the guess is incorrect.

- **`game()`**: Manages the main game loop, including displaying the hangman figure, the word progress, and remaining tries. It handles user input for letter and word guesses, processes those guesses, and provides feedback. This function also manages game state and allows players to restart the game.



Acknowledgements
Streamlit for providing a powerful and easy-to-use framework for creating interactive web apps.
ASCII art resources for the hangman figure.
