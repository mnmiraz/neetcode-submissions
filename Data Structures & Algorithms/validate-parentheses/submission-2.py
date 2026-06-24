class Solution:
    def isValid(self, s: str) -> bool:
        if s is None:
            return False

        stack = []
        for char in s:
            if char in "([{":
                stack.append(char)
            elif char == ")":
                if not stack or stack[-1] != "(":
                    return False
                stack.pop()
            elif char == "]":
                if not stack or stack[-1] != "[":
                    return False
                stack.pop()
            elif char == "}":
                if not stack or stack[-1] != "{":
                    return False
                stack.pop()
                
        return True if not stack else False
