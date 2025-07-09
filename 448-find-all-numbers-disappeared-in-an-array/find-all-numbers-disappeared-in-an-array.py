class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)  # Store the length of the array in n
        result = []  # Create an empty list for the result
        nums.sort()  # Sort the array to make it easier to find missing numbers
        i = 0 # Initialize index i to 0
        for num in range(1, n + 1):  # Check numbers from 1 to n
            if i >= n or nums[i] > num:
                # If i is out of bounds or the current number in nums is greater than num,
                # it means num is missing in the array
                result.append(num)
            else:
                # If the current number in nums is equal to num, move to the next index
                while i < n and nums[i] == num:
                    i += 1
        return result  # Return the list of missing numbers
        