class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        frequency = [0] * 26
        for t in tasks:
            nr = ord(t) - ord('A')
            frequency[nr] += 1
        frequency = [f for f in frequency if f]
        
        heapq.heapify_max(frequency)
        tasks_queue = deque()
        time = 0
        while tasks_queue or frequency:
            time += 1

            if not frequency:
                time = tasks_queue[0][1]
            
            if frequency:
                freq = heapq.heappop_max(frequency)
                freq -= 1
                if freq:
                    tasks_queue.append([freq, n + time])

            if tasks_queue and tasks_queue[0][1] == time:
                heapq.heappush_max(frequency, tasks_queue.popleft()[0])
        return time