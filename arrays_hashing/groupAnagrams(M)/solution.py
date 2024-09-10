class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        if len(strs) == 0 or len(strs) == 1:
            return [strs]

        hashmap = {}

        for i in range(len(strs)):
            
            string = strs[i]
            
            if ''.join(sorted(string)) in hashmap.keys():
                hashmap[''.join(sorted(string))].append(string)

            else:
                hashmap[''.join(sorted(string))] = [string]
        
        return list(hashmap.values())