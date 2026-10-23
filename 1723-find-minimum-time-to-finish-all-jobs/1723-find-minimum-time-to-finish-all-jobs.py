class Solution:
    def minimumTimeRequired(self, jobs: list[int], k: int) -> int:
        jobs.sort(reverse=True)
        left = max(jobs)
        right = sum(jobs)
        def canFinish(limit):
            workers = [0] * k
            def backtrack(i):
                if i == len(jobs):
                    return True
                seen = set()
                for j in range(k):
                    if workers[j] in seen:
                        continue
                    seen.add(workers[j])
                    if workers[j] + jobs[i] <= limit:
                        workers[j] += jobs[i]
                        if backtrack(i + 1):
                            return True
                        workers[j] -= jobs[i]
                    if workers[j] == 0:
                        break
                return False
            return backtrack(0)
        while left < right:
            mid = (left + right) // 2
            if canFinish(mid):
                right = mid
            else:
                left = mid + 1
        return left    