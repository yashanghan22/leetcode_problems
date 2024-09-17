from collections import Counter
from typing import List

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        words = s1.split() + s2.split()
    
        freq = Counter(words)
        print(freq)
        res = [word for word in freq if freq[word] == 1]
        
        return res


if __name__=='__main__':
    s1 = "this apple is sweet"
    s2 = "this apple is sour"
    s = Solution()
    print(s.uncommonFromSentences(s1, s2))