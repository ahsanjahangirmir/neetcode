class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1

        while l < r:
            
            twoSum = numbers[l] + numbers[r]
            
            if twoSum == target:
                return [l + 1, r + 1]
            
            if twoSum < target:
                l += 1
            
            if twoSum > target:
                r -= 1

        return []