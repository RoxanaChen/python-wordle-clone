"""Tests for my 3 main functions that grade a Wordle guess.
"""

from functions import check_correct_positions, check_correct_letters, check_incorrect_letters


def test_check_correct_positions():
    assert callable(check_correct_positions)
    assert check_correct_positions('RIGHT', 'RIGHT') == '.....'
    assert check_correct_positions('RIgHt', 'RIGHT') == '.....'
    assert check_correct_positions('ALONE', 'CLONE') == 'a....'
    assert check_correct_positions('BATON', 'CLONE') == 'baton'
    
    
def test_check_correct_letters():
    assert callable(check_correct_letters)
    assert check_correct_letters('.....', 'RIGHT') == '.....'
    assert check_correct_letters('A....', 'CLONE') == 'a....'
    assert check_correct_letters('alone', 'CLONE') == 'a----'
    assert check_correct_letters('TASER', 'STARE') == '-----'
    assert check_correct_letters('RIGHT', 'RIGHT') == '-----'
    
    


def test_check_incorrect_letters():
    assert callable(check_incorrect_letters)
    assert check_incorrect_letters('.....', 'RIGHT') == '.....'
    assert check_incorrect_letters('A....', 'CLONE') == '/....'
    assert check_incorrect_letters('alone', 'CLONE') == '/lone'
    assert check_incorrect_letters('stare', 'taser') == 'stare'
    
    
    

                 
    