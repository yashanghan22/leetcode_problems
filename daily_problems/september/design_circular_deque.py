from collections import deque

class MyCircularDeque:

    def __init__(self, k: int):
        self.que=deque()
        self.k=k

    def insertFront(self, value: int) -> bool:
        if len(self.que)==self.k:
            return False
        self.que.appendleft(value)
        return True

    def insertLast(self, value: int) -> bool:
        if len(self.que)==self.k:
            return False
        self.que.append(value)
        return True

    def deleteFront(self) -> bool:
        if len(self.que)==0:
            return False
        self.que.popleft()
        return True

    def deleteLast(self) -> bool:
        if len(self.que)==0:
            return False
        self.que.pop()
        return True

    def getFront(self) -> int:
        if len(self.que)>0:
            return self.que[0]
        else:
            return -1

    def getRear(self) -> int:
        if len(self.que)>0:
            return self.que[-1]
        else:
            return -1
        
    def isEmpty(self) -> bool:
        return len(self.que)==0

    def isFull(self) -> bool:
        return len(self.que)==self.k


if __name__=='__main__':
    obj = MyCircularDeque(3)
    print(obj.insertFront(2))
    print(obj.insertLast(3))
    print(obj.insertLast(4))
    print(obj.insertLast(7))
    print(obj.deleteFront())
    print(obj.deleteLast())
    print(obj.getFront())
    print(obj.getRear())
    print(obj.isEmpty())
    print(obj.isFull())