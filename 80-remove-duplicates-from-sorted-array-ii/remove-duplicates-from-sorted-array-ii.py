class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = {}
        result = []
        k = 2
        for num in nums:
            if num not in count:
                count[num] = 0
            if count[num] < k:
                result.append(num)
                count[num] += 1
        nums[:] = result
        return len(result)