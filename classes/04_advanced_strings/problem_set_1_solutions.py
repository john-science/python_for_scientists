"""Complete the main method in this script,
by completing the methods described."""

from pprint import pprint

FILENAME = 'fat_kakapo.txt'
DOUGLAS_ADAMS_QUOTE = '''The kakapo is an extremely fat bird.
A good-sized adult will weigh about six or seven pounds,
and its wings are just about good for waggling a bit
if it thinks it's about to trip over something - but flying is out of the question.
Sadly, however, it seems that not only has the kakapo forgotten how to fly,
but it has forgotten that it has forgotten how to fly.
Apparently a seriously worried kakapo will sometimes run up a tree and jump out of it,
whereupon it flies like a brick and lands in a graceless heap on the ground.
'''


def main():
    # write the Douglas Adams quote to a simple text file
    write_quote_2_file(FILENAME, DOUGLAS_ADAMS_QUOTE)
    
    # read the file in again, as a series of strings, one for each line
    lines = read_quote_file(FILENAME)
    
    # remove all characters from each string that aren't letters
    lines = remove_non_letters(lines)
    
    # make all letters in each string lower case
    lines = make_lowercase(lines)
    
    # finally, create a dictionary that has the count of each letter in the quote
    letter_count_dict = count_letters(lines)
    
    # print the result
    print_letter_dict(letter_count_dic)


def write_quote_2_file(filename, text):
    """This function takes in a file name and a string and writes
    the contents of that string to the file name given."""
    f = open(filename, 'w')
    f.write(text)
    f.close()


def read_quote_file(filename):
    """This function takes in a file name and returns a list of strings,
    where each line in the file is a element in the output list"""
    f = open(filename, 'r')
    lines = f.readlines()
    f.close()
    
    return lines


def remove_non_letters(lines):
    """This function takes in a list of strings that contain numbers and other
    non-letter characters and returns a list where all the non-letter
    characters have been removed.
    
    Input Example: ['Arrakis 1!', 'Paul Atreides', 'Spice...\n']
    Output Example: ['Arrakis', 'PaulAtreides', 'Spice']
    """
    for i, line in enumerate(lines):
        new_line = ''
        for c in line:
            if c.isalpha():
                new_line += c
        lines[i] = new_line
        
    return lines


def make_lowercase(lines):
    """This function takes in a list of strings that contain only letters and
    returns that same list where all the letters are lowercase.
    
    Input Example: ['Arrakis', 'PaulAtreides', 'Spice']
    Output Example: ['arrakis', 'paulatreides', 'spice']
    """
    for i, line in enumerate(lines):
        lines[i] = line.lower()
    
    return lines


def count_letters(lines):
    """This function takes in a list of strings and returns a dictionary
    where the keys are letters of the alphabet and values are the number of occurences
    of that letter in the list.
    
    Input Example: lines = ['arrakis', 'paulatreides', 'spice']
    Output Example: {'a': 4, 'c': 1, 'e': 3, 'd': 1, 'i': 3, 'k': 1,
                     'l': 1, 'p': 2, 's': 3, 'r': 3, 'u': 1, 't': 1}
    """
    d = {}
    
    for line in lines:
        for c in line:
            if c not in d:
                d[c] = 0
            d[c] += 1
    
    return d

def print_letter_dict(d):
    pprint(d)


if __name__ == '__main__':
    main()
