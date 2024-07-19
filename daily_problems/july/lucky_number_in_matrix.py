from typing import List

class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        res=[]
        m = len(matrix)
        n = len(matrix[0])
        max_of_rows_mins=float('-inf')
        for row in range(m):
            row_min=min(matrix[row])
            max_of_rows_mins=max(row_min,max_of_rows_mins)
        
        for col in range(n):
            col_max=matrix[0][col]
            for i in range(m):
                col_max=max(col_max,matrix[i][col])
            if col_max==max_of_rows_mins:
                return [col_max]
        return []


if __name__=='__main__':
    s=Solution()
    print(s.luckyNumbers([[1,10,4,2],[9,3,8,7],[15,16,17,12]]))
    print(s.luckyNumbers([[3,7,8],[9,11,13],[15,16,17]]))