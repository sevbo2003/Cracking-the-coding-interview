# 1232. Check If It Is a Straight Line


class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        # y = kx + b
        x1, y1 = coordinates[0][0], coordinates[0][1]

        dx = x1 - coordinates[1][0]
        dy = y1 - coordinates[1][1]

        for cr in coordinates:
            x, y = cr
            x, y = x1 - x, y1 - y
            if dx * y != dy * x:
                return False

        return True


class Solution2:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        # y = kx + b
        x1, y1 = coordinates[0]
        x2, y2 = coordinates[1]

        try:
            k = (y1 - y2) / (x1 - x2)
            b = y1 - k * x1
            # equation = k * x + b
            for cr in coordinates:
                x, y = cr
                eq = k * x + b
                if eq != y:
                    return False
        except ZeroDivisionError:
            for cr in coordinates:
                x, y = cr
                if x != x1:
                    return False

        return True

