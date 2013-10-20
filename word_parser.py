
__author__ = 'Jervis Muindi'
__date__ = 'October 2013'

"""This module contains code for splitting text into individual
word tokens."""

def get_sample_text():
    path = "test_input.txt"
    content = ""
    with open(path,"r") as f:
        content = f.read(1)
    
    return content


class TextStream(object):
    """A stream of textual characters."""
    
    def __init__(self, file_path):
        if not file_path:
            raise ValueError("File Path not given")

        self.f = open(file_path, "r")
        self.char_pos = 0
        self.line = ""

    def get_character(self):
        """Retrieves the next charatcer from the text stream"""
        if not self.line:
            # next() will raise StopIteration when EOF is hit.
            self.line = self.f.next()
        
        if self.char_pos < len(self.line):
            char = self.line[self.char_pos]
            self.char_pos += 1
            return char
        else: # we have exhausted our line-cache
            # Reset our lines/position tracker
            self.line = ""
            self.char_pos = 0
            return self.get_character()


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

    def increment_count(self):
        self.count += 1

def test():
    file_path = "test_input.txt"
    ts = TextStream(file_path)
    print 'created ts'
    num_chars = 15
    print 'trying to get %s chars' % num_chars
    for _ in xrange(num_chars):
        print ts.get_character()


def main():
    test()

if __name__ == '__main__':
    main()
