class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        total = 0
        hashmap = {0: 1}  # Initialize with 0 sum having one occurrence
        for num in nums:
            total += num
            # If (total - k) is in hashmap, add its value to count
            if (total - k) in hashmap:
                count += hashmap[total - k]
            # Update hashmap with the current total
            hashmap[total] = hashmap.get(total, 0) + 1
        return count