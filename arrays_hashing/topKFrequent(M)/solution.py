class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        hashmap = {} # key = num, value = count 

        for num in nums:
            
            if num not in hashmap.keys():
                hashmap[num] = 1
            else:
                hashmap[num] += 1
        
        hashmap = dict(sorted(hashmap.items(), key=lambda item: item[1], reverse=True)) # sort hashmap in descending order of values
        
        return list(hashmap.keys())[:k]
        