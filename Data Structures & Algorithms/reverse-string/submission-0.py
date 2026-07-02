class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s)
        out = ""
        for i in range(n-1, -1, -1):
            out = out+s[i]
        for i in range(len(out)):
            s[i] = out[i]
        return out