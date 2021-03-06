import unittest
from src.game_function import *

class TestBuzzGame(unittest.TestCase):

    def setUp(self):
        self.input_1 = 1
        self.input_2 = 3
        self.input_3 = 5
        self.input_4 = 15
        self.input_5 = 7

    def test_first_input(self):
        self.assertEqual(1, fizz_buzz_game(self.input_1))

    def test_second_input(self):
        self.assertEqual("Fizz", fizz_buzz_game(self.input_2))
        
    def test_third_input(self):
        self.assertEqual("Buzz", fizz_buzz_game(self.input_3))

    def test_fourth_input(self):
        self.assertEqual("Fizz Buzz", fizz_buzz_game(self.input_4))

    def test_fifth_input(self):
        self.assertEqual(7, fizz_buzz_game(self.input_5))