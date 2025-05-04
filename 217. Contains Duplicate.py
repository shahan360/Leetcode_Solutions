'''
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

 

Example 1:

Input: nums = [1,2,3,1]

Output: true

Explanation:

The element 1 occurs at the indices 0 and 3.

Example 2:

Input: nums = [1,2,3,4]

Output: false

Explanation:

All elements are distinct.

Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]

Output: true

 

Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109
'''

# Solution
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Create an empty set to store unique numbers seen so far
        nums_set = set()
        # Iterate through each number in the input list
        for n in nums:
            # If the number is already in the set, we've found a duplicate
            if n in nums_set:
                return True
            # Otherwise, add the number to the set
            nums_set.add(n)
        # If we finish the loop without finding duplicates, return False
        return False

"""
Dry Run Example:
Input: nums = [1, 2, 3, 4, 1]

Step-by-step:
- Initialize nums_set = {}

Iteration 1: n = 1
    - 1 not in nums_set
    - Add 1 to nums_set → nums_set = {1}

Iteration 2: n = 2
    - 2 not in nums_set
    - Add 2 to nums_set → nums_set = {1, 2}

Iteration 3: n = 3
    - 3 not in nums_set
    - Add 3 to nums_set → nums_set = {1, 2, 3}

Iteration 4: n = 4
    - 4 not in nums_set
    - Add 4 to nums_set → nums_set = {1, 2, 3, 4}

Iteration 5: n = 1
    - 1 is already in nums_set
    - Return True (duplicate found)

Output: True
"""
