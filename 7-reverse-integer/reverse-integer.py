class Solution:
    def reverse(self, x: int) -> int:
        INT_MAX = 2**31 - 1  # 2147483647
        INT_MIN = -2**31     # -2147483648

        sign = 1 if x >= 0 else -1
        n = abs(x)
        rev = 0

        while n > 0:
            pop = n % 10
            n = n // 10

            if rev > INT_MAX // 10 or (rev == INT_MAX // 10 and pop > 7):
                return 0

            rev = rev * 10 + pop

        return sign * rev if INT_MIN <= sign * rev <= INT_MAX else 0
        