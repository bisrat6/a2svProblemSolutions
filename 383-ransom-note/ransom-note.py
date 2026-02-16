class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        frq=Counter(magazine)
        for i in ransomNote:
            if frq.get(i,0)==0:
                return False
            else:
                frq[i]-=1
        return True
        