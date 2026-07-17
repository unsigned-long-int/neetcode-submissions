class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        ts = [(tasks.count(t), ord(t) - ord('A')) for t in set(tasks)]
        heapq.heapify_max(ts)
        idle = deque()

        time = 0
        while idle or ts:
            time += 1
            if not ts:
                time = idle[0][2]

            if ts:
                freq, task = heapq.heappop_max(ts)
                freq -= 1
                if freq:
                    idle.append([freq, task, time + n])
            if idle:
                if idle[0][2] == time:
                    freq, task, _ = idle.popleft()
                    heapq.heappush_max(ts, (freq, task))

        return time



            