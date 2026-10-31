class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # sliding check
        l = 0
        r = len(s1) - 1
        result = False
        d = {}
        fix = {}
        for i in range(len(s1)):
            fix[s1[i]] = fix.get(s1[i], 0) + 1
        while r < len(s2):
            wd = s2[l : r + 1]
            d = {}
            for i in range(len(wd)):
                d[wd[i]] = d.get(wd[i], 0) + 1
            if d == fix:
                result = True
            r += 1
            l += 1

        return result
