class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        dic = defaultdict(list)
        for idx, char in enumerate(s):
            dic[char]=idx
        idx_2=0
        init=0
        result=[]
        for idx, char in enumerate(s):
            if idx_2==0 or dic[char]>idx_2:
                idx_2=dic[char]
            if idx==idx_2:
                result.append(idx_2-init+1)
                idx_2=0
                init=idx+1
        return result
            
            

