class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq_array = [0] * 26
        if len(s) == len(t):
            for i in s:
                freq_array[ord(i) - ord('a')] += 1
            for i in t:
                freq_array[ord(i) - ord('a')] -= 1
            for i in freq_array:
                if i != 0:
                    return False
            return True

        return False