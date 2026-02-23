class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)
        for i in strs:
            sorted_word = "".join(sorted(i.lower()))
            dic[sorted_word].append(i)
        result = [i for i in dic.values()]
        return result

       
