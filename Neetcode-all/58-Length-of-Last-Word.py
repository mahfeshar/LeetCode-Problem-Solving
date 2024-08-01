class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        flag = False
        count = 0
        for i in s[-1::-1]:
            if not(flag)  and i == \ \:
                continue
            flag = True
            if i == \ \:
                break
            count += 1
        return count