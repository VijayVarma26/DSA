### Problem Statement: Array Pair Sum

Write a function to find all pairs of integers in an array whose sum is equal to a given target value. The function should return the pairs or their count based on the specified requirement.

---

### Input:  
1. An array of integers, `nums`.  
2. An integer, `target`, representing the target sum.

---

### Output:  
A list of unique pairs (or the count of such pairs) whose sum equals the target value.

---

### Constraints:  
1. Each pair must use two different elements from the array.  
2. A number can only be used once per pair.  
3. If the array contains duplicates, the same number can be used in multiple pairs as long as the above rules are followed.  
4. The order of pairs in the output does not matter.  
5. If no pairs exist, return an empty list (or 0 for the count).

---

### Examples:

#### Example 1:
- **Input:** `nums = [1, 2, 3, 4, 5]`, `target = 6`  
- **Output:** `[(1, 5), (2, 4)]`  
**Explanation:** The pairs `(1, 5)` and `(2, 4)` add up to 6.

#### Example 2:
- **Input:** `nums = [1, 2, 2, 3]`, `target = 4`  
- **Output:** `[(1, 3), (2, 2)]`  

#### Example 3:
- **Input:** `nums = [1, 1, 1]`, `target = 2`  
- **Output:** `[(1, 1)]`  
**Explanation:** The only valid pair is `(1, 1)`.

#### Example 4:
- **Input:** `nums = [1, 2, 3]`, `target = 7`  
- **Output:** `[]`  
**Explanation:** No pairs add up to 7.

