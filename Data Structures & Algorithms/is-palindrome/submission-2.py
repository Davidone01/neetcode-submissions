class Solution:
    def isPalindrome(self, s: str) -> bool:
        reverse_s = ""
        for i in range(len(s)-1, -1, -1):
            if s[i].isalnum():
                reverse_s += s[i].lower()
        clean_s = ""
        for i in range(len(s)):
            if s[i].isalnum():
                clean_s += s[i].lower()
        #print(clean_s)

        return clean_s == reverse_s