import unittest
import test

class Testing(unittest.TestCase):
    
    def test_1(self):
        self.assertTrue(test.sayHi() == 'hello')
        
    def test_2(self):
        self.assertFalse(test.sayHi() == 'hello')

        
if __name__ == '__main__':
    unittest.main()
