
__author__ = 'Jervis Muindi'
__date__ = 'October 2013'

import unittest
import StringIO

import word_suggest

from word_parser import TextStream
from word_suggest import WordSuggestBuilder

TEXT_INPUT = "test_input.txt"
SAMPLE_DATA = "This is a sentence. Hello. World. Good bye; See you later. See you soon."

class WordSuggestBuilderTest(unittest.TestCase):

    def setUp(self):
        global TEXT_INPUT
        self.sample_input_file = TEXT_INPUT

    def test_get_word_pair(self):
        data = "This is a sentence. Hello. World. Good bye; See you later. See you soon."

        text_stream = TextStream(data=data)
        suggest = WordSuggestBuilder(text_stream)
        result = suggest.process_input()
        result_string = str(result)

        expected_result = ("{'a': {'sentence': sentence:1}," 
                           " 'good': {'bye': bye:1},"
                           " 'this': {'is': is:1}," 
                           " 'is': {'a': a:1}," 
                           " 'see': {'you': you:2},"
                           " 'you': {'later': later:1, 'soon': soon:1}}")
        
        self.assertTrue(result_string == expected_result, 
                        msg="Expected:\n %s \n But instead got: \n %s" %
                        (expected_result, result_string))


class WordSuggestModuleTest(unittest.TestCase):
    def setUp(self):
        global SAMPLE_DATA
        self.sample_data = SAMPLE_DATA

    def test_suggest_word(self):
        """ Test that doing a suggested word works. """
        data = self.sample_data
        text_stream = TextStream(data=data)
        suggest_dict = WordSuggestBuilder(text_stream).process_input()

        # Test some word suggestions. 
        test_words = ["good","see", "a", "NotAWord"]
        expected_answers = ["bye","you", "sentence", None]

        for word,expected_word in zip(test_words,expected_answers):
            suggestion = word_suggest.suggest_word(suggest_dict, word)
            if expected_word is None:
                self.assertFalse(suggestion, msg="Expected None Result but got %s" % suggestion)
                continue
            self.assertTrue(suggestion.word == expected_word,
                        msg="On Input '%s'; Expected: '%s' but got '%s'. \nSuggest Dict: \n%s" %
                            (word, suggestion.word, expected_word, suggest_dict))

        

if __name__ == '__main__':
    unittest.main()
    
