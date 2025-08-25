from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # Magazine ke characters ka count lo (Count characters in magazine)
        mag_count = Counter(magazine)
        
        # Har character ko ransomNote me check karo (Check each character in ransomNote)
        for char in ransomNote:
            # Agar magazine me wo character available nahi hai to false return karo 
            # (If character not available in magazine, return False)
            if mag_count[char] == 0:
                return False
            
            # Character use kar liya to count ko ek se kam karo (Decrement count after using character)
            mag_count[char] -= 1
        
        # Agar sab characters mil gaye to true return karo (If all characters found, return True)
        return True
