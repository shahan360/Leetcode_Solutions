def sortColors(nums):
    left, right, current = 0, len(nums) - 1, 0

    while current <= right:
        if nums[current] == 0:
            # Swap current with left
            nums[current], nums[left] = nums[left], nums[current]
            left += 1
            current += 1
        elif nums[current] == 2:
            # Swap current with right
            nums[current], nums[right] = nums[right], nums[current]
            right -= 1
        else:
            # Move to the next element
            current += 1

# Driver code
if __name__ == "__main__":
    # Example usage
    nums = [2, 0, 2, 1, 1, 0]
    sortColors(nums)
    print(f"Sorted Colors: {nums}")
