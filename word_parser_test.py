
__author__ = 'Jervis Muindi'
__date__ = 'October 2013'

import unittest

from word_parser import TextStream

class TextStreamTest(unittest.TestCase):

    def setUp(self):
        self.sample_input_file = "test_input.txt"

    
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


if __name__ == '__main__':
    unittest.main()
    
