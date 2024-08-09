class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        target = 0
        output = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            j, k = i + 1, len(nums)-1
            
            while j < k:
                sum = nums[i] + nums[j] + nums[k]
                
                if sum == target:
                    output.append([nums[i], nums[j], nums[k]])
                    j+=1
                    k-=1
                    while j < k and nums[j] == nums[j-1]:
                        j+=1
                    while j < k and nums[k] == nums[k+1]:
                        k-=1
                        
                elif sum < target:
                    j+=1
                else:
                    k-=1
        return output