class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        idle = deque()
        ts = [(tasks.count(t), t) for t in set(tasks)]
        heapq.heapify_max(ts)

        time = 0
        while ts or idle:
            time += 1
            if not ts:
                time = idle[0][2]

            if ts:
                freq, task = heapq.heappop_max(ts)
                freq -= 1
                if freq:
                    idle.append((task, freq, time + n))

            if idle and time == idle[0][2]:
                task, freq, _ = idle.popleft()
                heapq.heappush_max(ts, (freq, task))
        return time 

