class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        result = []
        result.append(nums[0])
        for i in range(1,len(nums)):
            result.append(result[i-1] + nums[i])
        return result

'''
The error occurs because you are trying to assign a value to an index in the list result[i] that does not exist yet. You need to use append() instead of assigning by index after the first element.
'''