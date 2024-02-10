def subarray_sum_equals_k(nums, k):
    # Dictionary to store the cumulative sum and its frequency
    cum_sum_freq = {0: 1}
    count = 0
    cum_sum = 0

    for num in nums:
        cum_sum += num
        # Check if there is a cumulative sum (cum_sum - k) in the dictionary
        if cum_sum - k in cum_sum_freq:
            # Add the frequency of that cumulative sum to the count
            count += cum_sum_freq[cum_sum - k]

        # Update the frequency of the current cumulative sum
        cum_sum_freq[cum_sum] = cum_sum_freq.get(cum_sum, 0) + 1

    return count

# Driver code
if __name__ == "__main__":
    # Example usage
    nums = [1, 2, 3, 4, 5]
    k = 9
    result = subarray_sum_equals_k(nums, k)
    print(f"Number of subarrays with sum {k}: {result}")
