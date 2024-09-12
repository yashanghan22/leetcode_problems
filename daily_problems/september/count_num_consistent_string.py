from typing import List

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        set_words=[set(i) for i in words ]
        print(set_words)
        count=0
        for i in set_words:
            if i.issubset(set(allowed)):
                count+=1
        return count


if __name__=='__main__':
    s = Solution()
    print(s.countConsistentStrings('cad',["cc","acd","b","ba","bac","bad","ac","d"]))
    # print(s.countConsistentStrings('abc',["a","b","c","ab","ac","bc","abc"]))
    # print(s.countConsistentStrings('ab',["ad","bd","aaab","baa","badab"]))