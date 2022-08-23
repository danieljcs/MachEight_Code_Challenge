import unittest
import itertools

from function import var_sum

class TestStringMethods(unittest.TestCase):
    def test_pairs_numbers(self):
        my_list = [1,9,5,0,20,-4,12,16,7]
        for x,y in itertools.combinations(list(set(my_list)), 2):
            if (x + y) == var_sum:
                self.assertIs((x + y), var_sum)


if __name__ == '__main__':
    unittest.main()