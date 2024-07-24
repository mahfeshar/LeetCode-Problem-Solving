class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # nums = [0,3,7,2,5,8,4,6,0,1]

        my_set = set(nums)
        longest = 0

        for i in nums:
            if i - 1 not in my_set:
                current = i
                count = 1
                
                while current + 1 in my_set:
                    current += 1
                    count += 1
            
                longest = max(longest, count)
        return longest