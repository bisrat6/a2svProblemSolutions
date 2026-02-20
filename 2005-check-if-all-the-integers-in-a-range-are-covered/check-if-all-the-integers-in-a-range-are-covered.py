class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        for i in range(left,right+1):
            check=False
            for j in ranges:
                if j[0]<=i<=j[1]:
                    check=True
                    break
            if not check:
                return False
        return True
