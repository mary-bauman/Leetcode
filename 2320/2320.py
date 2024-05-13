class Solution:
    def countHousePlacements(self, n: int) -> int:
        fib = [1, 2]
        while len(fib) <= n:
            fib.append(fib[-1] + fib[-2])
        return (fib[n]**2) % (10**9 + 7)
