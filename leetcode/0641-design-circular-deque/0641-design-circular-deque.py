class MyCircularDeque:

    def __init__(self, k: int):
        self.size = k
        self.que = [None] * k
        self.front = -1
        self.rear = -1
        

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False

        if self.isEmpty():
            self.front = self.rear = 0
        else:
            self.front = (self.front - 1 + self.size) % self.size

        self.que[self.front] = value
        return True
            

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False

        if self.isEmpty():
            self.front = self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.size

        self.que[self.rear] = value
        return True
        
    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False

        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.size

        return True

    def deleteLast(self) -> bool:
        if self.rear == -1:
            return False

        if self.front == self.rear:
            self.que[self.rear] = None
            self.front = self.rear = -1
            return True

        self.que[self.rear] = None
        self.rear = (self.rear - 1 + self.size) % self.size
        return True
        

    def getFront(self) -> int:
        if self.front == -1:
            return -1
        else:
            return self.que[self.front]
        

    def getRear(self) -> int:
        if self.rear == -1:
            return -1
        else:
            return self.que[self.rear]

    def isEmpty(self) -> bool:
        return self.front == -1
        

    def isFull(self) -> bool:
        return (self.rear + 1) % self.size == self.front
        


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