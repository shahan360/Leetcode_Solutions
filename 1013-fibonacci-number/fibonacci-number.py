class Solution:
    def fib(self, n: int) -> int:
        # Base case: if n is 0, return 0
        if n == 0: # Agar n 0 hai, toh wo Fibonacci number 0 hai. (If n is 0, the Fibonacci number is 0.)
            return 0 # Agar n 0 hai, toh return 0. (If n is 0, return 0.)
        # Base case: if n is 1, return 1
        elif n == 1: # Agar n 1 hai, toh wo Fibonacci number 1 hai. (If n is 1, the Fibonacci number is 1.)
            return 1 # Agar n 1 hai, toh return 1. (If n is 1, return 1.)
        # Recursive case: return the sum of the two previous Fibonacci numbers
        else: # Agar n 2 se bada hai, toh hum Fibonacci number ko n-1 aur n-2 ke Fibonacci numbers ka sum karte hain. (If n is greater than 1, we return the sum of the Fibonacci numbers at positions n-1 and n-2.)
            return self.fib(n - 1) + self.fib(n - 2) # Hum n-1 aur n-2 ke Fibonacci numbers ka sum karte hain. (We return the sum of the Fibonacci numbers at positions n-1 and n-2.)

# Visualizing the recursion tree:
# fib(5)
# ├── fib(4) + fib(3)
# │   |        ├── fib(2) + fib(1)
# │   │        |   |        └── 1
# │   │        │   ├── fib(1) + fib(0)
# │   │        │   │   └── 1 +  └── 0
# │   ├── fib(3) + fib(2)
# │   │   |        ├── fib(1) + fib(0)
# │   │   │            └── 1 +  └── 0
# │   │   ├── fib(2) + fib(1)
# │   │   │   |        ├── fib(1) + fib(0)
# │   │   │   │            └── 1 +  └── 0
# │   │   │   ├── fib(1) + fib(0)
# │   │   │   │   └── 1 +  └── 0 
        