class Solution:
    def minSteps(self, s: str, t: str) -> int:
        frq=Counter(s)
        count=0
        for char in t:
            if frq.get(char,0)==0:
                count+=1
            else:
                if frq[char]==0:
                    count+=1
                else:
                    frq[char]-=1
        return count
