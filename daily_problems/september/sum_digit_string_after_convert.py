class Solution:
    def getLucky(self, s: str, k: int) -> int:
        val={
            'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,
            'g':7,'h':8,'i':9,'j':10,'k':11,'l':12,
            'm':13,'n':14,'o':15,'p':16,'q':17,'r':18,
            's':19,'t':20,'u':21,'v':22,'w':23,'x':24,
            'y':25,'z':26
        }
        current_str=''
        cur_val=[]
        for i in s:
            # print(s)
            cur_val.append(str(val[i]))
        current_str=''.join(cur_val)
        total=0
        for j in range(k):
            cur_total=0
            for l in current_str:
                cur_total+=int(l)
            current_str=str(cur_total)
            total=cur_total
        # print(cur_val)
        return total

if __name__=='__main__':
    s = Solution()
    print(s.getLucky("leetcode", 2))  # Output: 0