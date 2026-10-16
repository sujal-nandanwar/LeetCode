
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        dp = [0] * n
        result = 0

        for i in range(1, n):
            if s[i] == ')':
                if s[i - 1] == '(':
                    if i >= 2:
                        dp[i] = dp[i - 2] + 2
                    else:
                        dp[i] = 2
                else:
                    var1 = i - dp[i - 1] - 1
                    if var1 >= 0 and s[var1] == '(':
                        dp[i] = dp[i - 1] + 2
                        if var1 >= 1:
                            dp[i] += dp[var1 - 1]

            result = max(result, dp[i])

        return result

