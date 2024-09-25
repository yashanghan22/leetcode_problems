from typing import List

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        res=s
        lst=set()
        for i in dictionary:
            if  i in res:
                res = res.replace(i, '')
                # print(s)
            # print(list(i))
            # lst.update(list(i))
        # total_dict=set()
        # total_dict.update(lst)
        print(res)
        return len(res)


if __name__=='__main__':
    s = Solution()
    print(s.minExtraChar("leetscode", ["leet","code","leetcode"]))  