class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        # We are given an array of integers and a number k, we need to find the number of unique k-diff pairs in the array
        if k < 0:
            return 0
        if k == 0:
            # If k is 0, we need to find the number of elements that appear more than once in the array
            from collections import Counter
            count = Counter(nums)
            return sum(1 for v in count.values() if v > 1)
        # If k is greater than 0, we need to find the number of unique pairs
        seen = set()
        pairs = set()
        for num in nums:
            if num - k in seen:
                pairs.add((num - k, num))
            if num + k in seen:
                pairs.add((num, num + k))
            seen.add(num)
        return len(pairs)
        