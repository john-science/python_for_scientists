"""Complete the main method in this script,
by completing the methods described."""

from pprint import pprint

FILENAME = 'fat_kakapo.txt'
DOUGLAS_ADAMS_QUOTE = '''The kakapo is an extremely fat bird.
A good-sized adult will weigh about six or seven pounds,
and its wings are just about good for waggling a bit
if it thinks it's about to trip over something — but flying is out of the question.
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
    exit('The function "write_quote_2_file" is unfinished.')
    
    return lines


def read_quote_file(filename):
    """This function takes in a file name and returns a list of strings,
    where each line in the file is a element in the output list"""
    exit('The function "read_quote_file" is unfinished.')
    
    return lines


def remove_non_letters(lines):
    """This function takes in a list of strings that contain and
    returns that same list where all the non-letter characterss have been removed.
    
    Input Example: ['Arrakis 1!', 'Paul Atreides', 'Spice...']
    Output Example: ['Arrakis', 'PaulAtreides', 'Spice']
    """
    for line in lines:
        exit('The function "remove_non_letters" is unfinished.')
    
    return lines


def make_lowercase(lines):
    """This function takes in a list of strings that contain only letters and
    returns that same list where all the letters are lowercase.
    
    Input Example: ['Arrakis', 'PaulAtreides', 'Spice']
    Output Example: ['arrakis', 'paulatreides', 'spice']
    """
    for line in lines:
        exit('The function "make_lowercase" is unfinished.')
    
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
        exit('The function "count_letters" is unfinished.')
    
    return d

def print_letter_dict(d):
    pprint(d)


if __name__ == '__main__':
    main()
