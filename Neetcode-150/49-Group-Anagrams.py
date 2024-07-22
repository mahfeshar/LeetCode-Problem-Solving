class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # I will use Hash map
        hashMap = {}
        for i in strs:
            sortedI = \\.join(sorted(i))
            if sortedI not in hashMap:
                hashMap[sortedI] = [i]
            else:
                hashMap[sortedI].append(i)

        ans = []
        # Learn How to use HashMap and what happens behind the scene
        for i in hashMap:
            ans.append(hashMap[i])
            
        return ans