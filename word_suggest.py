

__author__ = 'Jervis Muindi'
__date__ ='October 2013'


from word_parser import TextStream
from word_parser import WordParser

class WordSuggestBuilder(object):
    """Analyzes input textual data to build a datastructure that will be useful to make
    suggested word recommendations given a candidate input word. 
    """

    def __init__(self, text_stream):
    """Creates a word suggest builder object.

    Args:
        text_stream: A WordParser.TextStream object. It contains the text 
        stream to use for building up the word suggestions. 
    """
        if not text_stream:
            raise ValueError("text stream must be specified")

        if not isinstance(text_stream, TextStream):
            raise TypeError("text stream must be of type word_parser.TextStream")

        
        self.text_stream = text_stream
        self.parser = WordParser(text_stream)
        

    def process_input(self):
        """Process the text stream input to generate a 
        dictionary of: word ->  { word -> word_count } for each
        word pair in the text stream."""
        pass
        
