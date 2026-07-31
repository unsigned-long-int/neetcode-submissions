class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        fib = [1, 2]
        i = 2
        while i < n:
            fib.append(fib[i-1] + fib[i-2])
            i += 1

        return fib[-1]