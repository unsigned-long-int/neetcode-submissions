class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        ts = [(tasks.count(t), t) for t in set(tasks)]

        time = 0
        heapq.heapify_max(ts)
        idles = deque()

        while ts or idles:
            time += 1

            if not ts:
                time = idles[0][2]

            if ts:
                freq, task = heapq.heappop_max(ts)
                freq -= 1
                if freq:
                    idles.append([freq, task, time + n])

            if idles:
                if idles[0][2] == time:
                    freq, task, _ = idles.popleft()
                    heapq.heappush_max(ts, (freq, task))

        return time 