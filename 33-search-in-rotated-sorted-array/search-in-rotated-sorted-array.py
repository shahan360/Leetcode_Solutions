class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if nums is None or len(nums) == 0:
            return -1
        n = len(nums)
        low = 0
        high = n - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            elif nums[low] <= nums[mid]: # Left side is sorted
                if nums[low]<= target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else: # Right side is sorted
                if nums[mid] < target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid -1
        return -1  
        