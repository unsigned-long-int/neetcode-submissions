class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        frequency = [0] * 26
        for t in tasks:
            nr = ord(t) - ord('A')
            frequency[nr] += 1

        frequency = [c for c in frequency if c]
        heapq.heapify_max(frequency)
        print(frequency)

        time = 0
        task_queue = deque()

        while task_queue or frequency:
            time += 1

            if not frequency:
                time = task_queue[0][1]
            else:
                freq = heapq.heappop_max(frequency)
                freq -= 1
                if freq:
                    task_queue.append([freq, time + n])
            if task_queue and task_queue[0][1] == time:
                heapq.heappush_max(frequency, task_queue.popleft()[0])

        return time