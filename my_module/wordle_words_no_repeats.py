''' This is the function I used to get the Wordle dataset I got from Github to remove words that have repeating letters.

    Original dataset can be found at: https://gist.github.com/cfreshman/a03ef2cba789d8cf00c08f767e0fad7b 
    It is also uploaded within the my_module folder along with this file and the output text file that this code produces.

    All code here was written by ChatGPT. I could have learned how to do it, but it was not the focus of my project.
    
    '''

def has_repeating_letters(word):
    """Check if a word contains repeating letters."""
    for char in set(word):
        if word.count(char) > 1:
            return True
    return False

def filter_repeating_words(input_file, output_file):
    """Filter out words with repeating letters from a file."""
    with open(input_file, 'r') as file:
        lines = file.readlines()

    # Remove newline characters and filter out words with repeating letters
    filtered_words = [line.strip() for line in lines if not has_repeating_letters(line.strip())]

    # Write the filtered words to a new file, each on a new line
    with open(output_file, 'w') as file:
        for word in filtered_words:
            file.write(word + '\n')


filter_repeating_words("wordle_words.txt", "wordle_words_no_repeats.txt")