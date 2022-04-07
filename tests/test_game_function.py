import unittest
from src.game_function import *

class TestBuzzGame(unittest.TestCase):

    def setUp(self):
        self.input_1 = 1
        self.input_2 = 3
        self.input_3 = 5
        self.input_4 = 15

    def test_first_input(self):
        self.assertEqual(1, fizz_buzz_game(self.input_1))

    def test_second_input(self):
        self.assertEqual("Fizz", fizz_buzz_game(self.input_2))