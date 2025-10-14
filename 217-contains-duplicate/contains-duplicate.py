class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Brute Force Approach
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[j]==nums[i]:
        #             return True
        # return False

        # Optimized Approach using set to store numbers
        # Create a set to store unique numbers
        unique_nums = set()
        # iterate over the array
        for n in nums:
            # check if element n already in set
            if n in unique_nums:
                # if yes then return True as the array contains duplicates
                return True
            # if the element n is not already in set and uniquely new then add it to the set
            unique_nums.add(n)
        # if there are no duplicate elements then return False
        return False 