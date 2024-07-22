class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = {}

        for i in nums:
            if i not in hashMap:
                hashMap[i] = 1
            else:
                hashMap[i] += 1

        ans = []
        for i in range(k):
            maxValue = -1000000000000
            maxInt = -1
            for k, j in hashMap.items():
                if maxValue < j:
                    maxValue = j
                    maxInt = k
            ans.append(maxInt)
            del(hashMap[maxInt])
        return(ans)