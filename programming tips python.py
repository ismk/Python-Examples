"""

# Let's learn about basic unittest in Python

import unittest


class Test(unittest.TestCase):

    def test_basic_addition(self):
        # in here we are testing that 1+1 is always equal to 2
        self.failUnlessEqual(1 + 1, 2)


if __name__ == '__main__':
    unittest.main()


"""

s = "mary had a little lamb"
