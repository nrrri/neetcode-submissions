class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            # pairs = even
            return False

        closeToOpen = {")": "(", "}": "{", "]": "["}
        stack = []
        for c in s:
            # check key(c) if close
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return True if not stack else False
