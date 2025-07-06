class Solution:
    def rob(self, nums: List[int]) -> int:
        # Using Recursion
        # def rob_helper(i): # we define a helper function to handle the recursion
        #     if i < 0: # base case, if index is negative, return 0
        #         return 0 # no house to rob
        #     if i == 0: # if we are at the first house, return its value
        #         return nums[0] # rob the first house
        #     # we can either rob the current house and skip the previous one, or skip the current house
        #     # and take the maximum of the two options
        #     return max(rob_helper(i - 1), nums[i] + rob_helper(i - 2))
        # return rob_helper(len(nums) - 1) # call the helper function with the last index

        # Using Dynamic Programming
        if not nums: # if the list is empty, return 0
            return 0 # no house to rob
        n = len(nums) # get the number of houses
        if n == 1: # if there is only one house, return its value
            return nums[0] # rob the only house
        dp = [0] * n # create a dp array to store the maximum amount we can rob up to each house
        dp[0] = nums[0] # we can only rob the first house
        dp[1] = max(nums[0], nums[1]) # we can either rob the first house or the second house, whichever is greater
        for i in range(2, n): # iterate through the houses starting from the third one
            dp[i] = max(dp[i - 1], nums[i] + dp[i - 2]) # we can either skip the current house or rob it and add the maximum from two houses before it
        return dp[-1] # return the maximum amount we can rob from all houses