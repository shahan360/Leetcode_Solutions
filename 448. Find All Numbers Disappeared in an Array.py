def findDisappearedNumbers(nums):
    # Iterate through each number in the array
    for num in nums:
        # Use the absolute value to get the index
        index = abs(num) - 1

        # If the value at the calculated index is positive, make it negative
        if nums[index] > 0:
            nums[index] = -nums[index]

    # Collect the indices of positive values (indices + 1 are the missing numbers)
    result = [i + 1 for i in range(len(nums)) if nums[i] > 0]

    return result

# Driver code
if __name__ == "__main__":
    # Example usage
    nums = [4, 3, 2, 7, 8, 2, 1, 1]
    result = findDisappearedNumbers(nums)
    print(f"Numbers Disappeared in Array: {result}")
