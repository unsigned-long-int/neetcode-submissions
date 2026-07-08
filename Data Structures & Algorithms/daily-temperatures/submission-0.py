class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = []
        for i in range(len(temperatures)):
            temp = temperatures[i]
            res.append(0)
            for j in range(i +1, len(temperatures)):
                if temp < temperatures[j]:
                    res.pop()
                    res.append(j-i)
                    break 

        return res