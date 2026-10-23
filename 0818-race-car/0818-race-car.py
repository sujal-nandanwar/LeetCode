class Solution:
    def racecar(self, target: int) -> int:
        dp = [0] * (target + 1)
        for i in range(1, target + 1):
            n = i.bit_length()
            if (1 << n) - 1 == i:
                dp[i] = n
            else:
                dp[i] = n + 1 + dp[(1 << n) - 1 - i]
                for m in range(n - 1):
                    forward = (1 << (n - 1)) - 1
                    backward = (1 << m) - 1
                    remaining = i - (forward - backward)
                    dp[i] = min(
                        dp[i],
                        (n - 1) + 1 + m + 1 + dp[remaining]
                    )
        return dp[target]
