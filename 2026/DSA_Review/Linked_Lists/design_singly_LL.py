class Node:
    def __init__(self, data, next_node = None):
        self.data = data
        self.next = next_node

# dummy node, useful for deleting first element
class LinkedList:
    
    def __init__(self):
        self.head = Node(-1)
        self.tail = self.head
    
    def get(self, index: int) -> int:
        curr = self.head.next
        i = 0
        while curr:
            if i == index:
                return curr.data
            i += 1
            curr = curr.next
        return -1 

    def insertHead(self, val: int) -> None:
        newHead = Node(val)
        newHead.next = self.head.next
        self.head.next = newHead
        if self.tail == self.head:
            self.tail = newHead
        

    def insertTail(self, val: int) -> None:
        new_node = Node(val)
        self.tail.next = new_node
        self.tail = new_node
        

    def remove(self, index: int) -> bool:
        curr = self.head
        for i in range(index):
            if curr.next:
                curr = curr.next
            else:
                return False

        if curr.next:
            # if tail
            if curr.next == self.tail:
                self.tail = curr
            curr.next = curr.next.next
            return True
        return False
    
    def getValues(self) -> List[int]:
        curr = self.head.next
        arr = []
        while curr:
            arr.append(curr.data)
            curr = curr.next
        return arr
        
