class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        nums = list(set(nums))

        # bubble sort in o(n)
        for i in range(len(nums)):
            swapped = False
            for j in range(0, len(nums)-i-1):
                if nums[j] > nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
                    swapped = True
            if (swapped == False):
                break
        
        if len(nums) <=3:
            if len(nums) == 3 and nums[0] == nums[1] - 1 and nums[0] == nums[2] - 2:
                return 3
            elif len(nums) == 2 and nums[0] == nums[1] - 1:
                return 2 
            elif len(nums) == 1:
                return 1 
            elif len(nums) == 0:
                return 0
            else: 
                return 1 
        else:
            sequences = []
            counter = 1

            for i in range(0, len(nums)-1):
                if i == len(nums) - 2:
                    sequences.append(counter + 1)
                if nums[i] == nums[i + 1] - 1:
                    counter += 1
                else:
                    sequences.append(counter)
                    counter = 1

            return max(sequences)
        