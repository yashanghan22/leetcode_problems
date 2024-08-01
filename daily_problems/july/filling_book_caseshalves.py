from typing import List

class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        cache={}
        def hepler(i):
            if i==len(books):
                return 0
            if i in cache:
                return cache[i]
            cur_width=shelfWidth
            max_height=0
            cache[i]=float('inf')
            for j in range(i,len(books)):
                width,height=books[j]
                if cur_width<width:
                    break
                cur_width-=width
                max_height=max(max_height,height)
                cache[i]=min(cache[i],hepler(j+1)+max_height)
            return cache[i]
        return hepler(0)

if __name__=='__main__':
    books = [[1,1],[2,3],[2,3],[1,1],[1,1],[1,1],[1,2]]
    s=Solution()
    print(s.minHeightShelves(books,4))