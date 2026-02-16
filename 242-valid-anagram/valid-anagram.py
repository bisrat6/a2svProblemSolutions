class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic={}
        for i in s:
            if i not in dic:
                dic[i]=1
            else:
                dic[i]+=1
        for i in t:
            if i not in dic or dic[i]<=0:
                return False
            else:
                dic[i]-=1
        for value in dic.values():
            if value>0:
                return False
        return True