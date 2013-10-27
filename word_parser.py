
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
    
    def __init__(self, file_path=None, data=None):
        """ Creates a TextStream from given arguments.

        Only one argument should be specified, and not both. 

        Specifying both arguments is taken as an error and will
        raise a ValueError. 
        
        Args:
           file_path: A file path to a text file. 
           data: A data string with the data. 
        """

        if not (file_path or data):
            raise ValueError("Must specify non-empty file_path or data args.")
        
        
        if file_path:
            self.f = open(file_path, "r")
        elif data:
            # Create a File-like object from a String using StringIO
            self.f = StringIO.StringIO(data)
        

        if not file_path:
            raise ValueError("File Path not given")

        self.char_pos = 0
        self.line = ""

    def get_character(self):
        """Retrieves the next charatcer from the text stream
           or None if EOF. """
        if not self.line:
            # next() will raise StopIteration when EOF is hit.
            try:
                self.line = self.f.next()
            except StopIteration:
                return None
        if self.char_pos < len(self.line):
            char = self.line[self.char_pos]
            self.char_pos += 1
            return char
        else: # we have exhausted our line-cache
            # Reset our line and char position tracker
            self.line = ""
            self.char_pos = 0
            return self.get_character()


class WordParser(object):
    """Responsible for extracting words from a stream of text.
    
    This will be implemented as a finite state machine. 

                                               / - -  alpha-numeric character
    Start  non-whitespace character           |      \
    State     ->                         Reading < - |
           non-alphanumeric character
           except a few characters (e.g. "-")
           which are not considered word-terminators. 
               <-

    When we transition from Reading to Start State, whatever is in the
    buffer will be considered a word. 
    """
    
    PUNCTUATION = (".", ";", "?", ",", "!", "&", "(", ")", ":")

    def __init__(self, text_stream):
        if not text_stream:
            raise ValueError("Text Stream not specified")
        self.text_stream = text_stream
        self.prev_word = ""
        self.curr_word = ""

    def _update_prev_word(self, new_word):
        """Updates the previous/current word pairing."""
        if self.curr_word:
            self.prev_word = self.curr_word
        self.curr_word = new_word

    def _get_word(self):
        """Gets the next word from the stream."""
        global PUNCTUATION
        READING_STATE = 'READING'
        INIT_STATE = 'INIT STATE'
        state = INIT_STATE
        char_buffer = ""
        non_word_delimeters = ["-", "'"]
        sentence_delimeters = [".", ";", ":"]
        while(True):
            char = self.text_stream.get_character()
            
            if char is not None:
                if state == INIT_STATE:
                    # Skip whitespace and non-alphanumeric characters.
                    if char.isspace() or not char.isalnum():
                        continue
                    else:
                        state = READING_STATE
                        char_buffer += char
                elif state == READING_STATE:
                    # Read until we hit whitespace character or 
                    # non-alpha numeric character with the exeption of
                    #  some chars which are not considered to mark end of a word. 
                    
                    if (not char in non_word_delimeters and 
                        (char.isspace() or  not char.isalnum())):
                        # If character is a sentence terminator/delimeter
                        # include it, so that future clients know this
                        # was the last word. 
                        if char in sentence_delimeters:
                            char_buffer += char
                        
                        return char_buffer
                    else:
                        char_buffer += char
                
            else: # End of stream
                return char_buffer

    @staticmethod
    def normalize_word(word):
        """Nomarlizes the given word by removing whitespace and converting to lowercase."""
        if not word:
            return ""

        return word.strip().lower()

    def get_word(self):
        new_word = self._get_word()
        new_word = self.normalize_word(new_word)
        self._update_prev_word(new_word)
        return new_word

    def get_word_pair(self):
        """Gets the next word pair from the stream.

        This should respect sentence boundaries such that
        that we don't give a word-pair that cross sentence
        boundaries.

        For example in the text: 

        "Hello World. Welcome Back."
        
        Word Pairs are:
        <Hello, World>
        <Welcome, Back>

        And it does not include

        <World, Welcome>

        The same should apply with the ";" and ":" punctuation characters.
        """
        
        # We use the fact that the word token retain the sentence punctuation delimeters
        # to determine where the sentence boundaries are in. 
        sentence_delimeters = [".", ";", ":"]
        while True:
            self.get_word()
            prev = self.prev_word
            curr = self.curr_word
            
            # previous word is empty, proceed ahead. 
            # this is the case at the very beggining, when we start
            # parsing a text stream. 
            if not prev:
                continue

            # Skip word Pairs in which the previous words with
            # a sentence punctuation (e.g. '.', ';' etc). This represents
            # A cross-sentence barrier word pair. 
            last_char = prev[-1]
            if last_char in sentence_delimeters:
                continue

            return (prev,curr)
        
        
            
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
    num_chars = 200
    print 'trying to get %s chars' % num_chars
    for _ in xrange(num_chars):
        print ts.get_character()


def main():
    test()

if __name__ == '__main__':
    main()
