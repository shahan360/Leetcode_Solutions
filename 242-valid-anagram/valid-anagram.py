class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Brute Force Approach
        # return sorted(s) == sorted(t)

        # Optimized Approach using hashmap
        from collections import Counter
        if len(s) != len(t):
            return False
        return Counter(s) == Counter(t)
