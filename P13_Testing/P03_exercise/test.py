import unittest
import script


class testGame(unittest.TestCase):
    def test_game(self):
        result = script.run_guess(5, 5)
        self.assertTrue(result)

    def test_game2(self):
        result = script.run_guess(0, 5)
        self.assertFalse(result)

    def test_game3(self):
        result = script.run_guess(15, 4)
        self.assertFalse(result)

    def test_game4(self):
        result = script.run_guess(0, '4')
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
