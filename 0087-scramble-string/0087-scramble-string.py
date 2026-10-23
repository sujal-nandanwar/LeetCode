from functools import lru_cache
class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False
        @lru_cache(None)
        def solve(s1, s2):
            if s1 == s2:
                return True
            if sorted(s1) != sorted(s2):
                return False
            n = len(s1)
            for i in range(1, n):
                if solve(s1[:i], s2[:i]) and solve(s1[i:], s2[i:]):
                    return True
                if solve(s1[:i], s2[n-i:]) and solve(s1[i:], s2[:n-i]):
                    return True
            return False
        return solve(s1, s2)