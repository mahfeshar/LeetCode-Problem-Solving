class Solution:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        ans = [0] * len(temps)
        s = []
        for i, temp in enumerate(temps):
            while s and temps[s[-1]] < temp:
                x = s.pop()
                ans[x] = i - x
            s.append(i)
        return ans