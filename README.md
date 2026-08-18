# Wordle Clone

## Overview
This is my clone of the New York Times' Wordle game. It is a text-based played in the input line in a Jupyter notebook. I created this clone to show the skills I gained over 10 weeks in my first programming course learning Python.

## Data
Word list sourced from [cfreshman's Wordle word list gist](https://gist.github.com/cfreshman/a03ef2cba789d8cf00c08f767e0fad7b).
I modified this list to create a new refined txt file that removed all words with repeat letters for my purposes (wordle_words_no_repeats.py).

## Methods
...

## Files
- `my_module/` - folder with all files besides Jupyter notebook
  - `wordle_words/` - folder for txt files with Wordle words, original and revised
    - `wordle_words.txt` - original word list sourced from [cfreshman's Wordle word list gist](https://gist.github.com/cfreshman/a03ef2cba789d8cf00c08f767e0fad7b)
    - `wordle_words_no_repeats.txt` - revised word list without words that have repeat letters
  - `functions.py` - functions that make the game run: 4 that grade a guess + 4 for the game interface
  - `test_functions.py` - tested 3 functions from functions file
  - `wordle_words_no_repeats.py` - code used to filter out the words with repeat letters
- `wordle_clone.ipnyb` - Jupyter notebook where you play the game
