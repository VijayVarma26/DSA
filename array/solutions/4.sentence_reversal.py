import unittest


# List Slicing Technique avoid this in an interview
def reverse_sentence_list_slicing(str):
    str = str.strip().split()
    return " ".join(str[::-1])

# Iterating over list
def reverse_sentence_iterating(str):
    str = str.strip().split()
    reversed_str = ""
    for i in range(len(str)-1, -1, -1):
        reversed_str += str[i] + " "
    return reversed_str.strip()

class TestReverseSentence(unittest.TestCase):
    def test_reverse_sentence(self):
        self.assertEqual(reverse_sentence_list_slicing("Hello World"), "World Hello")
        self.assertEqual(reverse_sentence_list_slicing("  Hello   World  "), "World Hello")
        self.assertEqual(reverse_sentence_list_slicing("a b c d"), "d c b a")
        self.assertEqual(reverse_sentence_list_slicing(""), "")
        self.assertEqual(reverse_sentence_list_slicing("   "), "")
        self.assertEqual(reverse_sentence_list_slicing("single"), "single")

        self.assertEqual(reverse_sentence_iterating("Hello World"), "World Hello")
        self.assertEqual(reverse_sentence_iterating("  Hello   World  "), "World Hello")
        self.assertEqual(reverse_sentence_iterating("a b c d"), "d c b a")
        self.assertEqual(reverse_sentence_iterating(""), "")
        self.assertEqual(reverse_sentence_iterating("   "), "")
        self.assertEqual(reverse_sentence_iterating("single"), "single")

if __name__ == '__main__':
    unittest.main()