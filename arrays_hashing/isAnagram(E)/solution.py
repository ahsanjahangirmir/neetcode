class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        s_letters = [s[i] for i in range(len(s))]
        t_letters = [t[i] for i in range(len(t))]

        return sorted(t_letters) == sorted(s_letters)
        