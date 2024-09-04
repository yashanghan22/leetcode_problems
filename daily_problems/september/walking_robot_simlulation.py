from typing import List

class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        x, y = 0, 0
        direction = [[0,1],[1,0],[0,-1],[-1,0]]
        i=0
        res=0
        obstacles={tuple(o) for o in obstacles}
        print(obstacles)    
        for c in commands:
            if c==-1:
                i=(i+1)%4
            elif c==-2:
                i=(i-1)%4
            else:
                dx,dy=direction[i]
                for _ in range(c):
                    if (x+dx,y+dy) in obstacles:
                        break
                    x,y=dx+x,dy+y
            res=max(res,x**2+y**2)
        print(x,y)
        return res


if __name__=='__main__':
    s = Solution()
    print(s.robotSim([4,-1,4,-2,4],[[2,4]]))