class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        canDrinkCount=numBottles
        while numBottles>=numExchange:
            cv=(numBottles/numExchange).__floor__()
            canDrinkCount+=cv
            numBottles=cv+(numBottles%numExchange)
        return canDrinkCount


if __name__=='__main__':
    s=Solution()
    print(s.numWaterBottles(9,3))
    print(s.numWaterBottles(15,4))
    print(s.numWaterBottles(6,4))