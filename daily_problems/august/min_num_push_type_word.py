from collections import defaultdict

class Solution:
    def minimumPushes(self, word: str) -> int:
        res=0
        letter_count=defaultdict(int)
        button_list=defaultdict(list)
        for i in word:
            letter_count[i]+=1
        # print(type(sorted(letter_count.items(),key= lambda kv : kv[1],reverse=True)))
        for i,v in enumerate(sorted(letter_count.items(),key= lambda kv : kv[1],reverse=True)):
            # print(i+1,(i)%8,v)
            button_list[i%8].append(v)
        for k in button_list:
            for l in range(len(button_list[k])):
                res+=(button_list[k][l][1]*(l+1))
                # print(button_list[k][l][1]*(l+1))
        # print(res)
        return res


if __name__=="__main__":
    s=Solution()
    print(s.minimumPushes('aabbccddeeffgghhiiiiii'))