class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # sliding check
        l = 0
        r = len(s1) - 1
        result = False
        while r < len(s2):
            wd = sorted(s2[l : r + 1])
            if sorted(s1) == wd:
                result = True
            r += 1
            l += 1

        return result
