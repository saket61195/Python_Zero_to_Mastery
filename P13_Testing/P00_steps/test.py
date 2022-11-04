import unittest
import script


class TestMain(unittest.TestCase):
    def test_do_stuff(self):
        test_param = 10
        result = script.do_stuff(test_param)
        self.assertEqual(result, 15)
        # self.assertEqual(result, 11) #changing value show error to fix


unittest.main()


# python3 test.py
