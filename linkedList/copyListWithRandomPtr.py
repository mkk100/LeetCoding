class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        hashMap = {None: None}

        cur = head
        while cur:
            copy = Node(cur.val)
            hashMap[cur] = copy
            cur = cur.next
        
        cur = head
        while cur:
            copy = hashMap[cur]
            copy.next = hashMap[cur.next]
            copy.random = hashMap[cur.random]
            cur = cur.next
        
        return hashMap[head]
# O(N) for time and O(N) for space 
# use hashmap and 2 pass.