class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def evaluate(op1: int, op2: int, operator: chr) -> int:
            if operator == "+":
                return op1 + op2
            elif operator == "-":
                return op1 - op2
            elif operator == "*":
                return op1 * op2
            elif operator == "/":
                return int(op1 / op2)
        
        operators = ["+", "-", "/", "*"]
        stack = []

        for token in tokens:
            if token not in operators:
                stack.append(int(token))
            else:
                op2 = stack.pop()
                op1 = stack.pop()
                stack.append(evaluate(op1, op2, token))
        
        return stack[-1]