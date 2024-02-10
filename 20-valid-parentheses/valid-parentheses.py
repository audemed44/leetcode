class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        closeOpen = {")":"(","]":"[","}":"{"}
        for c in s:
            if c in closeOpen:
                if len(stack) > 0 and stack[-1] == closeOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return len(stack) == 0

                
        