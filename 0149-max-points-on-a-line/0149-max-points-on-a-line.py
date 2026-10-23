class Solution:
    def maxPoints(self, points: list[list[int]]) -> int:
        n = len(points)
        if n <= 2:
            return n
        result = 0
        for i in range(n):
            slopes = {}
            duplicate = 0
            current_max = 0
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                dx = x2 - x1
                dy = y2 - y1
                if dx == 0 and dy == 0:
                    duplicate += 1
                    continue
                var1 = abs(dx)
                var2 = abs(dy)
                while var2 != 0:
                    var1, var2 = var2, var1 % var2
                g = var1
                dx //= g
                dy //= g
                if dx < 0 or (dx == 0 and dy < 0):
                    dx = -dx
                    dy = -dy
                slope = (dy, dx)
                if slope not in slopes:
                    slopes[slope] = 0
                slopes[slope] += 1
                current_max = max(current_max, slopes[slope])
            result = max(result, current_max + duplicate + 1)
        return result


        