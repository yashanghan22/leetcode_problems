from typing import List

class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count=0
        for i in details:
            if int(i[11:-2])>60:
                count+=1
            # print(int(i[11:-2]))
        return count

if __name__=="__main__":
    s = Solution()
    print(s.countSeniors(["7868190130M7522","5303914400F9211","9273338290F4010"]))