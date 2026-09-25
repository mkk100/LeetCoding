class MyCircularQueue(object):

    def __init__(self, k):
        """
        :type k: int
        """
        self.k = k
        self.cap = 0
        self.front = 0
        self.rear = 0
        self.q = [0] * k
        

    def enQueue(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if self.cap == self.k:
            return False
        self.q[self.rear % self.k] = value
        self.rear += 1
        self.cap += 1
        return True

    def deQueue(self):
        """
        :rtype: bool
        """
        if self.cap == 0:
            return False
        self.front += 1
        self.cap -= 1
        return True

    def Front(self):
        """
        :rtype: int
        """
        if self.cap == 0:
            return -1
        return self.q[self.front % self.k]
        

    def Rear(self):
        """
        :rtype: int
        """        
        if self.cap == 0:
            return -1
        return self.q[(self.rear - 1)% self.k]
        

    def isEmpty(self):
        """
        :rtype: bool
        """
        return self.cap == 0
        

    def isFull(self):
        """
        :rtype: bool
        """
        return self.cap == self.k
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()