from typing import List

class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        res=0
        ls=[]
        n=len(skill)
        skill.sort()
        total=skill[0]+skill[-1]
        l,r=0,n-1
        while l<r:
            if skill[l]+skill[r]==total:
                ls.append((skill[l],skill[r]))
            else:
                return -1
            l+=1
            r-=1
        for i in ls:
            res+=(i[0]*i[1])
        return res


if __name__=='__main__':
    s=Solution()
    print(s.dividePlayers([3,2,5,1,3,4]))