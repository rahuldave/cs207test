
from mymath import myaverage, mymedian

import unittest

class MyTest(unittest.TestCase):
    
    def test_mymath(self):
        self.assertEqual(myaverage([2,3]), 2.5)
        
    def test_char(self):
        with self.assertRaises(TypeError):
            myaverage(['a',3])
            
    def test_zerol(self):
        with self.assertRaises(ValueError):
            myaverage([])