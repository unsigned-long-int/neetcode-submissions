class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        c_1 = [0] * 26
        c_2 = [0] * 26

        for i in range(len(s1)):
            i1 = ord(s1[i]) - ord('a')
            c_1[i1] += 1
            i2 = ord(s2[i]) - ord('a')
            c_2[i2] += 1

        matches = 0
        for i in range(26):
            if c_1[i] == c_2[i]:
                matches += 1
        
        l = 0
        for i in range(len(s1), len(s2)):
            if matches == 26:
                return True

            i1 = ord(s2[i]) - ord('a')
            c_2[i1] += 1

            if c_2[i1] == c_1[i1]:
                matches += 1
            elif c_2[i1] - 1 == c_1[i1]:
                matches -= 1

            i2 = ord(s2[l]) - ord('a')
            c_2[i2] -= 1
            if c_2[i2] == c_1[i2]:
                matches += 1
            elif c_2[i2] + 1 == c_1[i2]:
                matches -= 1

            l += 1

        return matches == 26 






