class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        student_queue = collections.deque(students)
        sandwich_stack = collections.deque(sandwiches) # Use as a stack/queue
        
        rotations = 0
        while student_queue and rotations < len(student_queue):
            if student_queue[0] == sandwich_stack[0]:
                student_queue.popleft()
                sandwich_stack.popleft()
                rotations = 0 # Reset rotations because the queue changed
            else:
                # Student doesn't want it, move them to the back
                student_queue.append(student_queue.popleft())
                rotations += 1
                
        return len(student_queue)
                
            
