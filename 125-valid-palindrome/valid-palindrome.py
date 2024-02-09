class Solution:
    def isPalindrome(self, s: str) -> bool:
        an_str = "".join(ch.lower() for ch in s if ch.isalnum())
        l = 0
        r = len(an_str)-1
        while r >= l:
            if an_str[l] != an_str[r]:
                return False
            l += 1
            r -= 1
        return True        