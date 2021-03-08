import unittest
import LeapYear
i=0
result=LeapYear.leapyear()


class TestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual(result,True)




if __name__ == '__main__':
    unittest.main()
