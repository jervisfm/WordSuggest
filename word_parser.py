
__author__ = 'Jervis Muindi'
__date__ = 'October 2013'

"""This module contains code for splitting text into individual
word tokens."""

def get_sample_text():
    path = "test_input.txt"
    content = ""
    with open(path,"r") as f:
        content = f.read()
    
    return content


class TextStream(object):
    """A stream of textual characters."""
    pass

class WordParser(object):
    """Responsible for extracting words from a stream of text.
    
    This will be implemented as a state machine. 

                                               / - - alpha-numeric character
    Start  non-whitespace character           |     |
    State     ->                         Reading< - |
         whitespace and punctuation  character
               <-

    When we transition from Reading to Start State, whatever is in the
    buffer will be considered a word. 
    """
    
    PUNCTUATION = [".", ";", "?", ",", "!", "&", "(", ")", ":"]

class WordCount(object):
    """Includes a count for how often a word appears."""
    def __init__(self, word, count):
        if not word:
            raise ValueError("Word not specified")

        if not count:
            count = 0

        self.word = word
        self.count = count

    def incrementCount(self):
        self.count += 1

def test():
    print get_sample_text()


def main():
    test()

if __name__ == '__main__':
    main()
