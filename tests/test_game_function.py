import unittest

class TestBuzzGame(unittest.TestCase):

    def setUp(self):
        input_1 = 1
        input_2 = 3
        input_3 = 5
        input_4 = 15

    def test_first_input(self):
        self.assertEqual(1, fizz_buzz_game(input_1))