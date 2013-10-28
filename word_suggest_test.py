
__author__ = 'Jervis Muindi'
__date__ = 'October 2013'

import unittest
import StringIO

from word_parser import TextStream
from word_suggest import WordSuggestBuilder

TEXT_INPUT = "test_input.txt"

class WordSuggestTest(unittest.TestCase):

    def setUp(self):
        global TEXT_INPUT
        self.sample_input_file = TEXT_INPUT

    def test_get_word_pair(self):
        # TODO(jervis): implement test to verify this works as expected.
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


if __name__ == '__main__':
    unittest.main()
    
