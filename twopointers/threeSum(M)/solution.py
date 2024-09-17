class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        res = set()
        nums.sort()        

        for i in range(len(nums) - 2):
            
            l = i + 1 
            r = len(nums) - 1

            while l < r:

                threeSum = nums[i] + nums[l] + nums[r]

                if threeSum == 0:
                    res.add((nums[i], nums[l], nums[r]))  
                    l += 1

                if threeSum < 0:
                    l += 1
                else:
                    r -= 1
        
        return [list(tup) for tup in res]