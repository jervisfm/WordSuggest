

__author__ = 'Jervis Muindi'
__date__ ='October 2013'


from word_parser import TextStream
from word_parser import WordParser
from word_parser import WordCount

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
        dictionary of: current_word ->  { next_word -> WordCount Object } for each
        word pair in the text stream."""

        parser = self.parser
        result = {}
        # TODO(jervis): Current processing assumes that the output
        # will fit in memory. For really large datasets, this assumption
        # won't be true; will need to work with that. In that scenario, 
        # it would be simplest to actually just write all word pairs to disk
        # and sort them using external merge sort. This will be slow due to 
        # the sorting; may be worthwhile to consider alternative faster approaches. 
        while True:
            curr, next = parser.get_word_pair()

            if not next:
                # We're done
                break
        
            if curr in result:
                # Retrieve and use the existing value dict
                value_dict = result[curr]
                
                # Check if this subseqeuent word already exists
                if next in value_dict:
                    # Then just update the running count
                    word_count = value_dict[next]
                    word_count.count += 1
                else:
                    # Create a new word count
                    word_count = WordCount(next, 1)
                    value_dict[next] = word_count
            else:
                # Make a new word count.
                word_count = WordCount(next, 1)
                
                # Since key didn't exist before, we need 
                # to create the value dict. 
                value_dict = {}
                value_dict[curr] = word_count
                result[curr] = value_dict
        return result
