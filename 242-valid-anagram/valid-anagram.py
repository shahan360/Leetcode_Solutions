class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Brute Force Approach
        # return sorted(s) == sorted(t)

        # Optimized Approach using Counter
        # from collections import Counter
        # if len(s) != len(t):
        #     return False
        # return Counter(s) == Counter(t)

        # Optimized approach using dictionary

        # Step 1: check if the length are unequal, if they are return False as unequal strings can't be anagrams
        if len(s) != len(t):
            return False
        
        count = {}
        for ch in s:
            count[ch] = count.get(ch, 0) + 1
        for ch in t:
            if ch not in count or count[ch] == 0:
                return False
            count[ch] -= 1
        return True
