'''
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
 

Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The input is generated such that answer[i] is guaranteed to fit in a 32-bit integer.
 

Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)


'''

# Solution
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # The length of the input array
        length = len(nums)

        # The left and right arrays as described in the algorithm
        L, R, answer = [0] * length, [0] * length, [0] * length

        # L[i] contains the product of all the elements to the left
        # Note: for the elemnt at index '0', there are no elements to the left,
        # so the L[0] would be 1
        L[0] = 1
        for i in range(1, length):
            # L[i-1] already contains the product of elements to the left of 'i-1'
            # Simply multiplying it with nums[i-1] would give the product of all elements to the left of index 'i'
            L[i] = nums[i-1]*L[i-1]

        # R[i] contains the product of all the elements to the right
        # Note: for the element at index 'length - 1', there are no elements to the right, so the R[length -1] would be 1
        R[length - 1] = 1
        for i in reversed(range(length - 1)):
            # R[i+1] already contains the product of elements to the right of 'i+1'
            # Simply multiplying it with nums[i+1] would give the product of all elements to the right of index 'i'
            R[i] = nums[i+1] * R[i+1]

        # Constructing the answer array
        for i in range(length):
            answer[i] = L[i]*R[i]

        return answer            
    
'''
Dry Run:

Here's a step-by-step dry run of the productExceptSelf algorithm using nums = as an example:

Step 1: Initialize Arrays
text
nums = [1,2,3,4]
L    = [1,0,0,0]  # Left products
R    = [0,0,0,1]  # Right products
answer = [0,0,0,0]

Step 2: Calculate Left Products (L)
text
Index 0: L[0] = 1 (base case)
Index 1: L[1] = nums[0] * L[0] = 1*1 = 1
Index 2: L[2] = nums[1] * L[1] = 2*1 = 2
Index 3: L[3] = nums[2] * L[2] = 3*2 = 6

Final L = [1,1,2,6]

Step 3: Calculate Right Products (R)
text
Index 3: R[3] = 1 (base case)
Index 2: R[2] = nums[3] * R[3] = 4*1 = 4
Index 1: R[1] = nums[2] * R[2] = 3*4 = 12
Index 0: R[0] = nums[1] * R[1] = 2*12 = 24

Final R = [24,12,4,1]

Step 4: Calculate Answer Array
text
Index 0: 1 * 24 = 24
Index 1: 1 * 12 = 12
Index 2: 2 * 4 = 8
Index 3: 6 * 1 = 6

Final answer = [24,12,8,6]
Visualization
text
Original Array: [1,  2,  3,  4]
Left Products:  [1,  1,  2,  6]
Right Products: [24, 12, 4,  1]
Final Answer:   [24, 12, 8,  6]
Key Operations
Left Pass → Build cumulative product from left to right

Right Pass → Build cumulative product from right to left

Combine → Multiply corresponding left/right products

This approach achieves O(n) time complexity with O(n) space, avoiding division and handling zeros naturally.

'''    