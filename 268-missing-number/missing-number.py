class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # n = len(nums)
        # total = (n * (n + 1)) // 2
        # return total - sum(nums)

        nums.sort()
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == mid:
                left = mid + 1
            else:
                right = mid - 1
        return left  # The missing number is at the position 'left'
        