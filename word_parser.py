
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
        """Retrieves the next charatcer from the text strea 
           or NOne if EOF. m"""
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
    
    PUNCTUATION = (".", ";", "?", ",", "!", "&", "(", ")", ":")

    def __init__(self, text_stream):
        if not text_stream:
            raise ValueError("Text Stream not specified")
        self.text_stream = text_stream
    
    

    def get_word():
        """Gets the next word from the stream."""
        global PUNCTUATION
        READING_STATE = 'READING'
        INIT_STATE = 'INIT STATE'
        state = INIT_STATE
        char_buffer = ""
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
                    non_word_delimeters = ["-", "'"]
                    if (not char in non_word_delimeters and 
                        (char.isspace() or  not char.isalnum()))):
                        return char_buffer
                    else:
                        char_buffer += char
                
            else: # End of stream
                return char_buffer
            
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
