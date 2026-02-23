class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic=Counter(nums)
        sorted_keys = sorted(dic, key=lambda k: dic[k],reverse=True)
        result=[]
        count=k
        for i in sorted_keys:
            if count==0:
                break
            result.append(i)
            count-=1
        return result