class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        left=0
        right=len(skill)-1
        chem=0
        constant=skill[left]+skill[right]
        while left<right:
            if skill[left]+skill[right]!=constant:
                return -1
            chem+=skill[left]*skill[right]
            right-=1
            left+=1
        return chem