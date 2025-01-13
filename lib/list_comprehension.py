#!/usr/bin/env python3

# Function definitions
def return_evens(num_list):
    """Returns a list of even numbers from the input list."""
    return [num for num in num_list if num % 2 == 0]

def make_exclamation(sentence_list):
    """Appends an exclamation mark to each sentence in the input list."""
    return [sentence + "!" for sentence in sentence_list]

# Test classes
class TestReturnEvens:
    '''function return_evens()'''

    def test_return_empty_list_if_odds(self):
        '''returns empty list when num_list has no evens'''
        num_list = range(1, 10, 2)
        assert return_evens(num_list) == []

    def test_return_evens(self):
        '''returns evens from num_list'''
        num_list = range(10)
        assert return_evens(num_list) == [0, 2, 4, 6, 8]

class TestMakeExclamation:
    '''function make_exclamation()'''

    def test_return_empty_list_if_empty_input(self):
        '''returns empty list when sentence_list is empty'''
        assert make_exclamation([]) == []

    def test_return_exclamation_list(self):
        '''returns list of sentences with exclamation marks'''
        sentence_list = [
            "I like computers",
            "I require coffee",
            "Live long and prosper",
        ]
        assert make_exclamation(sentence_list) == [
            "I like computers!",
            "I require coffee!",
            "Live long and prosper!",
        ]
