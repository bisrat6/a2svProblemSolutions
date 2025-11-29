class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        def isVowel(a:str)->bool:
            if a=='a' or a=='i' or a=='u' or a=='e' or a=='o':
                return True
            else: False
        count=0
        i=0
        while i<k:
            if isVowel(s[i]):
                count+=1
            i+=1
        temp=count
        for i in range(k,len(s)):
            if isVowel(s[i]):
                temp+=1
            if isVowel(s[i-k]):
                temp-=1
            count=max(count,temp)
        return count
        
