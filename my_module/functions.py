"""
A collection of functions for doing my project. The only unoriginal function is get_input().

NOTE: Docstrings and code comments were made with the help of ChatGPT but reviewed and edited myself after generation.

"""


def check_correct_positions(guess, wordle_word):
    """
    Compares each letter of the guess with the corresponding letter in the Wordle word,
    to see if the letter is correct and in the right position.
    
    Args:
        guess (str): The guessed word.
        wordle_word (str): The correct Wordle word.
    
    Returns:
        str: A string where each correctly positioned letter is replaced by '.'.
    
    Example:
        >>> check_correct_positions('apple', 'ample')
        '.p...'
    """
    
    # Changing inputs to lower case to make it case insensitive
    guess = guess.lower()
    wordle_word = wordle_word.lower()
    
    position = 0  
    out = ''     
    
    # Iterate through each letter in the guess
    for letter in guess:
        if letter == wordle_word[position]:
            out += '.'  # Replace with '.' if correct
        else:
            out += letter  # Keep original letter if incorrect
        position += 1
    
    return out


def check_correct_letters(guess, wordle_word):
    """ 
    Checks and replaces each letter in the guess with '-'
    if it exists in the Wordle word but is incorrectly positioned.
    
    Meant to take in the output from the check_correct_positions function.
    
    Args:
        guess (str): The guessed word.
        wordle_word (str): The correct Wordle word.
    
    Returns:
        str: A string where each correct letter that is incorrectly positioned is replaced by '-'.
    
    Example:
        >>> check_correct_letters('crane', 'acres')
        '---n-'
    """
    
    out = ''
    
    # Changing inputs to lower case to make it case insensitive
    guess = guess.lower()
    wordle_word = wordle_word.lower()
    
    # Iterate through each letter in the guess
    for letter in guess:        
        if letter in wordle_word:
            out += '-'  # Replace with '-' if the letter is in the word
        else:
            out += letter  # Keep the original letter if not
    
    return out


def check_incorrect_letters(guess, wordle_word):
    """
    Replaces each letter in the guess with '/' if it is not in the Wordle word.
    
    This function is meant to be called after check_correct_positions and check_correct_letters.
    
    Args:
        guess (str): The guessed word.
        wordle_word (str): The correct Wordle word.
    
    Returns:
        str: A string where each incorrect letter is replaced by '/'.
    
    Example:
        >>> check_incorrect_letters('flute', 'brute')
        '//ute'
    """
    out = ''
    
    # Changing inputs to lower case to make it case insensitive
    guess = guess.lower()
    wordle_word = wordle_word.lower()
    
    # Iterate through each letter in the guess
    for letter in guess:
        if letter in '.-':  # Keep characters indicating correct or misplaced positions
            out += letter
        elif letter not in wordle_word:  # Replace incorrect letters with '/'
            out += '/'
        else:
            out += letter  # Keep correct letters in case they are ungraded
            
    return out


def check_wordle_guess(guess, wordle_word):
    """
    Checks a guessed word against the correct Wordle word, providing feedback on correctness.
    
    Args:
        guess (str): The guessed word.
        wordle_word (str): The correct Wordle word.
    
    Returns:
        str: A string indicating the correctness of each letter in the guess.
    """
    
    # Convert guess to lowercase to ensure case-insensitive comparison
    lower_case_guess = guess.lower()
    
    # Check for correct letter positions
    checked_position_guess = check_correct_positions(lower_case_guess, wordle_word)
    
    # Check for correct letters in incorrect positions
    checked_letter_guess = check_correct_letters(checked_position_guess, wordle_word)
    
    # Check for incorrect letters
    fully_checked_guess = check_incorrect_letters(checked_letter_guess, wordle_word)
    
    return fully_checked_guess


def wordle_prompt():
    """
    Displays the introductory text and game instructions for the Wordle game.
    
    Output:
        The game instructions and key for interpreting feedback.
    """
    print('WORDLE GAME: Guess the mystery word in 6 tries or less!')
    print(' ')
    print('Guesses must be 5 letters, with no repeating letters.')
    print(' ')
    print('Key: a . represents a correct letter in the correct position')
    print('     a - represents a correct letter in the incorrect position')
    print('     a / represents an incorrect letter in your guess.')


def get_input():
    """
    Asks user for an input message.
    
    Returns
    -------
    msg : str
        text specified on input by user
    out_msg : None
        always returns None; subsequent functions would return a more specific out_msg
    """
    
    msg = input('INPUT :\t')
    out_msg = ''
    
    return msg, out_msg


def check_each_guess(wordle_words, wordle_word):
    """
    Allows the user 6 attempts to guess the Wordle word.
    Prints the grade of the guesses and game outcome.
    """
    guess_number = 0
    correct = False
    
    # Loop until either the correct word is guessed or the maximum number of attempts is reached
    while guess_number < 6 and correct == False:
    
        guess, response = get_input()
        grade = check_wordle_guess(guess, wordle_word)

        # Check if the guess meets the criteria
        if len(guess) != 5:
            print('Guess word must be 5 letters.')
            continue  # Skip to the next iteration without counting the invalid guess
            
        elif guess.lower() not in wordle_words:
            print('Not a valid word in this game.')
            continue  # Skip to the next iteration without counting the invalid guess
        
        # Check if guess is correct
        correct = (grade == '.....')
        
        # increment number of guesses
        guess_number += 1
            
        print(grade)
    
    # Determine game outcome based on the result of check_each_guess()
    if correct:
        out_msg = 'Congratulations! You have solved this Wordle :)'
    else:
        out_msg = 'You have lost this Wordle :( Better luck next time! The word was: ' + wordle_word

    print(out_msg)
    
    return None


def play_wordle_game(wordle_words, wordle_word):
    """
    Plays the Wordle game.
    """
    # Display game instructions
    wordle_prompt()
    
    # Check each guess made by the user and determine game outcome
    check_each_guess(wordle_words, wordle_word)
