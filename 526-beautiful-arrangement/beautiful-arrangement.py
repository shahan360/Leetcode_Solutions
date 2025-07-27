class Solution:
    def countArrangement(self, n: int) -> int:
        count = 0
        used = [False] * (n+1)

        def backtrack(i):
            nonlocal count
            if i > n:
                count += 1
                return
        
            for num in range(1, n+1):
                if not used[num] and (num%i==0 or i%num==0):
                    used[num] = True
                    backtrack(i+1)
                    used[num] = False
        
        backtrack(1)
        return count
        