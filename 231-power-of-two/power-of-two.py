class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0: # Base case: agar n 0 ya usse chhota hai, toh wo power of two nahi ho sakta. (If n is less than or equal to 0, it cannot be a power of two.)
            return False # Agar n 0 ya usse chhota hai, toh return False. (If n is less than or equal to 0, return False.)
        if n == 1: # Base case: agar n 1 hai, toh wo power of two hai. (If n is 1, it is a power of two.)
            return True # Agar n 1 hai, toh return True. (If n is 1, return True.)
        # Recursive case: agar n 2 se divide ho sakta hai, toh hum n ko 2 se divide karte hain aur function ko dobara call karte hain. (If n can be divided by 2, we divide n by 2 and call the function again.)
        if n % 2 != 0: # Agar n 2 se divide nahi ho sakta, toh wo power of two nahi hai. (If n is not divisible by 2, it is not a power of two.)
            return False # Agar n 2 se divide nahi ho sakta, toh return False. (If n is not divisible by 2, return False.)
        # Agar n 2 se divide ho sakta hai, toh hum n ko 2 se divide karte hain aur function ko dobara call karte hain. (If n can be divided by 2, we divide n by 2 and call the function again.)
        return self.isPowerOfTwo(n // 2) # Hum n ko 2 se divide karte hain aur function ko dobara call karte hain. (We divide n by 2 and call the function again.)

# Visualizing the recursion tree:
# isPowerOfTwo(8)
# ├── isPowerOfTwo(4)
# │   └── isPowerOfTwo(2)
# │       └── isPowerOfTwo(1)
# │           └── True