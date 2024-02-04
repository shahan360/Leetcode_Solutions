class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Initialize pointers for binary search
        left, right = 0, len(nums) - 1
        
        # Perform binary search
        while left < right:
            mid = (left + right) // 2
            
            # Check if the minimum element is in the left or right half
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
                
        # The minimum element is at the 'left' index
        return nums[left]