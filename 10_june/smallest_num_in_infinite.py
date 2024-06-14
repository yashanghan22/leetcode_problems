class SmallestInfiniteSet:
    lst = []

    def __init__(self):
        for i in range(1, 20):
            self.lst.append(i)

    def popSmallest(self) -> int:
        small = self.lst[0]
        self.lst.remove(small)
        print(small)
        return small

    def addBack(self, num: int) -> None:
        if num not in self.lst:
            self.lst.append(num)
            self.lst.sort()


if __name__ == "__main__":
    infinite = SmallestInfiniteSet()
    # infinite.__init__()
    infinite.addBack(1)
    infinite.popSmallest()
    infinite.popSmallest()
    infinite.popSmallest()
    infinite.addBack(1)
    infinite.popSmallest()
    infinite.popSmallest()
    infinite.popSmallest()
    print(infinite.lst)
