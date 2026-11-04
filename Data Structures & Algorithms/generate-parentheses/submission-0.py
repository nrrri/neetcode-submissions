class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # if open == close -> any
        # open < n -> open
        # if open > close -> close
        # valid open == close == n

        stack = []
        result = []

        def backtrack(opn, cls):
            if opn == cls == n:
                result.append("".join(stack))
                return

            if opn < n:
                stack.append("(")
                backtrack(opn + 1, cls)
                stack.pop()

            if cls < opn:
                stack.append(")")
                backtrack(opn, cls + 1)
                stack.pop()

        backtrack(0, 0)
        return result
