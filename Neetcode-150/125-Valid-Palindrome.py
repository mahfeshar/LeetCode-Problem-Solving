class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        l, r = 0, len(s) - 1
        while l < r:
            if not(s[l].isalpha()) and not(s[l].isdigit()):
                l += 1
                continue
            elif not(s[r].isalpha()) and not(s[r].isdigit()):
                r -= 1
                continue
            # print(s[l], s[r], sep=", ")
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True
