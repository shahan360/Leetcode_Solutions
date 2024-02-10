def longestPalindrome(s):
    n = len(s)
    
    # Create a 2D table to store whether substrings are palindromes
    is_palindrome = [[False] * n for _ in range(n)]

    # All substrings of length 1 are palindromes
    for i in range(n):
        is_palindrome[i][i] = True

    start = 0  # Start index of the longest palindrome
    max_length = 1  # Length of the longest palindrome

    # Check substrings of length 2 and more
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1

            # For a substring to be a palindrome, the characters at the ends must be equal
            # and the substring between them must be a palindrome
            if length == 2 and s[i] == s[j]:
                is_palindrome[i][j] = True
                start = i
                max_length = length
            elif s[i] == s[j] and is_palindrome[i + 1][j - 1]:
                is_palindrome[i][j] = True
                start = i
                max_length = length

    return s[start:start + max_length]

# Driver code
if __name__ == "__main__":
    # Example usage
    input_str = "babad"
    result = longestPalindrome(input_str)
    print(f"Longest palindromic substring: {result}")
