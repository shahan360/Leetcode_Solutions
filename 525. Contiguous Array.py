def findMaxLength(nums):
    # Dictionary to store the cumulative sum and its first index
    cum_sum_index = {0: -1}
    max_length = 0
    cum_sum = 0

    for i, num in enumerate(nums):
        # Convert 0 to -1 to simplify the calculation
        cum_sum += 1 if num == 1 else -1

        # Check if the cumulative sum has been encountered before
        if cum_sum in cum_sum_index:
            max_length = max(max_length, i - cum_sum_index[cum_sum])
        else:
            cum_sum_index[cum_sum] = i

    return max_length

# Driver code
if __name__ == "__main__":
    # Example usage
    nums = [0, 1]
    result = findMaxLength(nums)
    print(f"Maximum length of contiguous subarray: {result}")
