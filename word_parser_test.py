
__author__ = 'Jervis Muindi'
__date__ = 'October 2013'

import unittest
import StringIO

from word_parser import TextStream
from word_parser import WordParser


TEXT_INPUT = "test_input.txt"

class TextStreamTest(unittest.TestCase):

    def setUp(self):
        global TEXT_INPUT
        self.sample_input_file = TEXT_INPUT

    
    def test_get_character(self):
        file_path = self.sample_input_file
        
        # Read file to get expected content(s)
        expected_content = ""
        with open(file_path, "r") as f:
            expected_content = f.read()

        # Use TextStream to read file
        ts = TextStream(file_path)
        actual_content = ""
        while True:
            char = ts.get_character()
            if char is not None:
                actual_content += char
            else: # End of stream
                break
        self.assertEqual(actual_content, expected_content, 
                         msg="Expected: %s \n Vs Actual: %s" % (expected_content,actual_content))


class WordParserTest(unittest.TestCase):

    def setUp(self):
        global TEXT_INPUT
        self.sample_input_file = TEXT_INPUT
    
    def get_words_from_file(self, file_path):
        contents = ""
        with open(file_path, "r") as f:
            contents = f.read()

        words = contents.split()
        
        # Our WordParser including terminating punctuations in words
        # so that sentence termination can be determined, so no need
        # to do any filtering here.
    
        # However, need to apply same word normalization as
        # The word parser does.
        return map(WordParser.normalize_word, words)

        
    def test_get_word(self):
        
        # Get all the words in text input file.
        file_path = self.sample_input_file
        expected_words = self.get_words_from_file(file_path)
        
        
        # Now try to use WordParser to extract words

        text_stream = TextStream(file_path)
        parser = WordParser(text_stream)
        actual_words = []
        while True:
            word = parser.get_word()
            if word:
                actual_words.append(word)
            else:
                break
        self.assertTrue(actual_words == expected_words,
                        msg="Expected: %s \nActual: %s" %
                        (expected_words, actual_words))


    def test_get_word_pair(self):
        # TODO(jervis): implement test to verify this works as expected.
        data = "This is a sentence. Hello. World. Good bye; See you later."
        expected_pairs = [("this", "is"), 
                          ("is", "a"),
                          ("a", "sentence"),
                          ("good", "bye"),
                          ("see", "you"),
                          ("you", "later")]
        text_stream = TextStream(data=data)
        parser = WordParser(text_stream)
        actual_pairs = []
        while True:
            pair = parser.get_word_pair()
            if not pair:
                break
            actual_pairs.append(pair)
            
        # Check that the sizes match
        actual_size = len(actual_pairs)
        expected_size = len(expected_pairs)
        self.assertTrue(actual_size == expected_size, 
                        msg="Expected Size: %s but got %s" % 
                        (expected_size, acutal_size))
            
        # Verify contents match
        for expected,actual in zip(expected_pairs, actual_pairs):
            self.assertTrue(expected == actual,
                            msg="Expected %s but got %s" % 
                            (expected,actual))

if __name__ == '__main__':
    unittest.main()
    
