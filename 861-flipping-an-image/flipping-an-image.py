class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for i in image:
            i.reverse()
            for idx in range(len(i)):
                if i[idx]==0:
                    i[idx]=1
                else:
                    i[idx]=0
        return image
