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
    str1 = str1.replace(" ", "")
    str2 = str2.replace(" ", "")

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