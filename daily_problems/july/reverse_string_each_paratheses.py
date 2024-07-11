class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        for c in s:
            if c == ')':
                p=[]
                while stack[-1]!='(':
                    p.append(stack.pop())
                stack.pop()
                stack.extend(p)
            else:
                stack.append(c)
        print(stack)
        return "".join(stack)


if __name__=='__main__':
    s = Solution()
    print(s.reverseParentheses("(u(love)i)"))