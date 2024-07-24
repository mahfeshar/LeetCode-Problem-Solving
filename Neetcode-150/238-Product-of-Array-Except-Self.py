class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # nums = [-1,1,0,-3,3]

        prefix = [0] * len(nums)
        suffix = [0] * len(nums)

        total = 1
        # Prefix
        for i in range(len(nums)):
            total *= nums[i]
            prefix[i] = total
        # print(prefix)

        # Suffix
        total = 1
        for i in range(len(nums) - 1, -1, -1):
            total *= nums[i]
            suffix[i] = total
        # print(suffix)

        solution = []
        for i in range(len(nums)):
            preProd = prefix[i -1 ] if i != 0 else 1
            postProd = suffix[i + 1] if i < len(nums) - 1 else 1
            solution.append(preProd * postProd)
        # print(solution)
        return(solution)
