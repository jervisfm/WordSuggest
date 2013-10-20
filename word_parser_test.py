
__author__ = 'Jervis Muindi'
__date__ = 'October 2013'

import unittest

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
        
        # Drop  last "." if present
        result = []
        for word in words:
            if word[-1] == ".":
                word = word[:-1]
                result.append(word)
            else:
                result.append(word)
                
        return result

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


if __name__ == '__main__':
    unittest.main()
    
