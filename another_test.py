import unittest

def FizzBuzz(number):
    if number % 15 == 0:
        return 'FizzBuzz'
    if number % 5 == 0:
        return 'Buzz'
    if number % 3 == 0:
        return 'Fizz'
    return number

class TestFizzBuzz(unittest.TestCase):
#if the number is divisible by 3 then we should return 'Fizz'
    def test_3_is_Fizz(self):
        self.assertEqual(FizzBuzz(3), 'Fizz')
    def test_6_is_Fizz(self):
        self.assertEqual(FizzBuzz(6), 'Fizz')
#if the number is divisible by 5 then we should return 'Buzz'
    def test_5_is_Buzz(self):
        self.assertEqual(FizzBuzz(5), 'Buzz')
    def test_10_is_Buzz(self):
        self.assertEqual(FizzBuzz(10), 'Buzz')
#if the number is divisible by 15 then we should return 'FizzBuzz'
    def test_15_is_Fizz(self):
        self.assertEqual(FizzBuzz(15), 'FizzBuzz')
    def test_30_is_FizzBuzz(self):
        self.assertEqual(FizzBuzz(30), 'FizzBuzz')
#if another number then we return the number itself
    def test_1_returns_1(self):
        self.assertEqual(FizzBuzz(1), 1)

    def test_2_returns_2(self):
        self.assertEqual(FizzBuzz(2), 2)


if __name__ == '__main__':
    unittest.main(warnings='ignore')
