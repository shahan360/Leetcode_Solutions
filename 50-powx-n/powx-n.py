class Solution:
    def myPow(self, x: float, n: int) -> float:
        # Base case: if n is 0, return 1
        if n == 0:
            return 1
        # If n is negative, convert it to positive and take the reciporcal of x
        elif n < 0:
            n = -n
            x = 1 / x
        # Recursive case: if n is even, return the square of the result of myPow
        if n % 2 == 0:
            half = self.myPow(x, n // 2)
            return half * half
        # If n is odd, return x multiplied by the result of myPow
        else:
            return x * self.myPow(x, n - 1)

# Visualizing the recursion tree:
# myPow(2, 10)
# ├── myPow(2, 5)
# │   ├── myPow(2, 2)
# │   │   ├── myPow(2, 1)
# │   │   │   ├── myPow(2, 0)
# │   │   │   │   └── 1
# │   │   │   └── 2
# │   │   └── 4
# │   └── 8
# └── 1024