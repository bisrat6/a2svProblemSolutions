class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words=s.split(' ')
        if len(words)!=len(pattern):return False
        dic={}
        for a,b in zip(pattern,words):
            if dic.get(a,0)==0 and b not in dic.values():
                dic[a]=b
            elif dic.get(a,0)==0 and b in dic.values():
                return False
            else:
                if dic[a]!=b:
                    return False
        return True