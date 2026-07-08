class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""

        for word in strs:
            encoded += str(len(word))
            encoded += "#"
            encoded += word

        return encoded

    def decode(self, s: str) -> List[str]:
        decoded, i = [], 0

        while i < len(s):
            j = i 
            while s[j] != '#':
                j += 1
            
            len_ = int(s[i:j])
            decoded.append(s[j+1:len_ + j + 1])
            i = j + 1 + len_

        return decoded


            
