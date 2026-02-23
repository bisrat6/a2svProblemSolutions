class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic={}
        for i in strs:
            sorted_word = "".join(sorted(i, key=str.lower))
            if dic.get(sorted_word) is None:
                dic[sorted_word]=[i]
            else:
                dic[sorted_word].append(i)
        result = [i for i in dic.values()]
        return result

       
