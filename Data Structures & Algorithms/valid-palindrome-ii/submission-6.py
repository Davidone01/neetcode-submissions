class Solution:
    def validPalindrome(self, s: str) -> bool:
        bonus = 1
        bonus_2 = 1
        left = 0
        right = len(s)-1
        while left <= right:
            if s[left] != s[right]:
                bonus -= 1
                right -= 1
                continue
            left += 1
            right -= 1
        left = 0
        right = len(s)-1
        while left <= right:
            if s[left] != s[right]:
                bonus_2 -= 1
                left += 1
                continue
            left += 1
            right -= 1
        return (bonus >= 0 or bonus_2>= 0)