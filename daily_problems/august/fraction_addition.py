from math import gcd

class Solution:
    def fractionAddition(self, expression: str) -> str:
        numer = 0
        denom = 1
        i = 0
        while i < len(expression):
            sign = 1
            if expression[i] == '-' or expression[i] == '+':
                if expression[i] == '-':
                    sign = -1
                i += 1
            
            j = i
            while expression[i] != '/':
                i += 1
            numerator = sign * int(expression[j:i])
            
            i += 1
            j = i
            while i < len(expression) and expression[i].isdigit():
                i += 1
            denominator = int(expression[j:i])
            
            numer = numer * denominator + numerator * denom
            denom = denom * denominator
            
            common_divisor = gcd(abs(numer), denom)
            numer //= common_divisor
            denom //= common_divisor
        
        return f'{numer}/{denom}'


if __name__=='__main__':
    s = Solution()
    print(s.fractionAddition('1/3-1/2'))
    print(s.fractionAddition('-1/2+1/2'))
    # print(s.fractionAddition('-1/2+1/2+1/3'))