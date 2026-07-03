class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        out = ""
        i = 0
        while i < max(len(word1), len(word2)):
            if i > len(word1)-1:
                out += word2[i]
            elif i > len(word2)-1:
                out += word1[i]
            else: 
                out += word1[i]+word2[i]
            i += 1
        return out