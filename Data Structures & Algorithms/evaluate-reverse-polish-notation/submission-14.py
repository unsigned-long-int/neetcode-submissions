class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if not tokens:
            return 0
        stack = []
        amount = int(tokens[0])
        operators = "+-*/"
        for i in range(0, len(tokens)):
            stack.append(tokens[i])
            if tokens[i] in operators:
                op = stack.pop()
                right = stack.pop()
                left = stack.pop()
                amount = int(eval(f'{left} {op} {right}'))
                stack.append(amount)
                continue

        return amount