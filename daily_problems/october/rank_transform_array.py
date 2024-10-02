from typing import List

class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        sort_list=sorted(set(arr))
        rank_dict={sort_list[i]:i+1 for i in range(len(sort_list))}
        return [rank_dict[x] for x in arr]


if __name__=='__main__':
    s=Solution()
    print(s.arrayRankTransform([40, 10, 20, 30]))