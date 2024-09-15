class Solution:
    def isValid(self, s: str) -> bool:
        
        brackets = {'(':')', '[':']', '{':'}'}
        stack = []

        for ch in s:
            if ch in brackets.keys():
                stack.append(ch)
            if ch in brackets.values():
                if len(stack) > 0 and ch == brackets[stack[-1]]:
                    stack.pop()
                else:
                    return False
        
        return len(stack) == 0