class Solution:
    def longestPalindrome(self, s: str) -> int:
        # # Brute force Approach
        # # Time Complexity: O(n^3)
        # # Space Complexity: O(1)
        # max_length = 0 # humne max_length ko 0 se initialize kiya hai kyunki abhi tak humne koi bhi palindrome nahi dekha hai (we initialized max_length to 0 because we haven't seen any palindrome yet)
        # for i in range(len(s)): # hum string ke har index par iterate karte hain (we iterate through each index of the string)
        #     for j in range(i, len(s)): # hum current ith index se lekar end ke index tak j variable ko iterate karte hain (we iterate through the j variable from the current ith index to the end of the string)
        #         substring = s[i:j + 1] # humne substring ko current ith index se lekar jth index tak banaya hai (we created a substring from the current ith index to the jth index)
        #         if substring == substring[::-1]: # agar substring palindrome hai to hum max_length ko update karte hain (if the substring is a palindrome, we update max_length)
        #             max_length = max(max_length, j - i + 1) # humne max_length ko update kiya hai (we updated max_length)
        # return max_length # hum max_length ko return karte hain (we return max_length)
        
        # Optimized Approach: Using a hashmap to count character frequencies
        # Time Complexity: O(n)
        # Space Complexity: O(1) (since we only use a fixed-size hashmap for 52 letters)
        char_count = {}
        for char in s: # hum string ke har character par iterate karte hain (we iterate through each character in the string)
            char_count[char] = char_count.get(char, 0) + 1 # humne character ki frequency ko update kiya hai (we updated the frequency of the character)
        length = 0 # humne length ko 0 se initialize kiya hai (we initialized length to 0)
        odd_found = False # humne odd_found ko False se initialize kiya hai (we initialized odd_found to False)
        for count in char_count.values(): # humne character count ki values par iterate kiya hai (we iterate through the values of character count)
            if count % 2 == 0: # agar count even hai to hum length ko update karte hain (if the count is even, we update the length)
                length += count # humne length ko count se update kiya hai (we updated the length with the count)
            else: # agar count odd hai to hum length ko update karte hain (if the count is odd, we update the length)
                length += count - 1 # humne length ko count - 1 se update kiya hai (we updated the length with count - 1)
                odd_found = True # humne odd_found ko True set kiya hai (we set odd_found to True)
        if odd_found: # agar koi odd count mila hai to hum length ko 1 se badhate hain (if we found any odd count, we increase the length by 1)
            length += 1 # humne length ko 1 se badhaya hai (we increased the length by 1)
        return length # hum length ko return karte hain (we return the length)