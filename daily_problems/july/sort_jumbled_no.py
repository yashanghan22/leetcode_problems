from typing import List
from collections import defaultdict

class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        item=defaultdict(int)
        stack =[]
        for i in nums:
            k=len(str(i))
            if i in item:
                stack.append(i)
            else:
                for n in str(i):
                    # print(mapping[int(n)],int(str(1).ljust(k,"0")))
                    item[i]+=(mapping[int(n)]*int(str(1).ljust(k,"0")))
                    k-=1
        print(stack)
        res=[k for k,v in sorted(item.items(),key=lambda arg : (arg[1],-arg[0]))] if len(set(item.values()))>1 else list(item.keys())
        for l in stack:
            inx= res.index(l)
            res.insert(inx,l)
        # print(sorted(item.items(),key=lambda arg : (arg[1],-arg[0])))
        return res

if __name__=='__main__':
    s = Solution()
    # print(s.sortJumbled([8,9,4,0,2,1,3,5,7,6], [991,338,38]))
    print(s.sortJumbled([8,9,4,6,2,1,3,5,7,0], [9,99,999,9999,999999999]))
    # print(s.sortJumbled([8,2,9,5,3,7,1,0,6,4],[418,4191,916,948,629641556,574,111171937,28250,42775632,6086,85796326,696292542,186,67559,2167,366,854,2441,78176,621,4257,2250097,509847,7506,77,50,4135258,4036,59934,59474,3646243,9049356,85852,90298188,2448206,30401413,33190382,968234660,7973,668786,992777977,77,355766,221,246409664,216290476,45,87,836414,40952]))