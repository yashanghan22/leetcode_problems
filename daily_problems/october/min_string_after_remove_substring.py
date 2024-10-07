class Solution:
    def minLength(self, s: str) -> int:
        n = s
        while n.__contains__('AB') or n.__contains__('CD'):
            n = n.replace('AB', '').replace('CD', '')

        return len(n)

if __name__=='__main__':
    s=Solution()
    print(s.minLength('ABFCACDB'))