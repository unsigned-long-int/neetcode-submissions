class TimeMap:

    def __init__(self):
        self.hash_map = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hash_map[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        res, values = "", self.hash_map.get(key, [])
        l, r = 0, len(values) - 1
        while l<=r:
            mid = (l + r) // 2
            if values[mid][0] <= timestamp:
                res = values[mid][1]
                l = mid + 1
            else:
                r = mid - 1
        return res
