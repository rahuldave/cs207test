
import unittest

from mymath import mysum

class MyTest(unittest.TestCase):
    
    def test_mymath(self):
        self.assertEqual(mysum(2,3), 5)

if __name__ == '__main__':
    unittest.main()