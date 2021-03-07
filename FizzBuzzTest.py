import unittest
import FizzBuzz
i=0
result=FizzBuzz.FizzBuzz()


class TeastCase(unittest.TestCase):
    def test1(self):
        self.assertEqual(result[0],"FizzBuzz")
    def test3(self):
        self.assertTrue(result,1)


            
    
if __name__ == '__main__':
    unittest.main()
