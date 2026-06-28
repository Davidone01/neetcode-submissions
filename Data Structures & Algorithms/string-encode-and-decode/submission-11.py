class Solution:

    def encode(self, strs: List[str]) -> str:
        out =""
        for s in strs:
            out += str(len(s))+"#"+s
        return out
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        #print(s)
        while i < len(s):
            #print(i)
            j = i
            while s[j] != "#":
                j += 1
            #print(j)
            len_w = int(s[i:j])
            #print(len_w)
            res.append(s[j+1:j+1+len_w])
            i = j+len_w+1
        return res
                