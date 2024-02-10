def productExceptSelf(nums):
    n = len(nums)
    
    # Initialize two arrays to store products to the left and right of each element
    left_products = [1] * n
    right_products = [1] * n

    # Calculate products to the left of each element
    left_product = 1
    for i in range(1, n):
        left_product *= nums[i - 1]
        left_products[i] = left_product

    # Calculate products to the right of each element
    right_product = 1
    for i in range(n - 2, -1, -1):
        right_product *= nums[i + 1]
        right_products[i] = right_product

    # Calculate the final product by multiplying left and right products for each element
    output = [left_products[i] * right_products[i] for i in range(n)]

    return output

# Driver code
if __name__ == "__main__":
    # Example usage
    nums = [1, 2, 3, 4]
    result = productExceptSelf(nums)
    print(f"Product of Array Except Self: {result}")
