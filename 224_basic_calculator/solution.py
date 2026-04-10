class Solution:
    def calculate(self, s: str) -> int:
        num = 0
        result = 0
        sign = 1
        stack = []
        
        for char in s:
            if char.isdigit():
                num = num * 10 + int(char)
            elif char == '+':
                result += sign * num
                num = 0
                sign = 1
            elif char == '-':
                result += sign * num
                num = 0
                sign = -1
            elif char == '(':
                stack.append(result)
                stack.append(sign)
                result = 0
                num = 0
                sign = 1
            elif char == ')':
                result += sign * num
                num = 0
                popped_sign = stack.pop()
                popped_result = stack.pop()
                result = popped_result + popped_sign * result
            
        result += sign * num
            
        return result