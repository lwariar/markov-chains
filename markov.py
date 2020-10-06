"""Generate Markov text from text files."""
import sys
import random
from random import choice

def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """
    contents = open(file_path).read()
    return contents


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains('hi there mary hi there juanita')

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """
    # your code goes here
    text_string = text_string.split()
    chains = {}
  
    for i in range(len(text_string) - 2):
        chains_key = (text_string[i], text_string[i + 1])
        chains_value = text_string[i+2]
        
        if chains_key not in chains:
            chains[chains_key] = []
            
        chains[chains_key].append(chains_value)
    
    return chains


def make_text(chains):
    """Return text from chains."""

    words = []

    # your code goes here
    random_key = random.choice(list(chains))
    words = [random_key[0], random_key[1]]
    random_value = choice(chains[random_key])

    while random_value is not None:
        words.append(random_value)
        random_key = (random_key[1], random_value)
        if random_key in chains:
            random_value = choice(chains[random_key])
        else:
            break        

    return ' '.join(words)


input_path = 'green-eggs.txt'

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
