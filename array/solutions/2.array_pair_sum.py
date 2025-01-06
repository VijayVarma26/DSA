import unittest

def array_pair_sum(arr, target):
    seen = set()
    output = set()
    for i in arr:
        diff = target - i
        if diff in seen:
            output.add((min(diff, i), max(diff, i)))
        else:
            seen.add(i)

    if output:
        return output
    return None

class TestArrayPairSum(unittest.TestCase):

    def test_array_pair_sum(self):
        self.assertEqual(array_pair_sum([1, 2, 3, 4, 5], 6), {(1, 5), (2, 4)})
        self.assertEqual(array_pair_sum([1, 2, 3, 4, 5], 10), None)
        self.assertEqual(array_pair_sum([1, 2, 3, 4, 5, 5], 10), {(5, 5)})
        self.assertEqual(array_pair_sum([1, 2, 3, 4, 5], 7), {(2, 5), (3, 4)})
        self.assertEqual(array_pair_sum([], 6), None)

if __name__ == '__main__':
    unittest.main()