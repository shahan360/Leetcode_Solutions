class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)  # Store the length of the array in n
        result = [] # Create an empty list for the result
        num_set = set(nums)  # Create a set from the nums array for quick lookup
        for i in range(1, n + 1):
            if i not in num_set:
                # If i is not in the set, it means it's a missing number
                result.append(i)
        return result  # Return the list of missing numbers
        # This approach has a time complexity of O(n) and space complexity of O(n) due to the set.
        