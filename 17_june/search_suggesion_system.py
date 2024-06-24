from typing import List


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        out = []
        products.sort()
        print(out)
        for i in range(1, len(searchWord)+1):
            lst = []
            word = searchWord[:i]
            for k in products:
                if len(lst) < 3 and k.__contains__(word):
                    lst.append(k)
                    lst.sort()
            if len(lst) > 0:
                out.append(lst)
        return out


if __name__ == '__main__':
    solution = Solution()
    # sug = solution.suggestedProducts(
    #     ["havana"], 'havana')
    sug = solution.suggestedProducts(
        ["mobile", "mouse", "moneypot", "monitor", "mousepad"], 'mouse')
    print(sug)
