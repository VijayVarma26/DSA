import math
import unittest

# Kadanes Algorithm 
def max_subarray_sum(array):
    max_sum = -math.inf
    con_sum = 0
    for i in array:
        con_sum += i
        max_sum = max(max_sum, con_sum)
        if con_sum < 0:
            con_sum = 0
    return max_sum

class TestMaxSubarraySum(unittest.TestCase):

    def test_max_subarray_sum(self):
        self.assertEqual(max_subarray_sum([1, 2, 3, 4, 5]), 15)
        self.assertEqual(max_subarray_sum([-1, -2, -3, -4, -5]), -1)
        self.assertEqual(max_subarray_sum([1, -2, 3, 4, -1, 2, 1, -5, 4]), 9)
        self.assertEqual(max_subarray_sum([1]), 1)
        self.assertEqual(max_subarray_sum([]), -math.inf)

if __name__ == '__main__':
    unittest.main()