class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        product = 1
        res = []

        for num in nums:
            if num != 0:
                product *= num
        
        if nums.count(0) == 0:
            return [product//num for num in nums]
        elif nums.count(0) == 1:
            res = [0] * len(nums)
            res[nums.index(0)] = product
        else:
            res = [0] * len(nums)

        return res