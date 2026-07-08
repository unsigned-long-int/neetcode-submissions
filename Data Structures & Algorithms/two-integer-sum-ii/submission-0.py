class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = {}
        for index in range(len(numbers)):
            complement = target - numbers[index]
            if complement in seen and complement != numbers[index]:
                return [seen[complement] + 1, index + 1]
            seen[numbers[index]] = index