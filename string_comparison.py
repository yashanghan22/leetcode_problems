
from collections import defaultdict
from typing import List

class Solution:
    def compress(self, chars: List[str]) -> int:
        dic=defaultdict(int)
        for i in range(len(chars)):
            dic[chars[i]]=dic[chars[i]]+1
        lst=[]
        for u,v in dic.items():
            lst.append(str(u))
            if v>0:
                lst.append(str(v))
        b=''.join(lst)
        print(b)
        return len(''.join(lst))

if __name__=='__main__':
    s=Solution()
    print(s.compress(["a","a","b","b","c","c","c"]))