class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # Brute Force
        # Time Complexity: O(n^2)
        # Space Complexity: O(1)
        # count = 0
        # for i in range(len(nums)):
        #     total = 0
        #     for j in range(i, len(nums)):
        #         total += nums[j]
        #         if total == k:
        #             count += 1
        # return count
    
        # Optimized using HashMap
        # Time Complexity: O(n)
        # Space Complexity: O(n)
        count = 0 # humne count variable ko 0 se initialize kiya hai kyunki humne abhi tak koi bhi subarray nahi dekha hai jiski sum k ke barabar ho (we kept count variable initialized to 0 because we haven't seen any subarray with sum equal to k yet)
        total = 0 # total variable ko 0 se initialize kiya hai kyunki humne abhi tak koi bhi element nahi dekha hai (we kept total variable initialized to 0 because we haven't seen any element yet)
        hashmap = {0: 1}  # Initialize with 0 sum having one occurrence # humne ye hashmap banaya hai jisme 0 sum ki ek occurrence hai, kyunki agar total k ke barabar ho jaye to hum count ko increase kar sakte hain (we created this hashmap with one occurrence of 0 sum because if total becomes equal to k, we can increase the count)
        # Iterate through the array
        for num in nums: # humne nums array ke har element par num variable ko iterate kiya hai (we iterated through each element of the nums array)
            total += num # total variable mein current element ko add kiya hai (we added the current element to the total variable)
            # If (total - k) is in hashmap, add its value to count
            if (total - k) in hashmap: # agar (total - k) hashmap mein hai to hum uski value ko count mein add karte hain (if (total - k) is in hashmap, we add its value to count)
                count += hashmap[total - k] # humne count ko increase kiya hai kyunki humne ek aur subarray dekha hai jiska sum k ke barabar hai (we increased count because we found another subarray whose sum is equal to k)
            # Update hashmap with the current total
            hashmap[total] = hashmap.get(total, 0) + 1 # humne hashmap mein current total ko update kiya hai, agar total pehle se hai to uski value ko 1 se increase kiya hai, warna 1 set kiya hai (we updated the hashmap with the current total, if total is already present, we increased its value by 1, otherwise set it to 1)
        return count # humne count ko return kiya hai jo ki subarrays ka count hai jinka sum k ke barabar hai (we returned count which is the count of subarrays whose sum is equal to k)