class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s_1 = [0] * 26 # number of lcase char in alphabet
        s_2 = [0] * 26
        for i in range(len(s1)):
            is1 = ord(s1[i]) - ord('a')
            is2 = ord(s2[i]) - ord('a')

            s_2[is2] += 1
            s_1[is1] += 1

        matches = 0
        for i in range(26):
            if s_1[i] == s_2[i]:
                matches += 1

        l = 0
        for i in range(len(s1), len(s2)):
            if matches == 26:
                return True

            index_1 = ord(s2[i]) - ord('a')
            s_2[index_1] += 1

            if s_2[index_1] == s_1[index_1]:
                matches += 1
            elif s_2[index_1] - 1 == s_1[index_1]:
                matches -= 1

            index_2 = ord(s2[l]) - ord('a')
            s_2[index_2] -= 1

            if s_2[index_2] == s_1[index_2]:
                matches += 1
            elif s_2[index_2] + 1 == s_1[index_2]:
                matches -= 1

            l += 1
        print(matches)
        return matches == 26






