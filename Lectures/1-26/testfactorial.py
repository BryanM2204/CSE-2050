from factorial import factorial
import unittest

#unittest.TestCase()

class TestFactorial(unittest.TestCase):
    # factorial test here

    #tests must begin wiith test
    def test_expected(self):
        self.assertEqual(factorial(5), 120)

    def test_edge(self):
        self.assertEqual(factorial(0), 1)

    def test_typing(self):
        #test that I raise a typerror w/ 2.3
        with self.assertRaises(TypeError):
            factorial(2.3)

# class TestSumk(unittest.TestCase):


unittest.main()
