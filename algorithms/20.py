class Solution:
    def isValid(self, string: str) -> bool:
        stack = []
        for s in string:
            if s in ['(', '{', '[']:
                stack.append(s)
            elif not stack:
                return False
            elif (s == ')' and stack[-1] == '(' or
                  s == '}' and stack[-1] == '{' or
                  s == ']' and stack[-1] == '['):
                stack.pop()
            else:
                return False
        return not stack
