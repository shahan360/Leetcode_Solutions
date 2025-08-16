class Solution:
    def isArmstrong(self, n: int) -> bool:
        pow_a = len(str(n))
        sum_a = 0
        original = n
        while n > 0:
            sum_a = sum_a + ((n%10)**pow_a)
            n = n//10
        if original == sum_a:
            return True
        return False