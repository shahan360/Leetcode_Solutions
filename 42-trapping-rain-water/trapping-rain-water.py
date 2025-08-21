class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left = 0              # left pointer
        right = n - 1         # right pointer
        left_max = 0          # ab tak ki left wali max height
        right_max = 0         # ab tak ki right wali max height
        ans = 0               # total pani ka amount

        while left < right:
            # Left side ki height kam hai
            if height[left] < height[right]:
                if height[left] >= left_max:
                    left_max = height[left]      # Left max update karo
                else:
                    ans += left_max - height[left]   # Pani add karo
                left += 1
            else:
                # Right side ki height kam hai
                if height[right] >= right_max:
                    right_max = height[right]    # Right max update karo
                else:
                    ans += right_max - height[right] # Pani add karo
                right -= 1

        return ans  # Output: Total trapped pani