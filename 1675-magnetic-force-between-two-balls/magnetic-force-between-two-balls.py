class Solution:
    def maxDistance(self, position, m):
        position.sort()

        def can_place(distance):
            count = 1  # first ball placed
            last = position[0]

            for i in range(1, len(position)):
                if position[i] - last >= distance:
                    count += 1
                    last = position[i]
                    if count >= m:
                        return True
            return False

        left, right = 1, position[-1] - position[0]

        while left < right:
            mid = (left + right + 1) // 2
            if can_place(mid):
                left = mid
            else:
                right = mid - 1

        return left