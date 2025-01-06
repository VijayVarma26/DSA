import unittest

# Two strings are anagram of each other if 

# This implementation uses sorting and uses the sorted strings to check if they are equal
def check_anagram_using_sorting(str1, str2):
    str1 = str1.replace(" ", "")
    str2 = str2.replace(" ", "")

    list1 = list(str1.lower().strip())
    list2 = list(str2.lower().strip())

    list1.sort()
    list2.sort()

    return list1 == list2


# This implementation uses counting the frequency of each character in the string
def check_anagram_using_counting(str1, str2):
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    if len(str1) != len(str2):
        return False
    
    seen = {}
    for char in str1:
        if char in seen:
            seen[char] += 1
        else:
            seen[char] = 1

    for char in str2:
        if char in seen:
            seen[char] -= 1
        else:
            return False
        
    for key in seen:
        if seen[key] != 0:
            return False

    return True

class TestAnagramCheck(unittest.TestCase):

    def test_check_anagram_using_sorting(self):
        self.assertTrue(check_anagram_using_sorting("listen", "silent"))
        self.assertTrue(check_anagram_using_sorting("triangle", "integral"))
        self.assertFalse(check_anagram_using_sorting("apple", "pale"))
        self.assertTrue(check_anagram_using_sorting("A gentleman", "Elegant man"))
        self.assertFalse(check_anagram_using_sorting("Hell1", "Olelh"))

    def test_check_anagram_using_counting(self):
        self.assertTrue(check_anagram_using_counting("listen", "silent"))
        self.assertTrue(check_anagram_using_counting("triangle", "integral"))
        self.assertFalse(check_anagram_using_counting("apple", "pale"))
        self.assertTrue(check_anagram_using_counting("A gentleman", "Elegant man"))
        self.assertFalse(check_anagram_using_counting("Hell1", "Olelh"))

if __name__ == '__main__':
    unittest.main()