class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) <= 1:
            return True
        s_nospace=re.sub(r'[^a-zA-Z0-9]', '', s.lower())
        left = 0
        right = len(s_nospace)-1
        while left < right:
            if s_nospace[left] != s_nospace[right]:
                return False
            else:
                left += 1
                right -= 1
        return True
