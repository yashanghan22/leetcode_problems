class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        def remove_pairs(pairs:str,count:int):
            nonlocal s
            res=0
            stack=[]
            for i in s:
                # print(i,stack,pairs)
                if i==pairs[1] and stack and stack[-1]==pairs[0]:
                    print(i,stack,pairs)
                    stack.pop()
                    res+=count
                else:
                    stack.append(i)
            s="".join(stack)
            return res
        count=0
        pairs='ab' if x>y else 'ba'
        count+=remove_pairs(pairs,max(x,y))
        count+=remove_pairs(pairs[::-1],min(x,y))
        return count

if __name__=='__main__':
    s=Solution()
    print(s.maximumGain('cdbcbbaaabab',4,5))
    print(s.maximumGain('aabbaaxybbaabb',5,4))