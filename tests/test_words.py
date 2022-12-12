import unittest
from ..src import words as words
# import words.words as words

class TestWords(unittest.TestCase):

    def test_reverse_words(self):
        result = words.reverse_words("Pluto")
        self.assertEqual(result, "otulP")
        
    def test_two_words(self):
        result = words.two_words("is")
        self.assertEqual(result, "IS")




        # result = calculator.minus(-2, -3)
        # self.assertEqual(result, 1)




