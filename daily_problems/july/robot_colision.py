from typing import List

class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        indexed_map={p:i for i,p in enumerate(positions)}
        stack=[]
        for p in sorted(positions):
            i=indexed_map[p]
            
            if directions[i]=='R':
                stack.append(i)
            else:
                while stack and directions[stack[-1]]=='R' and healths[i]:
                    i2=stack.pop()
                    if healths[i]>healths[i2]:
                        healths[i2]=0
                        healths[i]-=1
                    elif healths[i]<healths[i2]:
                        healths[i]=0
                        healths[i2]-=1
                        stack.append(i2)
                    else:
                        healths[i]=healths[i2]=0
        return [h for h in healths if h>0]

if __name__=='__main__':
    s = Solution()
    print(s.survivedRobotsHealths([3,47],[46,26],"RL"))
    print(s.survivedRobotsHealths([5,4,3,2,1],[2,17,9,15,10],"RRRRR"))
    print(s.survivedRobotsHealths([3,5,2,6],[10,10,15,12],"RLRL"))
    print(s.survivedRobotsHealths([1,2,5,6],[10,10,11,11],"RLRL"))