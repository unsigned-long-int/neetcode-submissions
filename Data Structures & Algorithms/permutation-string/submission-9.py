class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s_1 = [0] * 26
        s_2 = [0] * 26

        for i in range(len(s1)):
            i_1 = ord(s1[i]) - ord('a')
            i_2 = ord(s2[i]) - ord('a')

            s_1[i_1] += 1
            s_2[i_2] += 1

        matches = 0

        for i in range(26):
            if s_1[i] == s_2[i]:
                matches+=1


        l = 0
        for i in range(len(s1), len(s2)):
            if matches == 26:
                return True

            index = ord(s2[i]) - ord('a')

            s_2[index] += 1
            if s_2[index] == s_1[index]:
                matches += 1

            if s_2[index] -1 == s_1[index]:
                matches -= 1

            index = ord(s2[l]) - ord('a')
            s_2[index] -= 1
            if s_2[index] == s_1[index]:
                matches += 1
            
            if s_2[index] + 1 == s_1[index]:
                matches -= 1
            l += 1

        return matches == 26