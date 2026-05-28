class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)
        q = collections.deque()
        time = 0

        while maxHeap or q:
            time += 1
            if maxHeap:
                task = heapq.heappop(maxHeap) + 1 # decreasing task by 1
                if task != 0: # if we havent' finished processing, then readd
                    q.append([task, time + n])

            if q and q[0][1] == time: # if first of queue
                heapq.heappush(maxHeap, q.popleft()[0])
        return time
