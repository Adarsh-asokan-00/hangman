import streamlit as st
import random
from collections import Counter
from word import word_list

def count_letters(word):
    """Returns a dictionary with counts of each letter in the word using Counter."""
    return Counter(word)

def display_hangman(tries):
    """Displays the hangman based on remaining tries."""
    steps = [
        """
        ┏━━┑
        ┃  O
        ┃ /|\\
        ┃  |
        ┃ / \\
        ┻━━━━
        """,
        """
        ┏━━┑
        ┃  O
        ┃ /|\\
        ┃  |
        ┃ / 
        ┻━━━━
        """,
        """
        ┏━━┑
        ┃  O
        ┃ /|\\
        ┃  |
        ┃ 
        ┻━━━━
        """,
        """
        ┏━━┑
        ┃  O
        ┃ /|\\
        ┃    
        ┃ 
        ┻━━━━
        """,
        """
        ┏━━┑
        ┃  O
        ┃ /|
        ┃  
        ┃ 
        ┻━━━━
        """,
        """
        ┏━━┑
        ┃  O
        ┃  |
        ┃  
        ┃ 
        ┻━━━━
        """,
        """
        ┏━━┑
        ┃  O
        ┃  
        ┃    
        ┃ 
        ┻━━━━
        """,
        """
        ┏━━┑
        ┃  
        ┃ 
        ┃  
        ┃
        ┻━━━━
        """
    ]
    return steps[tries]

def get_word():
    """Randomly selects a word for the hangman game."""
    word = word_list.splitlines()
    return random.choice(word).strip()

def get_hint(word, word_completion):
    """Provides a hint by revealing one letter of the word."""
    unrevealed_indices = [i for i, letter in enumerate(word) if word_completion[i] == "_"]
    if unrevealed_indices:
        hint_index = random.choice(unrevealed_indices)
        return word[hint_index]
    return None

def reset_game():
    """Resets the game state to start a new game."""
    st.session_state.word = get_word()
    st.session_state.word_completion = "_" * len(st.session_state.word)
    st.session_state.guessed_letters = []
    st.session_state.guessed_words = []
    st.session_state.tries = 7
    st.session_state.guessed = False
    st.session_state.incorrect_guesses = 0
    st.session_state.hint_provided = False

def process_letter_guess(guess, word):
    """Processes a letter guess."""
    if guess in st.session_state.guessed_letters:
        st.warning(f'You already guessed the letter "{guess}".')
    elif guess not in word:
        st.error(f'The letter "{guess}" is not in the word.')
        st.session_state.tries -= 1
        st.session_state.incorrect_guesses += 1
        st.session_state.guessed_letters.append(guess)
    else:
        st.success(f'Good job! The letter "{guess}" is in the word.')
        st.session_state.guessed_letters.append(guess)
        word_list = list(st.session_state.word_completion)
        indices = [i for i, letter in enumerate(word) if letter == guess]
        for index in indices:
            word_list[index] = guess
        st.session_state.word_completion = "".join(word_list)
        if "_" not in st.session_state.word_completion:
            st.session_state.guessed = True

def process_word_guess(guess, word):
    """Processes a full word guess."""
    if guess in st.session_state.guessed_words:
        st.warning(f'You already guessed the word "{guess}".')
    elif count_letters(guess) == count_letters(word):
        st.success("Congratulations, you guessed the word!")
        st.session_state.word_completion = word
        st.session_state.guessed = True
    else:
        st.error(f'"{guess}" is not the correct word.')
        st.session_state.tries -= 1
        st.session_state.incorrect_guesses += 1
        st.session_state.guessed_words.append(guess)

def game():
    """Main game function for hangman."""
    st.title('Hangman Game')
    col1, col2 = st.columns(2)

    # Initialize session state variables
    if 'word' not in st.session_state:
        reset_game()

    word = st.session_state.word
    word_completion = st.session_state.word_completion
    tries = st.session_state.tries
    guessed = st.session_state.guessed
    incorrect_guesses = st.session_state.incorrect_guesses
    hint_provided = st.session_state.hint_provided

    # Display hangman ASCII art and the word progress
    with col2:
        st.text(display_hangman(tries))
    with col1:
        st.header(f"Word: {word_completion}")
        st.write(f'Tries remaining: {tries}')

    # Provide hint if needed
    if incorrect_guesses >= 3 and not hint_provided:
        hint = get_hint(word, word_completion)
        if hint:
            st.write(f"Hint: The word contains the letter '{hint}'")
            st.session_state.hint_provided = True

    # Handle guesses
    if not guessed and tries > 0:
        guess = st.text_input("Please guess a letter or the word").lower().strip()

        if st.button("Submit Guess"):
            if not guess.isalpha():
                st.error("Invalid input. Please enter only letters.")
            elif len(guess) == 1:
                process_letter_guess(guess, word)
            elif len(guess) == len(word):
                process_word_guess(guess, word)
            else:
                st.error("Invalid guess. Please enter a single letter or the full word.")

    # Handle end of game
    if guessed:
        st.success(f"Congratulations! You guessed the word: {word}")
    elif tries == 0:
        st.error(f"Sorry, you've run out of tries. The word was: {word}")

    # Play again button
    if st.button("Play Again"):
        reset_game()

if __name__ == "__main__":
    game()



