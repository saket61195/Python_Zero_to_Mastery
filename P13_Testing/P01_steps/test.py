import unittest
import script


class TestMain(unittest.TestCase):
    def test_do_stuff(self):
        test_param = 10
        result = script.do_stuff(test_param)
        self.assertEqual(result, 15)
        
    def test_do_stuff1(self):
        test_param = 'ghh'
        result = script.do_stuff(test_param)
        # self.assertEqual(result,15)
        # self.assertEqual(result,ValueError)
        # self.assertTrue(isinstance(result,ValueError))
        self.assertIsInstance(result,ValueError)


unittest.main()


# python3 test.py
