from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag_count = Counter(magazine)
        for char in ransomNote:
            if mag_count[char] == 0:
                return False
            mag_count[char] -= 1
        return True
        