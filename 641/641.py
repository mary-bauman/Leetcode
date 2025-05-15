class MyCircularDeque:
    def __init__(self, k: int):
        self.dq = deque([])
        self.maxLen = k

    def insertFront(self, value: int) -> bool:
        if len(self.dq) == self.maxLen: return False
        self.dq.extendleft([value])
        return True

    def insertLast(self, value: int) -> bool:
        if len(self.dq) == self.maxLen: return False
        self.dq.extend([value])
        return True

    def deleteFront(self) -> bool:
        if len(self.dq)==0: return False
        self.dq.popleft()
        return True

    def deleteLast(self) -> bool:
        if len(self.dq)==0: return False
        self.dq.pop()
        return True

    def getFront(self) -> int:
        if len(self.dq)==0: return -1
        return self.dq[0]

    def getRear(self) -> int:
        if len(self.dq)==0: return -1
        return self.dq[-1]

    def isEmpty(self) -> bool:
        return len(self.dq)==0

    def isFull(self) -> bool:
        return len(self.dq)==self.maxLen


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
