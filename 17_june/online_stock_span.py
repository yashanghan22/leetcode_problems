class StockSpanner:
    ls = []
    stack = []

    def __init__(self):
        self.ls = [[],]
        # self.stack = []

    def next(self, price: int) -> int:
        self.stack = []
        self.stack.append(None)
        v = [1]*(len(self.ls))
        # print(v)
        self.stack.extend(v)
        self.ls.append([price])
        # print(self.stack)
        for i in range(len(self.ls)-1, 0, -1):
            for j in range((len(self.ls)-1)-(len(self.ls) - i), 0, -1):
                if self.ls[i][0] and self.ls[j][0] > self.ls[i][0]:
                    # print(i, j)
                    self.stack[i] = i-j
                    break
        # print(self.stack)
        return price


if __name__ == "__main__":
    stockSpan = StockSpanner()
    stockSpan.next(100)
    stockSpan.next(80)
    stockSpan.next(60)
    stockSpan.next(70)
    stockSpan.next(60)
    stockSpan.next(75)
    stockSpan.next(85)
    print(stockSpan.ls)
    print(stockSpan.stack)
